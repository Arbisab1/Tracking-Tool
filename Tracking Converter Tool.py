import streamlit as st
import random

st.title("Tracking Converter Tool")

# Input field
orig_tracking = st.text_input("Original Tracking / Order ID:")

# Carrier selection
carrier = st.selectbox("Select Carrier Format:", ["UPS", "FedEx", "USPS"])

if st.button("Convert / Generate"):
    if orig_tracking:
        if carrier == "UPS":
            generated = "1Z" + "".join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=16))
        elif carrier == "FedEx":
            generated = "".join(random.choices("0123456789", k=12))
        else:
            generated = "".join(random.choices("0123456789", k=22))
            
        st.success("Tracking generated successfully!")
        st.write(f"**Generated Tracking:** {generated}")
        st.write(f"**Carrier:** {carrier}")
        st.write("**Status:** In Transit (Simulated)")
    else:
        st.error("Please enter an original tracking or order ID first.")
