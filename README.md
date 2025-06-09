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

🔐 Password Cracker

A simple brute-force password cracker written in Python. It attempts to crack a given hash by comparing it against a list of potential passwords (wordlist) using a specified hashing algorithm.

 🚀 Features

- Supports multiple hash algorithms (`sha256`, `md5`, `sha1`, etc.)
- Reads from a customizable wordlist file
- Displays progress every 1000 attempts
- Fast and lightweight command-line tool

 🧠 How It Works

The script takes in a hash, reads a wordlist line by line, hashes each word using the chosen algorithm, and compares it to the target hash. If a match is found, the password is revealed.

 📦 Requirements

- Python 3.x

No external libraries required — only built-in modules (`hashlib`, `os`, `sys`).

 🛠️ Usage

```bash
python PASSWORD\ CRACKER.py <target_hash> <wordlist_path> [hash_algorithm]


