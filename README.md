# 🔒 Cybersecurity Python Projects 🚀

This collection contains ** 3 simple scripts ** for educational and security testing purposes. Each script focuses on a specific area in cybersecurity — from web security scanning to password strength and brute-force testing.


---

## 1️⃣ Password Strength Checker

**Description:**  
Evaluates password strength using length and complexity.

### 🚀 Features
- Checks:
  - Minimum 8 characters
  - Lowercase
  - Uppercase
  - Numbers
  - Special characters (@$!%*?&)
- Score out of 5 with suggestions.

### 🧰 Requirements
- Python 3.x  

### ⚙️ Usage
```bash
python PASSWORD_CHECKER.py
```

### 🧪 Example
```
Enter password: Welcome123
Strength Score: 4/5
Suggestions: Add at least one special character.
```



## 2️⃣🔐 Password List Generator
**Description:**  
This project is a simple Python script designed to generate a large list of random lowercase passwords. It is useful for testing password cracking tools, brute-force simulations, or other cybersecurity-related experiments.

---

### 📜 Features

- ✅ Generates **1 million** random passwords  
- ✅ Each password:
  - Is **8 characters** long  
  - Consists of **lowercase letters only** (`a-z`)  
- ✅ Outputs the list to a file named `password.lst`

---

### 🧰 Requirements

- Python **3.x**  
- No external libraries needed (uses built-in `random` and `string` modules)

---

### 🏃‍♂️ Usage

1. Clone or download this project.
2. Run the script using Python:

   ```bash
   python PASSWORD\ LIST\ GENERATOR.py
   ```

3. A file named `password.lst` will be created in the same directory containing **1 million** randomly generated passwords.

---

### 📁 Output Example

Each line in `password.lst` contains one 8-character password. Example:

```
qweorplk
zmxnvcas
asldkfjg
...
```


 ## 3️⃣ 🔐 Encryption & Decryption Toolkit

This project provides simple command-line tools for **text encryption and decryption** using three classic cipher techniques:  

- **Caesar Cipher**  
- **XOR Cipher**  
- **Vigenère Cipher**  

The toolkit is split into two scripts:  

- `ENCRYPTION_TOOL.py` → Encrypts plaintext into ciphertext.  
- `DECRYPTION_TOOL.py` → Decrypts ciphertext back into plaintext.  

---

### 🚀 Features

- Interactive command-line interface.  
- Supports **three different cipher algorithms**.  
- Input validation (keys must match expected format).  
- Works with uppercase and lowercase letters.  
- Lightweight — no external dependencies required.  

---

### 📂 Project Structure

```
📁 Encryption-Decryption-Toolkit
 ├── ENCRYPTION_TOOL.py   # Encrypts text
 ├── DECRYPTION_TOOL.py   # Decrypts text
 └── README.md            # Project documentation
```

---

### ⚙️ Installation

1. Clone or download the project folder.  
2. Ensure you have **Python 3.x** installed on your system.  
3. Run the scripts directly with Python:

```bash
python ENCRYPTION_TOOL.py
python DECRYPTION_TOOL.py
```

---

### 🛠️ Usage

### 1. Encryption
Run the encryption tool:

```bash
python ENCRYPTION_TOOL.py
```

Steps:
1. Choose a cipher method:  
   - `1` → Caesar Cipher  
   - `2` → XOR Cipher  
   - `3` → Vigenère Cipher  
2. Enter the text you want to encrypt.  
3. Provide the encryption key depending on the cipher.  
4. The encrypted text is displayed.  

---

### 2. Decryption
Run the decryption tool:

```bash
python DECRYPTION_TOOL.py
```

Steps:
1. Choose the cipher method used during encryption.  
2. Enter the encrypted text.  
3. Provide the decryption key (must match the encryption key).  
4. The decrypted text is displayed.  

---

## 🔑 Cipher Details

### Caesar Cipher
- Shifts each letter by a numeric key.  
- Example: `"HELLO"` with key `3` → `"KHOOR"`.  

### XOR Cipher
- Applies bitwise XOR with a numeric key (`1–255`).  
- Symmetric: encryption and decryption use the same operation.  

### Vigenère Cipher
- Uses a keyword of letters to determine shifting for each character.  
- Example: Text `"HELLO"`, Key `"KEY"` → `"RIJVS"`.  

---

## 📌 Example Workflow

**Encryption (Caesar Cipher):**
```
=== ENCRYPTION TOOL ===
Choose a cipher method:
1. Caesar Cipher
2. XOR Cipher
3. Vigenère Cipher

Enter your choice (1-3): 1
Enter the text to encrypt: HELLO
Enter the shift key (number): 3

Original text: HELLO
Caesar key: 3
Encrypted text: KHOOR
```

**Decryption (Caesar Cipher):**
```
=== DECRYPTION TOOL ===
Choose the cipher method used for encryption:
1. Caesar Cipher
2. XOR Cipher
3. Vigenère Cipher

Enter your choice (1-3): 1
Enter the encrypted text: KHOOR
Enter the shift key used for encryption: 3

Encrypted text: KHOOR
Caesar key: 3
Decrypted text: HELLO
```

---





---
