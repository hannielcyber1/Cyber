python
import hashlib
import sys
import os

def hash_password(password, algorithm='sha256'):
    """Hash the password using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    hash_func.update(password.encode('utf-8'))
    return hash_func.hexdigest()

def brute_force_password(target_hash, wordlist_path, algorithm='sha256'):
    """Attempts to find the password by hashing each word in the wordlist."""
    if not os.path.isfile(wordlist_path):
        print(f"[ERROR] Wordlist file not found: {wordlist_path}")
        sys.exit(1)

    print(f"Using wordlist: {wordlist_path}")
    print(f"Target hash: {target_hash}")
    print(f"Hash algorithm: {algorithm}")
    print("Starting brute-force attack...\n")

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line_number, word in enumerate(f, start=1):
            word = word.strip()
            hashed = hash_password(word, algorithm)
            if hashed == target_hash:
                print(f"[SUCCESS] Password found: '{word}' (Line {line_number} in wordlist)")
                return word

            # Optional: show progress every 1000 attempts (comment out if noisy)
            if line_number % 1000 == 0:
                print(f"Checked {line_number} passwords so far...")

    print("[FAILURE] Password not found in wordlist.")
    return None

def main():
    if len(sys.argv) not in [3, 4]:
        print("Usage: python brute_force.py <target_hash> <wordlist_path> [hash_algorithm]")
        print("Example: python brute_force.py e3b0c44298fc1c149afbf4c8996fb924... wordlist.txt sha256")
        sys.exit(1)

    target_hash = sys.argv[1]
    wordlist_path = sys.argv[2]
    algorithm = sys.argv[3] if len(sys.argv) == 4 else 'sha256'

    supported_algorithms = hashlib.algorithms_guaranteed
    if algorithm.lower() not in supported_algorithms:
        print(f"[ERROR] Unsupported hash algorithm: {algorithm}")
        print(f"Supported algorithms: {', '.join(sorted(supported_algorithms))}")
        sys.exit(1)

    brute_force_password(target_hash, wordlist_path, algorithm.lower())

if __name__ == "__main__":
    main()
