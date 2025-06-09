python
import requests

class ScanHeaders:
    def __init__(self, url):
        self.url = url
        response = requests.get(self.url)
        self.headers = response.headers
        self.cookies = response.cookies

    def scan_xxss(self):
        """Check if X-XSS-Protection header is present."""
        if "X-XSS-Protection" in self.headers:
            print("[+]", "X-XSS-Protection", ':', "pass")
        else:
            print("[-]", "X-XSS-Protection header not present", ':', "fail!")

    def scan_nosniff(self):
        """Check if X-Content-Type-Options is set to 'nosniff'."""
        if self.headers.get("X-Content-Type-Options", "").lower() == "nosniff":
            print("[+]", "X-Content-Type-Options", ':', "pass")
        else:
            print("[-]", "X-Content-Type-Options header not set correctly", ':', "fail!")

    def scan_xframe(self):
        """Check if X-Frame-Options is set to DENY or SAMEORIGIN."""
        if "X-Frame-Options" in self.headers:
            if "deny" in self.headers["X-Frame-Options"].lower() or "sameorigin" in self.headers["X-Frame-Options"].lower():
                print("[+]", "X-Frame-Options", ':', "pass")
            else:
                print("[-]", "X-Frame-Options header not set correctly", ':', "fail!")
        else:
            print("[-]", "X-Frame-Options header not present", ':', "fail!")

    def scan_hsts(self):
        """Check if Strict-Transport-Security header is present."""
        if "Strict-Transport-Security" in self.headers:
            print("[+]", "Strict-Transport-Security", ':', "pass")
        else:
            print("[-]", "Strict-Transport-Security header not present", ':', "fail!")

    def scan_policy(self):
        """Check if Content-Security-Policy header is present."""
        if "Content-Security-Policy" in self.headers:
            print("[+]", "Content-Security-Policy", ':', "pass")
        else:
            print("[-]", "Content-Security-Policy header not present", ':', "fail!")

    def scan_secure(self, cookie):
        """Check if Set-Cookie header has the secure attribute set."""
        if cookie.secure:
            print("[+]", "Secure", ':', "pass")
        else:
            print("[-]", "Secure attribute not set", ':', "fail!")

    def scan_httponly(self, cookie):
        """Check if Set-Cookie header has the HttpOnly attribute set."""
        if cookie.has_nonstandard_attr('httponly') or cookie.has_nonstandard_attr('HttpOnly'):
            print("[+]", "HttpOnly", ':', "pass")
        else:
            print("[-]", "HttpOnly attribute not set", ':', "fail!")

if __name__ == "__main__":
    target = ScanHeaders("http://localhost:8000/setup.php")

    for key in target.headers:
        print(key, ":", target.headers[key])

    print()

    target.scan_xxss()
    target.scan_nosniff()
    target.scan_xframe()
    target.scan_hsts()
    target.scan_policy()

    for cookie in target.cookies:
        print("Set-Cookie:")
        target.scan_secure(cookie)
        target.scan_httponly(cookie)
