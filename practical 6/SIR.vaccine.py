# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm  

# Define variables
N = 10000
I_initial = 1  
R_initial = 0
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
beta = 0.3
gamma = 0.05
results = {}  

for rate in vaccination_rates:
    V = int(N * rate)
    S = N - I_initial - V
    I = I_initial  
    R = R_initial
    
    
    S_array = [S]
    I_array = [I]
    R_array = [R]
    
    
    for _ in range(1000):
        if S > 0:  
            infection_prob = beta * I / N
            new_infection = np.random.choice(
                [0, 1], 
                S, 
                p=[1-infection_prob, infection_prob]
            ).sum()
        else:
            new_infection = 0
        
        if I > 0:  
            new_recoveries = np.random.choice(
                [0, 1], 
                I, 
                p=[1-gamma, gamma]
            ).sum()
        else:
            new_recoveries = 0
        
        
        S -= new_infection
        I += new_infection - new_recoveries
        R += new_recoveries
        
        
        S = max(S, 0)
        I = max(I, 0)
        R = max(R, 0)
        
        
        S_array.append(S)
        I_array.append(I)
        R_array.append(R)
    
    
    results[rate] = {'S': S_array, 'I': I_array, 'R': R_array}


plt.figure(figsize=(12, 6), dpi=150)
plt.subplot(1, 2, 1)
colors = cm.viridis(np.linspace(0, 1, len(vaccination_rates)))  

for i, rate in enumerate(vaccination_rates):
    plt.plot(
        results[rate]['I'], 
        color=colors[i], 
        label=f'{int(rate*100)}% vaccinated'  
    )

plt.xlabel('Time')  
plt.ylabel('Number of Infected People')
plt.title('Infection Curves with Different Vaccination Rates')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

plt.subplot(1, 2, 2)
peak_infections = [max(results[rate]['I']) for rate in vaccination_rates]
plt.plot(vaccination_rates, peak_infections, 'o-')
plt.xlabel('Vaccination Rate')  
plt.ylabel('Peak Number of Infections')
plt.title('Herd Immunity Threshold Analysis')

plt.tight_layout()
plt.savefig("SIR_vaccination_results.png")  
plt.show()