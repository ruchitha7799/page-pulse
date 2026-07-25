from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.schemas.audit import (
    AuditRequest,
    AuditResponse,
    ErrorResponse,
)
from app.services.fetcher import (
    FetchConnectionError,
    FetchTimeoutError,
    NonHTMLResponseError,
    fetch_webpage,
)
from app.services.parser import parse_html


router = APIRouter(
    prefix="/api/v1",
    tags=["Audit"],
)

@router.post(
    "/audit",
    response_model=AuditResponse,
    responses={
        422: {
            "model": ErrorResponse,
            "description": "Invalid URL or request data.",
        },
        415: {
            "model": ErrorResponse,
            "description": "The target URL does not return HTML.",
        },
        502: {
            "model": ErrorResponse,
            "description": "Unable to connect to the target website.",
        },
        504: {
            "model": ErrorResponse,
            "description": "The target website timed out.",
        },
        500: {
            "model": ErrorResponse,
            "description": "Unexpected server error.",
        },
    },
)
async def audit_url(request: AuditRequest):
    """
    Audit a webpage URL and return a structured report.
    """

    try:
        fetched_page = await fetch_webpage(
            str(request.url)
        )

        parsed_data = parse_html(
            fetched_page["html"]
        )

        return AuditResponse(
            success=True,
            data={
                "url": str(request.url),
                "http_status": fetched_page["status_code"],
                "response_time_ms": fetched_page[
                    "response_time_ms"
                ],
                **parsed_data,
            },
        )

    except FetchTimeoutError as exc:
        return JSONResponse(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            content={
                "success": False,
                "error": {
                    "code": "TIMEOUT",
                    "message": str(exc),
                },
            },
        )

    except FetchConnectionError as exc:
        return JSONResponse(
            status_code=status.HTTP_502_BAD_GATEWAY,
            content={
                "success": False,
                "error": {
                    "code": "CONNECTION_ERROR",
                    "message": str(exc),
                },
            },
        )

    except NonHTMLResponseError as exc:
        return JSONResponse(
            status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            content={
                "success": False,
                "error": {
                    "code": "NON_HTML",
                    "message": str(exc),
                },
            },
        )

    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "success": False,
                "error": {
                    "code": "INTERNAL_ERROR",
                    "message": (
                        "An unexpected error occurred "
                        "while auditing the webpage."
                    ),
                },
            },
        )