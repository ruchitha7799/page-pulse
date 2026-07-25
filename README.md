# Page Pulse 🚀

Page Pulse is a web-based webpage auditing tool that analyzes a publicly accessible URL and returns a structured report containing useful information about the page's performance, content structure, SEO, and accessibility-related signals.

The application accepts a URL, fetches the webpage, analyzes its HTML, and presents the results through a simple web interface.

---

## 🌐 Live Demo

### Frontend

[Open Page Pulse](https://page-pulse-frontend-wb3y.onrender.com/)

> Replace `YOUR_FRONTEND_RENDER_URL` with the actual URL of the deployed frontend.

### Backend API

[Open Page Pulse API](https://page-pulse-wbkb.onrender.com/)

### API Documentation

[Open Swagger API Documentation](https://page-pulse-wbkb.onrender.com/docs)

### GitHub Repository

[View Source Code](https://github.com/ruchitha7799/page-pulse)

---

# ✨ Features

Page Pulse provides the following webpage audit information:

- HTTP response status
- Approximate response time
- Page title
- Meta description
- H1 heading count
- Number of images missing alt text
- Approximate word count

The application also provides:

- URL validation
- Timeout handling
- Connection error handling
- Non-HTML response handling
- Structured API error responses
- Loading state during audits
- Clean frontend result presentation
- User-friendly error messages
- Responsive user interface

---

# 🏗️ Architecture

Page Pulse follows a simple client-server architecture.

```text
                    User
                      |
                      v
              Frontend Application
              HTML / CSS / JavaScript
                      |
                      | HTTP POST
                      v
               FastAPI REST API
                      |
                      v
              URL Validation
                      |
                      v
             Webpage Fetcher
                      |
                      v
               HTML Parser
                      |
                      v
             Structured Audit
                  Report
                      |
                      v
             JSON API Response
                      |
                      v
              Frontend Results
```

The application is divided into separate responsibilities:

- **Frontend** handles user interaction and displays audit results.
- **API routes** handle HTTP requests and responses.
- **Fetcher service** handles webpage network requests.
- **Parser service** extracts information from HTML.
- **Schemas** define structured API request and response models.
- **Tests** verify parsing behaviour, successful audits, and error handling.

---

# 📁 Project Structure

```text
Page-Pulse/

├── backend/
│
│   ├── app/
│   │
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   └── audit.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── audit.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── fetcher.py
│   │   │   └── parser.py
│   │   │
│   │   ├── __init__.py
│   │   └── main.py
│   │
│   ├── tests/
│   │   ├── test_audit.py
│   │   ├── test_errors.py
│   │   └── test_parser.py
│   │
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── ARCHITECTURE.md
├── README.md
└── REQUIREMENTS.md
```

---

# 🔌 API Documentation

## Audit a Webpage

### Endpoint

```text
POST /api/v1/audit
```

### Full API URL

```text
https://page-pulse-wbkb.onrender.com/api/v1/audit
```

### Request Body

```json
{
  "url": "https://example.com"
}
```

---

## Successful Response

Example:

```json
{
  "success": true,
  "data": {
    "url": "https://example.com/",
    "http_status": 200,
    "response_time_ms": 185,
    "page_title": "Example Domain",
    "meta_description": null,
    "h1_count": 1,
    "images_missing_alt": 0,
    "word_count": 21
  }
}
```

---

## Response Fields

| Field | Type | Description |
|---|---|---|
| `url` | string | The URL that was audited |
| `http_status` | integer | HTTP response status returned by the target webpage |
| `response_time_ms` | integer | Approximate time taken to fetch the webpage in milliseconds |
| `page_title` | string or null | The content of the HTML `<title>` element |
| `meta_description` | string or null | The content of the meta description, if available |
| `h1_count` | integer | Number of H1 headings found on the page |
| `images_missing_alt` | integer | Number of images that do not contain meaningful alt text |
| `word_count` | integer | Approximate number of words extracted from the webpage |
```

---

# ❌ Error Handling

Page Pulse is designed to fail gracefully instead of crashing when an audit cannot be completed.

The application handles the following cases:

| Scenario | Behaviour |
|---|---|
| Invalid URL | Returns an `INVALID_URL` error |
| Connection failure | Returns a `CONNECTION_ERROR` error |
| Request timeout | Returns a `TIMEOUT` error |
| Non-HTML response | Returns a `NON_HTML_RESPONSE` error |
| Unexpected server failure | Returns a structured error response |

The frontend receives the API error and displays a user-friendly message instead of exposing internal server details.

---

## Invalid URL Example

Request:

```json
{
  "url": "hello"
}
```

Response:

```json
{
  "success": false,
  "error": {
    "code": "INVALID_URL",
    "message": "Please provide a valid HTTP or HTTPS URL."
  }
}
```

---

## Connection Error Example

If the target website cannot be reached, Page Pulse returns a structured connection error rather than allowing the application to crash.

Example:

```json
{
  "success": false,
  "error": {
    "code": "CONNECTION_ERROR",
    "message": "Unable to connect to the target website."
  }
}
```

---

# 🧪 Testing

Page Pulse uses `pytest` for automated testing.

Run all tests from the `backend` directory:

```bash
python -m pytest -v
```

The current test suite verifies:

### HTML Parsing

- Successful parsing of page information
- Handling missing metadata
- Detection of images missing alt text

### API Audit

- Successful webpage audit
- Correct API response structure

### Error Handling

- Invalid URL handling
- Timeout errors
- Connection errors
- Non-HTML response handling

The final local test run passed all 8 tests:

```text
8 passed
```

The test suite is designed so that parsing logic can be tested without relying on real external websites.

---

# ⚙️ Local Setup

## Prerequisites

Make sure you have:

- Python 3.10 or later
- Git
- A modern web browser

---

## 1. Clone the Repository

```bash
git clone https://github.com/ruchitha7799/page-pulse.git
```

Navigate into the project:

```bash
cd page-pulse
```

---

# 🖥️ Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

Swagger API documentation will be available at:

```text
http://127.0.0.1:8000/docs
```

---

# 🌐 Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Start a simple local web server:

```bash
python -m http.server 5500
```

Open the following URL in your browser:

```text
http://127.0.0.1:5500
```

The frontend communicates with the configured FastAPI backend.

---

# 💡 Design Decisions

## 1. Separating Webpage Fetching from HTML Parsing

### Decision

I separated the network fetching logic and HTML parsing logic into independent services.

### Why

The main reason for this decision was testability.

Network requests are slow, unreliable, and dependent on external websites. I did not want parser tests to depend on real network requests.

By separating the parser, I can provide controlled HTML directly to the parser and test its behaviour deterministically.

This separation also makes the application easier to maintain and allows the fetching mechanism to be changed independently in the future.

---

## 2. Using Structured Error Responses

### Decision

I use structured error responses containing both a machine-readable error code and a human-readable message.

For example:

```json
{
  "success": false,
  "error": {
    "code": "INVALID_URL",
    "message": "Please provide a valid HTTP or HTTPS URL."
  }
}
```

### Why

The frontend should not need to understand backend implementation details.

A stable error code allows the frontend to handle different failure types consistently, while the message provides useful information to the user.

This also makes the API easier for another client or frontend to consume.

---

## 3. Separating the Frontend and Backend

### Decision

The frontend and backend are implemented and deployed as separate services.

### Why

This keeps responsibilities clear.

The frontend focuses on:

- User interaction
- Input handling
- Loading states
- Displaying results
- Displaying errors

The backend focuses on:

- URL validation
- Fetching webpages
- Parsing HTML
- Error handling
- Returning structured JSON

Keeping these responsibilities separate makes the system easier to maintain and allows the frontend and backend to be updated independently.

---

# ⚠️ Current Limitations

Page Pulse currently audits publicly accessible HTML webpages.

It does not execute JavaScript-heavy pages in a real browser environment before parsing their content. As a result, information that is rendered only after client-side JavaScript execution may not be included in the audit.

The word count is approximate and is based on extracted webpage text rather than a full browser-rendered DOM.

The current implementation also does not provide a complete Lighthouse-style performance, SEO, or accessibility score.

---

# 🔐 Security Considerations

The application accepts user-provided URLs and makes server-side HTTP requests to those destinations.

For a production-scale version, I would strengthen the URL fetching layer with additional SSRF protections, including:

- Blocking localhost addresses
- Blocking private network ranges
- Blocking loopback addresses
- Blocking cloud metadata endpoints
- Validating resolved IP addresses
- Restricting allowed protocols to HTTP and HTTPS

These protections would help prevent the server from being abused to access internal network resources.

---

# 🚀 Deployment

The application is deployed using Render.

### Frontend

The frontend is deployed as a Render Static Site.

### Backend

The FastAPI backend is deployed as a Render Web Service.

### Backend URL

```text
https://page-pulse-wbkb.onrender.com
```

### API Documentation

```text
https://page-pulse-wbkb.onrender.com/docs
```

The backend is configured to allow requests from the deployed frontend using CORS configuration.

---

# 🔮 What I Would Improve With Another Day

If I had another day to continue developing Page Pulse, I would focus on the following improvements.

## 1. Browser-Based Rendering

I would add optional browser rendering using a tool such as Playwright.

This would allow Page Pulse to analyze content generated dynamically by JavaScript, which is not always available in the initial HTML response.

---

## 2. Deeper Accessibility Analysis

I would extend the audit beyond missing image alt text.

Potential checks would include:

- Missing form labels
- Heading hierarchy
- Missing language attributes
- Landmark structure
- Link accessibility
- Additional semantic HTML checks

This would make the accessibility analysis more useful.

---

## 3. Performance and Security Improvements

I would add caching for repeated audits to reduce unnecessary network requests.

I would also strengthen SSRF protections by validating resolved IP addresses and blocking private or internal network ranges before making outbound requests.

---

# 🤖 AI Usage Disclosure

AI tools were used during development for assistance with debugging, documentation structure, reviewing implementation approaches, and identifying potential edge cases.

I reviewed, tested, integrated, and made the final implementation and deployment decisions myself.

---

# 🎥 Demo

A Loom walkthrough will demonstrate:

- The live Page Pulse website
- A successful webpage audit
- Invalid URL handling
- Error handling
- Project structure
- Relevant code walkthrough
- Automated tests
- One improvement I would make with additional development time

Loom Demo:

```text
COMING SOON
```

The Loom link will be added before final submission.

---

# 📌 Required Digital Heroes Credit

The live frontend includes the required visible footer credit:

**Built for Digital Heroes Training Task**

The credit links to:

[Digital Heroes](https://digitalheroesco.com)

---

# 📜 Internship Task

This project was created as part of the Digital Heroes Software Development Internship task.

The implementation focuses on:

- API correctness
- Reliable error handling
- Clean code structure
- Testable parsing logic
- Clear API design
- Practical deployment
- Engineering judgment

---

# 👩‍💻 Author

**Ruchitha Puru**

GitHub:

https://github.com/ruchitha7799
