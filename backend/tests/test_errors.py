from fastapi.testclient import TestClient

from app.main import app
from app.services.fetcher import (
    FetchConnectionError,
    FetchTimeoutError,
    NonHTMLResponseError,
)


client = TestClient(app)


def test_invalid_url():
    response = client.post(
        "/api/v1/audit",
        json={
            "url": "hello",
        },
    )

    assert response.status_code == 422

    data = response.json()

    assert data["success"] is False

    assert data["error"]["code"] == "INVALID_URL"


def test_timeout_error(monkeypatch):
    async def mock_fetch_webpage(url):
        raise FetchTimeoutError(
            "The target website took too long to respond."
        )

    monkeypatch.setattr(
        "app.routes.audit.fetch_webpage",
        mock_fetch_webpage,
    )

    response = client.post(
        "/api/v1/audit",
        json={
            "url": "https://example.com",
        },
    )

    assert response.status_code == 504

    data = response.json()

    assert data["success"] is False

    assert data["error"]["code"] == "TIMEOUT"


def test_connection_error(monkeypatch):
    async def mock_fetch_webpage(url):
        raise FetchConnectionError(
            "Unable to connect to the target website."
        )

    monkeypatch.setattr(
        "app.routes.audit.fetch_webpage",
        mock_fetch_webpage,
    )

    response = client.post(
        "/api/v1/audit",
        json={
            "url": "https://example.com",
        },
    )

    assert response.status_code == 502

    data = response.json()

    assert data["success"] is False

    assert data["error"]["code"] == "CONNECTION_ERROR"


def test_non_html_response(monkeypatch):
    async def mock_fetch_webpage(url):
        raise NonHTMLResponseError(
            "The provided URL does not return an HTML page."
        )

    monkeypatch.setattr(
        "app.routes.audit.fetch_webpage",
        mock_fetch_webpage,
    )

    response = client.post(
        "/api/v1/audit",
        json={
            "url": "https://example.com",
        },
    )

    assert response.status_code == 415

    data = response.json()

    assert data["success"] is False

    assert data["error"]["code"] == "NON_HTML"
    