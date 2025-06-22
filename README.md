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

- X-Frame-Options : SAMEORIGIN
- X-Content-Type-Options : nosniff

Running Header Security Checks:

- [+] X-XSS-Protection : pass
- [+] X-Content-Type-Options : pass
- [+] X-Frame-Options : pass
- [-] Strict-Transport-Security header not present : fail!
- [-] Content-Security-Policy header not present : fail!

 Set-Cookie Checks:
- sessionid=123456
- [+] Secure : pass
- [+] HttpOnly : pass



2. 🔐 Password Cracker (Brute-Force using Wordlist)

This Python script attempts to recover plaintext passwords by "brute-forcing" them using a "wordlist" and comparing the hashes.
It supports various hashing algorithms and is useful for educational purposes, security testing, and understanding password vulnerabilities.


🚀 Features

- Supports common hashing algorithms (`sha256`, `md5`, `sha1`, etc.)
- Reads and checks each word from a wordlist file
- Gracefully handles errors like missing files or unsupported algorithms
- Reports success with line number and password if found
- Displays progress every 1000 attempts (can be modified)

🧰 Requirements

- Python 3.x
- No third-party packages required (uses Python's standard library)

⚙️ Usage

``bash
python password_cracker.py <target_hash> <wordlist_path> [hash_algorithm]


🔸 Arguments

| Argument           | Description                                |
| ------------------ | ------------------------------------------ |
| `<target_hash>`    | The hashed password you want to crack      |
| `<wordlist_path>`  | Path to a `.txt` file containing passwords |
| `[hash_algorithm]` | Optional. Default is `sha256`              |

🧪 Example
python password_cracker.py 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd  wordlist.txt sha256

✅ Sample Output
- [INFO] Using wordlist: wordlist.txt
- [INFO] Target hash: 5e88489...
- [INFO] Hash algorithm: sha256
= [INFO] Starting brute-force attack...

- [INFO] Checked 1000 passwords so far...
- [INFO] Checked 2000 passwords so far...

- [SUCCESS] Password found: 'password123' (Line 2035)
