import string
import re

def check_password_strength(password):
    score = 0
    feedback = []

    length = len(password)
    
    # Length-based scoring
    if length >= 12:
        score += 2
        feedback.append("✅ Good length (12+ characters)")
    elif length >= 8:
        score += 1
        feedback.append("⚠️ Decent length (8–11 characters)")
    else:
        feedback.append("❌ Too short")

    # Character variety
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Missing lowercase letters")

    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Missing uppercase letters")

    if re.search(r"\d", password):
        score += 1
        feedback.append("✅ Contains digits")
    else:
        feedback.append("❌ Missing digits")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Missing special characters")

    # Check for common patterns
    common_patterns = ["password", "1234", "admin", "qwerty", "letmein"]
    if any(pat in password.lower() for pat in common_patterns):
        score -= 2
        feedback.append("🚫 Contains common pattern — easily guessable")

    # Final verdict
    print("🔍 Password Analysis:")
    for msg in feedback:
        print("•", msg)

    print("\n🔐 Strength Score:", score, "/ 6")
    if score >= 5:
        print("🟢 Strong password")
    elif score >= 3:
        print("🟡 Moderate password")
    else:
        print("🔴 Weak password")

# Example usage:
user_password = input("Enter your password to check strength: ")
check_password_strength(user_password)
