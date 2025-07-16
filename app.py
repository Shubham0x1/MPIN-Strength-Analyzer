import streamlit as st
from mpin_strength_analyzer_shubham_gusain import check_strength_reason
st.set_page_config(page_title="MPIN Strength Checker", layout="centered")
st.markdown("""
    <style>
        .stApp {
            background-color: #ffe0e6;
        }

        /* Bolder input labels */
        label, .stTextInput > label {
            font-weight: 700;
            color: #222222;
        }

        h1, h2, h3 {
            color: #222222;
        }
    </style>
""", unsafe_allow_html=True)
st.title("🔐 MPIN Strength Analyzer")
st.markdown("Check whether your MPIN is secure or weak based on common patterns and demographics.")
pin = st.text_input("Enter your MPIN (4 or 6 digits)", max_chars=6)
dob = st.text_input("Enter your Date of Birth (DD-MM-YYYY)", placeholder="e.g., 02-01-1998")
spouse_dob = st.text_input("Spouse's DOB (optional)", placeholder="e.g., 10-12-1990")
anniversary = st.text_input("Wedding Anniversary (optional)", placeholder="e.g., 15-08-2015")
if st.button("Check Strength"):
    if not pin.strip():
        st.warning("⚠️ Please enter your MPIN.")
    else:
        strength, reasons = check_strength_reason(
            pin.strip(), 
            dob.strip() or None, 
            spouse_dob.strip() or None, 
            anniversary.strip() or None
        )
        
        st.subheader(f"Result: {strength}")
        
        if strength == "INVALID_LENGTH":
            st.error("❌ MPIN must be either 4 or 6 digits.")
        elif strength == "STRONG":
            st.success("✅ Your MPIN is strong and not easily guessable.")
        elif strength == "WEAK":
            st.error("⚠️ Your MPIN is weak.")
            st.write("**Reasons:**")
            for reason in reasons:
                st.markdown(f"- `{reason}`")
