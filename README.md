1. HTTP Header Analysis
This project is a Python script that performs a basic security analysis of HTTP response headers for a given URL. 
It checks for the presence and correct configuration of several essential HTTP security headers to help improve the security posture of web applications.


🔍 Features

✅ Scans target URLs for important HTTP response headers.

🔒 Highlights missing or improperly configured headers that can expose your web application to attacks.
- Checks for the following security headers:
  - `X-XSS-Protection`
  - `X-Content-Type-Options`
  - `X-Frame-Options`
  - `Strict-Transport-Security`
  - `Content-Security-Policy`

🍪 Analyzes cookie attributes like Secure and HttpOnly.

📦 Requirements

- Python 3.x
- `requests` library

Install the required package using pip:

``'bash
pip install requests
 
🚀 Usage
i. Open the script HTTP Header Analysis.py.

ii. Modify the URL inside the main block to the desired target:


url = "http://localhost:8000/setup.php"

iii. Run the script:
python "HTTP Header Analysis.py"

🖥️ Sample Output


Response Headers:

X-Frame-Options : SAMEORIGIN
X-Content-Type-Options : nosniff

Running Header Security Checks:

[+] X-XSS-Protection : pass
[+] X-Content-Type-Options : pass
[+] X-Frame-Options : pass
[-] Strict-Transport-Security header not present : fail!
[-] Content-Security-Policy header not present : fail!

Set-Cookie Checks:
- sessionid=123456
[+] Secure : pass
[+] HttpOnly : pass


