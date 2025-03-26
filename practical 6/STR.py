# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Define variables
N=10000
S=N-1
I=1
R=0
beta=0.3
gamma=0.05
# Define array
S_array=[S]
I_array=[I]
R_array=[R]
# Define the probility of infection
for _ in range(1000):
  
    infection_prob =beta * I/N
    new_infection=np.random.choice([0,1],S,p=[1-infection_prob,infection_prob]).sum()
    new_recoveries=np.random.choice([0,1],I,p=[1-gamma,gamma]).sum()
    S-=new_infection
    I+=new_infection - new_recoveries
    R+=new_recoveries
    S_array.append(S)
    I_array.append(I)
    R_array.append(R)
plt.figure(figsize=(6,4),dpi=150)
plt.plot(S_array, label='Susecptible')
plt.plot(I_array,label='Infected')
plt.plot(R_array,label='Recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model')
plt.legend()
plt.savefig("SIR_plot.png")
plt.show()