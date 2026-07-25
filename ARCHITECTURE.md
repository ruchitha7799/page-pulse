# Page Pulse Architecture

## Overview

Page Pulse is a web-based URL auditing tool. The application accepts a webpage URL, fetches the target page, analyses its HTML content, and returns a structured audit report.

## Technology Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Pydantic
- HTTPX
- BeautifulSoup4

### Testing
- Pytest

## Request Flow

1. User enters a URL in the frontend.
2. Frontend sends the URL to the backend API.
3. Backend validates the URL.
4. Fetcher requests the target webpage.
5. Backend checks the response and content type.
6. Parser analyses the HTML.
7. Backend returns a structured JSON response.
8. Frontend displays the audit results.

## Backend Responsibilities

### API Route
Receives and validates audit requests.

### Fetcher
Handles webpage requests, timeouts, connection failures, and response metadata.

### Parser
Extracts page title, meta description, H1 count, missing image alt text, and approximate word count.

### Schemas
Defines the request and response data structures.

### Tests
Verify parsing logic and expected success and failure behaviour.

## Frontend Responsibilities

The frontend provides:
- URL input
- Audit action
- Loading state
- Results display
- Error display
- Responsive user interface

## High-Level Architecture

User
↓
Frontend
↓
FastAPI API
↓
URL Validation
↓
Fetcher
↓
Target Website
↓
HTML Parser
↓
JSON Report
↓
Frontend Results