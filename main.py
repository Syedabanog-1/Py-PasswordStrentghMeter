import streamlit as st
import re

def check_password_strength(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Za-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[@$!%*#?&]", password):
        return False
    return True

st.set_page_config(page_title="Password Strength Meter", layout="centered")
st.title("🔒 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    if check_password_strength(password):
        st.success("Yes Strong Password Created Successfully.", icon="✅")
    else:
        st.error("Invalid Password! Please Try Again.", icon="❌")
