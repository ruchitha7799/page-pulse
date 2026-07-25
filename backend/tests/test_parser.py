from app.services.parser import parse_html


def test_parse_html_happy_path():
    html = """
    <html>
        <head>
            <title>Test Page</title>
            <meta
                name="description"
                content="This is a test page."
            >
        </head>

        <body>
            <h1>Welcome</h1>

            <img src="image1.jpg">

            <img
                src="image2.jpg"
                alt="A beautiful image"
            >

            <p>
                Hello everyone.
                This is a test webpage.
            </p>
        </body>
    </html>
    """

    result = parse_html(html)

    assert result["page_title"] == "Test Page"

    assert (
        result["meta_description"]
        == "This is a test page."
    )

    assert result["h1_count"] == 1

    assert result["images_missing_alt"] == 1

    assert result["word_count"] > 0

def test_parse_html_missing_metadata():
    html = """
    <html>
        <body>
            <h1>Only Heading</h1>
            <p>Some content.</p>
        </body>
    </html>
    """

    result = parse_html(html)

    assert result["page_title"] is None

    assert result["meta_description"] is None

    assert result["h1_count"] == 1

    assert result["images_missing_alt"] == 0

    assert result["word_count"] > 0


def test_parse_html_images_with_missing_alt():
    html = """
    <html>
        <body>
            <img src="one.jpg">
            <img src="two.jpg" alt="">
            <img src="three.jpg" alt="A valid image">
        </body>
    </html>
    """

    result = parse_html(html)

    assert result["images_missing_alt"] == 2