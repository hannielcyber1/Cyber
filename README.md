 HTTP Header Analysis

A simple Python script that performs basic security analysis on HTTP response headers for a given URL. It checks for the presence and correct configuration of several essential HTTP security headers to help improve the security posture of web applications.

 🔍 Features

- Checks for the following security headers:
  - `X-XSS-Protection`
  - `X-Content-Type-Options`
  - `X-Frame-Options`
  - `Strict-Transport-Security`
  - `Content-Security-Policy`
- Analyzes `Set-Cookie` attributes for:
  - `Secure`
  - `HttpOnly`

📦 Requirements

- Python 3.x
- `requests` library

Install the required package using pip:

```bash
pip install requests
