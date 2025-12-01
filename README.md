# Password Strength Analyzer (Python)

This project is a simple yet effective **Password Strength Analyzer** written in Python.  
It evaluates how strong a password is by checking its length, character diversity, dictionary weaknesses, and entropy (mathematical randomness).

---

## Features

- ✔ **Length-based scoring**
- ✔ **Uppercase, lowercase, digit & special character detection**
- ✔ **Weak/dictionary password detection**
- ✔ **Entropy calculation (in bits)**
- ✔ **Final categorized output: WEAK / MODERATE / STRONG**

---

## How It Works

The analyzer checks the password on the basis of:

### 1️ **Length Score**
- 8+ characters → +1
- 12+ characters → +1

### 2 **Character Diversity**
- Uppercase letters  
- Lowercase letters  
- Numbers  
- Special characters  
(each gives additional score)

### 3️ **Dictionary Weakness**
If the password contains common weak words like:
