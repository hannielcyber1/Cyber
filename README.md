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
if __name__ == "__main__":
    target = ScanHeaders("http://your-target-url.com")

iii. Run the script:
python "HTTP Header Analysis.py"

🖥️ Sample Output
X-XSS-Protection : 1; mode=block
X-Content-Type-Options : nosniff
X-Frame-Options : SAMEORIGIN
Strict-Transport-Security : max-age=31536000; includeSubDomains
Content-Security-Policy : default-src 'self'

[+] X-XSS-Protection : pass
[+] X-Content-Type-Options : pass
[+] X-Frame-Options : pass
[+] Strict-Transport-Security : pass
[+] Content-Security-Policy : pass

Set-Cookie:
[+] Secure : pass
[+] HttpOnly : pass



