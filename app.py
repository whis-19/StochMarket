import streamlit as st
from utils import fetch_stock_data, label_market_condition
from markov_model import simulate_order_states, compute_steady_state
from hmm_model import forward, viterbi
from queue_model import mm1_metrics

# Define HMM parameters
hidden_states = ['Bullish', 'Bearish', 'Consolidation']
observations = ['Up', 'Down', 'Flat']
obs_map = {'Up': 0, 'Down': 1, 'Flat': 2}

# Initial state probabilities (pi)
pi = [0.4, 0.3, 0.3]  # P(Bullish), P(Bearish), P(Consolidation)

# Transition matrix A (3x3)
A = [
    [0.6, 0.2, 0.2],  # Bullish transitions
    [0.3, 0.5, 0.2],  # Bearish transitions
    [0.3, 0.3, 0.4]   # Consolidation transitions
]

# Emission matrix B (3x3) - P(observation | state)
B = [
    [0.7, 0.1, 0.2],  # Bullish: Up, Down, Flat
    [0.1, 0.7, 0.2],  # Bearish
    [0.2, 0.2, 0.6]   # Consolidation
]

# Streamlit Layout for Interaction
st.title("Finance Market Modeling using Stochastic Processes")

# Fetch stock data
ticker = st.text_input('Enter Stock Ticker', 'AAPL')
data = fetch_stock_data(ticker)
data = label_market_condition(data)

# Display stock data and market conditions
st.subheader('Stock Data and Market Conditions')
st.write(data[['Close', 'Returns', 'Market_Condition']].head())

# Simulate Order State Transitions
order_states_sequence = simulate_order_states()
st.subheader("Order State Transitions (Markov Model)")
st.write(order_states_sequence)

# Compute Steady-State Probabilities for the Markov Chain
steady_state_probs = compute_steady_state({
    'Placed': {'Placed': 0.1, 'Executed': 0.6, 'Pending': 0.2, 'Cancelled': 0.1},
    'Executed': {'Executed': 1.0, 'Placed': 0.0, 'Pending': 0.0, 'Cancelled': 0.0},
    'Pending': {'Placed': 0.2, 'Executed': 0.4, 'Pending': 0.3, 'Cancelled': 0.1},
    'Cancelled': {'Cancelled': 1.0, 'Placed': 0.0, 'Executed': 0.0, 'Pending': 0.0}
})
st.subheader("Steady-State Probabilities (Order State)")
st.write(steady_state_probs)

# HMM - Forward Algorithm
obs_seq = ['Up', 'Down', 'Flat', 'Up', 'Up']  # Example sequence of observations
prob, alpha = forward(obs_seq, pi, A, B)
st.subheader("Forward Algorithm - Observation Probability")
st.write(f"Probability of observing the sequence: {prob:.4f}")

# HMM - Viterbi Algorithm
state_seq, delta = viterbi(obs_seq, pi, A, B)
st.subheader("Viterbi Algorithm - Most Likely Hidden States")
st.write(state_seq)

# M/M/1 Queue Metrics
arrival_rate = st.slider('Arrival Rate (orders/min)', 1, 10, 3)
service_rate = st.slider('Service Rate (orders/min)', 1, 10, 5)

if arrival_rate >= service_rate:
    st.error("Error: System is unstable (λ >= μ). Choose λ < μ.")
else:
    queue_metrics = mm1_metrics(arrival_rate, service_rate)
    st.subheader("M/M/1 Queue Metrics (Order Processing)")
    st.write(queue_metrics)
