from bs4 import BeautifulSoup


def parse_html(html: str) -> dict:
    """
    Parse HTML content and extract webpage audit information.
    """

    soup = BeautifulSoup(html, "html.parser")

    # Extract page title
    title_tag = soup.find("title")
    page_title = (
        title_tag.get_text(strip=True)
        if title_tag
        else None
    )

    # Extract meta description
    meta_description_tag = soup.find(
        "meta",
        attrs={"name": lambda value: value and value.lower() == "description"},
    )

    meta_description = None

    if meta_description_tag:
        meta_description = meta_description_tag.get("content")

        if meta_description:
            meta_description = meta_description.strip()

    # Count H1 elements
    h1_count = len(soup.find_all("h1"))

    # Count images that are missing useful alt text
    images = soup.find_all("img")

    images_missing_alt = 0

    for image in images:
        alt = image.get("alt")

        if alt is None or not alt.strip():
            images_missing_alt += 1

    # Remove non-visible elements before calculating word count
    for element in soup(
        ["script", "style", "noscript", "template"]
    ):
        element.decompose()

    visible_text = soup.get_text(
        separator=" ",
        strip=True,
    )

    words = visible_text.split()

    word_count = len(words)

    return {
        "page_title": page_title,
        "meta_description": meta_description,
        "h1_count": h1_count,
        "images_missing_alt": images_missing_alt,
        "word_count": word_count,
    }