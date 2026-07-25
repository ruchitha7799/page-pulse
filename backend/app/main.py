import os

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.routes.audit import router as audit_router


app = FastAPI(
    title="Page Pulse API",
    description="A web tool that audits webpages and returns a structured report.",
    version="1.0.0",
)

allowed_origins = [
    origin.strip()
    for origin in os.getenv(
        "ALLOWED_ORIGINS",
        "http://127.0.0.1:5500,http://localhost:5500",
    ).split(",")
    if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(audit_router)


@app.get("/health")
def health():
    return {"success": True, "message": "healthy"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "error": {
                "code": "INVALID_URL",
                "message": "Please provide a valid HTTP or HTTPS URL.",
            },
        },
    )


@app.get("/")
def root():
    return {"success": True, "message": "Page Pulse API is running"}