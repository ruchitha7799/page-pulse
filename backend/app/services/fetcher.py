import time

import httpx


class FetchError(Exception):
    """Base exception for webpage fetching errors."""


class FetchTimeoutError(FetchError):
    """Raised when the target webpage takes too long to respond."""


class FetchConnectionError(FetchError):
    """Raised when the target webpage cannot be reached."""


class NonHTMLResponseError(FetchError):
    """Raised when the target URL does not return HTML."""


async def fetch_webpage(url: str) -> dict:
    timeout = httpx.Timeout(10.0)

    try:
        start_time = time.perf_counter()

        async with httpx.AsyncClient(
            timeout=timeout,
            follow_redirects=True,
        ) as client:
            response = await client.get(
                url,
                headers={
                    "User-Agent": "PagePulse/1.0"
                },
            )

        end_time = time.perf_counter()

        response_time_ms = round(
            (end_time - start_time) * 1000
        )

    except httpx.TimeoutException as exc:
        raise FetchTimeoutError(
            "The target website took too long to respond."
        ) from exc

    except httpx.RequestError as exc:
        raise FetchConnectionError(
            "Unable to connect to the target website."
        ) from exc

    content_type = response.headers.get(
        "content-type",
        ""
    ).lower()

    if "text/html" not in content_type:
        raise NonHTMLResponseError(
            "The provided URL does not return an HTML page."
        )

    return {
        "status_code": response.status_code,
        "response_time_ms": response_time_ms,
        "html": response.text,
    }