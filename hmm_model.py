# Define the hidden states and observations
hidden_states = ['Bullish', 'Bearish', 'Consolidation']
observations = ['Up', 'Down', 'Flat']
obs_map = {'Up': 0, 'Down': 1, 'Flat': 2}

# Initial probabilities (pi), transition probabilities (A), and emission probabilities (B)
pi = [0.4, 0.3, 0.3]
A = [
    [0.6, 0.2, 0.2],
    [0.3, 0.5, 0.2],
    [0.3, 0.3, 0.4]
]
B = [
    [0.7, 0.1, 0.2],  # Bullish
    [0.1, 0.7, 0.2],  # Bearish
    [0.2, 0.2, 0.6]   # Consolidation
]

# Forward Algorithm: Calculates the probability of the observation sequence
def forward(obs_seq, pi, A, B):
    T = len(obs_seq)
    N = len(pi)
    alpha = [[0] * N for _ in range(T)]   
    # Initialization
    obs_idx = obs_map[obs_seq[0]]
    for j in range(N):
        alpha[0][j] = pi[j] * B[j][obs_idx]  
    # Recursion
    for t in range(1, T):
        obs_idx = obs_map[obs_seq[t]]
        for j in range(N):
            alpha[t][j] = sum(alpha[t - 1][i] * A[i][j] for i in range(N)) * B[j][obs_idx] 
    prob = sum(alpha[T - 1][j] for j in range(N))
    return prob, alpha

# Viterbi Algorithm: Finds the most likely sequence of hidden states
def viterbi(obs_seq, pi, A, B):
    T = len(obs_seq)
    N = len(pi)
    delta = [[0] * N for _ in range(T)]
    psi = [[0] * N for _ in range(T)]    
    # Initialization
    obs_idx = obs_map[obs_seq[0]]
    for j in range(N):
        delta[0][j] = pi[j] * B[j][obs_idx] 
    # Recursion
    for t in range(1, T):
        obs_idx = obs_map[obs_seq[t]]
        for j in range(N):
            max_val = max(delta[t - 1][i] * A[i][j] for i in range(N))
            delta[t][j] = max_val * B[j][obs_idx]
            psi[t][j] = max(range(N), key=lambda i: delta[t - 1][i] * A[i][j])  
    # Backtrack to get the most probable states
    state_seq = [0] * T
    state_seq[T - 1] = max(range(N), key=lambda j: delta[T - 1][j])
    for t in range(T - 2, -1, -1):
        state_seq[t] = psi[t + 1][state_seq[t + 1]]  
    state_path = [hidden_states[state] for state in state_seq]
    return state_path, delta
