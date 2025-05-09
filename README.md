# StochMarket

This project simulates various aspects of a financial market using stochastic processes. The system includes **Markov Models**, **Hidden Markov Models (HMM)**, and **Queuing Theory (M/M/1)** to model order state transitions, hidden market conditions, and order processing respectively. It allows users to interact with financial data and compute key metrics.

## Features

- **Stock Data Input**: Fetches real-time historical stock data using **yFinance** API.
- **Market Condition Labeling**: Classifies market conditions based on historical stock returns (Bullish, Bearish, Consolidation).
- **Order State Simulation**: Simulates order state transitions in a market using a **Markov Chain**.
- **Hidden Markov Model**: Infers hidden market conditions based on observed stock returns using **Forward** and **Viterbi Algorithms**.
- **Queuing Theory (M/M/1)**: Models the order processing system and computes key metrics such as **waiting time**, **queue length**, and **system utilization**.

## Models

### 1. **Markov Chain - Order States**

Simulates the transition of orders through states:
- **Placed**: The order is placed but not yet executed.
- **Executed**: The order is executed (absorbing state).
- **Pending**: The order is still pending.
- **Cancelled**: The order is cancelled (absorbing state).

We calculate:
- **Steady-State Probabilities**
- **Recurrence Time**
- **Passage Time**

### 2. **Hidden Markov Models (HMM) - Market Conditions**

Classifies market conditions (Bullish, Bearish, Consolidation) based on observed stock returns (up, down, flat). 
- **Forward Algorithm** computes the probability of the observation sequence.
- **Viterbi Algorithm** determines the most likely sequence of hidden states.

### 3. **Queuing Theory (M/M/1) - Order Processing**

Models the trade order processing system using the **M/M/1 Queuing Model**:
- **Poisson arrivals** (orders placed).
- **Exponential service times** (order execution).
- **Single server** (one exchange handling orders).

Key metrics computed:
- **Utilization (ρ)**
- **Average number of orders in the system (L)**
- **Average waiting time (Wq)**
- **Average time in the system (W)**

## Installation

To set up the project locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/whis-19/StochMarket.git
   ```

2. Navigate into the project folder:
   ```bash
   cd StochMarket
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Deployment

This project is deployed on **Streamlit Cloud**. You can access the deployed application via the following link:

https://whis-19-stochmarket-app-w3dgsi.streamlit.app

## Project Structure

```
/finance_market_model/
│
├── app.py               # Main Streamlit app
├── markov_model.py      # Order state simulation + analysis
├── hmm_model.py         # Hidden Markov Model logic
├── queue_model.py       # M/M/1 Queue metrics
└── utils.py             # Shared utilities (e.g., data fetching)
└── plot.py             # To visualise the model
```

## Acknowledgments

- **yFinance** for fetching stock data.
- **Streamlit** for the interactive app.
- **Python** and related libraries for implementing the models and algorithms.
