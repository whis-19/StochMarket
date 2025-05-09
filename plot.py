# plot.py
import matplotlib.pyplot as plt

def plot_stock_data(data):
    """Line chart of Close price."""
    fig = plt.figure()
    plt.plot(data.index, data['Close'])
    plt.title("Stock Close Price")
    plt.xlabel("Date")
    plt.ylabel("Close")
    plt.tight_layout()
    return fig

def plot_order_state_sequence(seq):
    """Bar chart of counts per state in the simulated sequence."""
    fig = plt.figure()
    counts = {s: seq.count(s) for s in set(seq)}
    plt.bar(counts.keys(), counts.values())
    plt.title("Order State Frequencies")
    plt.xlabel("State")
    plt.ylabel("Count")
    plt.tight_layout()
    return fig

def plot_steady_state_probs(steady_probs):
    """Pie chart of steady-state probabilities."""
    fig = plt.figure()
    labels, sizes = zip(*steady_probs.items())
    plt.pie(sizes, labels=labels, autopct='%.2f%%')
    plt.title("Steady-State Probabilities")
    plt.tight_layout()
    return fig

def plot_hmm_alpha(alpha):
    """Line plots of alpha values over time for each hidden state."""
    fig = plt.figure()
    for idx, state_vals in enumerate(zip(*alpha)):
        plt.plot(range(len(alpha)), state_vals, label=f"State {idx}")
    plt.title("Forward Algorithm α-values")
    plt.xlabel("Time step")
    plt.ylabel("α")
    plt.legend()
    plt.tight_layout()
    return fig

def plot_queue_metrics(metrics):
    """Bar chart of the M/M/1 queue metrics."""
    fig = plt.figure()
    plt.bar(metrics.keys(), metrics.values())
    plt.title("M/M/1 Queue Metrics")
    plt.ylabel("Value")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    return fig
