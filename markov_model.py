import random

# Define the order states
order_states = ['Placed', 'Executed', 'Pending', 'Cancelled']

# Transition probability matrix (manually set for now)
transition_matrix = {
    'Placed': {'Placed': 0.1, 'Executed': 0.6, 'Pending': 0.2, 'Cancelled': 0.1},
    'Executed': {'Executed': 1.0, 'Placed': 0.0, 'Pending': 0.0, 'Cancelled': 0.0},  # Absorbing state
    'Pending': {'Placed': 0.2, 'Executed': 0.4, 'Pending': 0.3, 'Cancelled': 0.1},
    'Cancelled': {'Cancelled': 1.0, 'Placed': 0.0, 'Executed': 0.0, 'Pending': 0.0},  # Absorbing state
}

def simulate_order_states(initial_state='Placed', steps=50):
    current_state = initial_state
    state_sequence = [current_state]   
    for _ in range(steps - 1):
        next_states = list(transition_matrix[current_state].keys())
        probs = list(transition_matrix[current_state].values())
        current_state = random.choices(next_states, probs)[0]
        state_sequence.append(current_state)
    
    return state_sequence

def compute_steady_state(transition_matrix, tolerance=1e-6, max_iterations=1000):
    # List of states
    states = list(transition_matrix.keys())
    num_states = len(states)
    # Initialize the steady state probabilities (uniform distribution)
    pi = [1.0 / num_states] * num_states
    # Iteratively calculate steady state probabilities
    for iteration in range(max_iterations):
        new_pi = [0] * num_states
        for i in range(num_states):
            # Sum up the contributions from each state using indices
            new_pi[i] = sum(pi[j] * transition_matrix[states[j]].get(states[i], 0) for j in range(num_states))    
        # Check for convergence (if change is smaller than tolerance)
        if all(abs(new_pi[i] - pi[i]) < tolerance for i in range(num_states)):
            break   
        pi = new_pi
    # Normalize the probabilities to sum to 1 (in case of any numerical issues)
    total = sum(pi)
    pi = [x / total for x in pi]
    # Return the result as a dictionary
    return dict(zip(states, pi))
