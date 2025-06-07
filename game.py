# A web-based interactive version using Streamlit. Click a button to simulate 3 games.

# Requirements: streamlit (install via pip install streamlit)
# Run with: python3 -m streamlit run game.py


import streamlit as st
import random

st.title("Rubinstein Bargaining Game Simulation")

if st.button("Run Simulation"):
    ROUND1_PIE = 100
    ROUND2_PIE = 90
    threshold_A = random.randint(10, 30)
    threshold_B = random.randint(10, 30)

    offer_to_A = random.randint(1, 99)
    offer_to_B = ROUND1_PIE - offer_to_A

    st.subheader("Round 1")
    st.write(f"Player A offers: A = ${offer_to_A}, B = ${offer_to_B}")
    st.write(f"Player B's acceptance threshold: ${threshold_B}")

    if offer_to_B >= threshold_B:
        st.success(f"Player B accepts. Final Payoffs: A = ${offer_to_A}, B = ${offer_to_B}")
    else:
        st.warning("Player B rejects the offer.")

        offer_to_B = random.randint(1, 89)
        offer_to_A = ROUND2_PIE - offer_to_B

        st.subheader("Round 2")
        st.write(f"Player B offers: B = ${offer_to_B}, A = ${offer_to_A}")
        st.write(f"Player A's acceptance threshold: ${threshold_A}")

        if offer_to_A >= threshold_A:
            st.success(f"Player A accepts. Final Payoffs: A = ${offer_to_A}, B = ${offer_to_B}")
        else:
            st.error("Player A rejects. No agreement. Both get $0.")
