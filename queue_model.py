def mm1_metrics(arrival_rate, service_rate):
    if arrival_rate >= service_rate:
        raise ValueError("System is unstable (λ >= μ). Choose λ < μ.") 
    rho = arrival_rate / service_rate  # Utilization
    L = rho / (1 - rho)                # Average number in the system
    Lq = rho**2 / (1 - rho)            # Average number in the queue
    W = 1 / (service_rate - arrival_rate)  # Average time in the system
    Wq = arrival_rate / (service_rate * (service_rate - arrival_rate))  # Average waiting time  
    return {
        'Utilization (ρ)': rho,
        'Avg Orders in System (L)': L,
        'Avg Orders in Queue (Lq)': Lq,
        'Avg Time in System (W)': W,
        'Avg Waiting Time (Wq)': Wq
    }
