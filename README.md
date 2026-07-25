# Page Pulse 🚀

A web-based webpage auditing tool that analyzes any public URL and provides insights about performance, content structure, SEO, and accessibility.

Page Pulse fetches a webpage, analyzes its HTML content, and generates a structured report containing important page metrics.

## 🌐 Live Demo

Frontend:
https://page-pulse-frontend-wb3y.onrender.com

Backend API:
https://page-pulse-wbkb.onrender.com

---

# ✨ Features

## Web Auditing

Page Pulse analyzes:

- HTTP response status
- Response time
- Page title
- Meta description
- H1 heading count
- Images missing alternative text
- Approximate word count


## Error Handling

The application handles:

- Invalid URLs
- Connection failures
- Timeout errors
- Non-HTML responses
- Server-side failures


## User Interface

The frontend provides:

- Simple URL input
- Loading state during analysis
- Clean audit report display
- Error messages for failed requests
- Responsive design


---

# 🏗️ Architecture

```
User
 |
 |
Frontend (HTML/CSS/JavaScript)
 |
 |
FastAPI REST API
 |
 |
Web Fetching Service
 |
 |
HTML Parser
 |
 |
Audit Report JSON
```

## Project Structure

```
Page-Pulse/

├── backend/
│
│   ├── app/
│   │
│   │   ├── routes/
│   │   │   └── audit.py
│   │   │
│   │   ├── services/
│   │   │   ├── fetcher.py
│   │   │   └── parser.py
│   │   │
│   │   ├── schemas/
│   │   │   └── audit.py
│   │   │
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
│
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# 🔌 API Documentation

## Audit URL

### Endpoint

```
POST /api/v1/audit
```

### Request

```json
{
  "url": "https://example.com"
}
```

### Successful Response

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

# ❌ Error Responses

## Invalid URL

```json
{
  "success": false,
  "error": {
    "code": "INVALID_URL",
    "message": "Please provide a valid HTTP or HTTPS URL."
  }
}
```

## Connection Failure

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

# ⚙️ Local Setup

## Backend Setup

Clone the repository:

```bash
git clone https://github.com/ruchitha7799/page-pulse.git
```

Navigate to backend:

```bash
cd Page-Pulse/backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

# Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Run:

```bash
python -m http.server 5500
```

Open:

```
http://127.0.0.1:5500
```

---

# 🧪 Testing

Run backend tests:

```bash
python -m pytest -v
```

Current test coverage includes:

- Successful HTML parsing
- Missing metadata handling
- Missing image alt attributes
- Successful audit request
- Invalid URLs
- Timeout handling
- Connection errors
- Non-HTML responses


---

# 💡 Design Decisions

## 1. Separation of Fetching and Parsing Logic

### Decision

The webpage fetching logic and HTML parsing logic are implemented as separate services.

### Reason

This improves maintainability and makes testing easier.

The parser can be tested independently without making real network requests.

---

## 2. Structured Error Responses

### Decision

All failures return consistent JSON error formats.

### Reason

A predictable API response makes frontend handling easier and improves developer experience.

---

## 3. Client-Server Separation

### Decision

The frontend and backend are deployed independently.

### Reason

This allows independent scaling, easier maintenance, and follows modern web application architecture patterns.

---

# 🚀 Deployment

Frontend:

Render Static Site

Backend:

Render Web Service

The backend API is configured with CORS support to allow communication with the deployed frontend.

---

# 🤖 AI Usage Disclosure

AI tools were used during development for assistance with debugging, improving documentation structure, reviewing implementation approaches, and identifying possible edge cases.

All final implementation decisions, code integration, testing, and deployment configuration were reviewed and completed by me.

---

# 🔮 Future Improvements

If given additional development time, I would improve:

- Lighthouse-style performance scoring
- Accessibility score calculation
- Screenshot generation
- Historical audit tracking
- Authentication and user dashboards

---

# 📜 License

This project was created as part of the Digital Heroes Software Development Internship task.

Built for Digital Heroes Training Task.