from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_audit_url_success(monkeypatch):
    async def mock_fetch_webpage(url):
        return {
            "status_code": 200,
            "response_time_ms": 120,
            "html": """
                <html>
                    <head>
                        <title>Test Website</title>
                        <meta
                            name="description"
                            content="A test website for Page Pulse."
                        >
                    </head>

                    <body>
                        <h1>Welcome</h1>

                        <img
                            src="good.jpg"
                            alt="A good image"
                        >

                        <img src="missing-alt.jpg">

                        <p>
                            This is sample content
                            for testing Page Pulse.
                        </p>
                    </body>
                </html>
            """,
        }

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

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True

    assert data["data"]["url"] == "https://example.com/"

    assert data["data"]["http_status"] == 200

    assert data["data"]["response_time_ms"] == 120

    assert data["data"]["page_title"] == "Test Website"

    assert (
        data["data"]["meta_description"]
        == "A test website for Page Pulse."
    )

    assert data["data"]["h1_count"] == 1

    assert data["data"]["images_missing_alt"] == 1

    assert data["data"]["word_count"] > 0