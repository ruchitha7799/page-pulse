from typing import Any

from pydantic import BaseModel, HttpUrl


class AuditRequest(BaseModel):
    url: HttpUrl


class AuditData(BaseModel):
    url: str
    http_status: int
    response_time_ms: int
    page_title: str | None
    meta_description: str | None
    h1_count: int
    images_missing_alt: int
    word_count: int


class AuditResponse(BaseModel):
    success: bool
    data: AuditData


class ErrorDetail(BaseModel):
    code: str
    message: str


class ErrorResponse(BaseModel):
    success: bool
    error: ErrorDetail