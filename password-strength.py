import re
import random
import string
import streamlit as st

# Common weak passwords list
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password123", "letmein", "welcome"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check if password is too common
    if password.lower() in COMMON_PASSWORDS:
        return 0, ["❌ This password is **too common!** Choose a more secure one."]

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔴 Password should be at least **8 characters long**.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("🟡 Include **both uppercase and lowercase letters**.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🟡 Add at least **one number (0-9).**")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("🟡 Include **at least one special character** (!@#$%^&*).")

    return score, feedback

# Function to generate a strong password
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("🔑 Enter your password:", type="password")

if password:
    score, feedback = check_password_strength(password)

    # Assign strength level based on score
    strength_levels = ["🔴 Weak", "🟡 Moderate", "🟢 Strong"]
    strength = strength_levels[min(score, 2)]

    # Display strength result with emojis
    st.markdown(f"### Password Strength: **{strength}**")

    # Strength Progress Bar
    st.progress(score / 4)

    # Show feedback if password is weak or moderate
    if strength in ["🔴 Weak", "🟡 Moderate"]:
        st.markdown("### 📢 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"- {tip}")

# Password Generator Button
if st.button("🔄 Generate Strong Password"):
    strong_password = generate_strong_password()
    st.text(f"💡 Suggested Password: {strong_password}")
