# Rubinstein Bargaining Game Simulation (Streamlit)

A simple Streamlit app simulating a two-player Rubinstein-style bargaining game with discounting.

### Description

- Player A and Player B negotiate over a $100 pie
- If no agreement in Round 1, pie is discounted to $90 in Round 2
- Offers are randomly generated
- Acceptance depends on randomly chosen thresholds for each player

### How to Run

Install requirements:

```bash
pip install streamlit

streamlit run bargaining_simulation_streamlit.py
