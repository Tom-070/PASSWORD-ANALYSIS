import math
import re

weak_words = ["password", "admin", "qwerty", "letmein", "welcome"]

def check_strength(password):
    score = 0
    length = len(password)

    # Length score
    if length >= 8: score += 1
    if length >= 12: score += 1

    # Character diversity
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'\d', password): score += 1
    if re.search(r'[@$!%*?&]', password): score += 1

    # Dictionary weakness
    for word in weak_words:
        if word in password.lower():
            score -= 2

    # Entropy calculation
    charset = 0
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'\d', password): charset += 10
    if re.search(r'[@$!%*?&]', password): charset += 10

    entropy = length * math.log2(charset)

    return score, entropy

password = input("Enter Password to Test: ")

score, entropy = check_strength(password)

print("\nPassword Strength Score:", score)
print("Entropy:", round(entropy, 2), "bits")

if score <= 2:
    print("Strength: WEAK Password")
elif score == 3 or score == 4:
    print("Strength: MODERATE Password")
else:
    print("Strength: STRONG Password")

