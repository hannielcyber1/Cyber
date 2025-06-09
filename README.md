 Web Security Testing Toolkit 🛡️

This repository contains a collection of simple yet effective Python tools for analyzing and testing web applications for common vulnerabilities:

- ✅ HTTP Header Security Analysis
- 🧪 XSS (Cross-Site Scripting) Detection
- 🕵️ SQL Injection Detection

Each tool is standalone, command-line-based, and written in Python.

---

 🔍 Projects Overview

 1. HTTP Header Analysis

File: `HTTP Header Analysis.py`

Checks the security posture of a website by scanning for important HTTP response headers.

Features:
- Detects presence and correctness of:
  - `X-XSS-Protection`
  - `X-Content-Type-Options`
  - `X-Frame-Options`
  - `Strict-Transport-Security`
  - `Content-Security-Policy`
- Scans cookies for `Secure` and `HttpOnly` attributes.

Usage:
```bash
python "HTTP Header Analysis.py"

