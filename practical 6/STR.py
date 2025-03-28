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
#Making a cycle
for _ in range(1000):
  
    infection_prob =beta * I/N #Define the probability of infection
    new_infection=np.random.choice([0,1],S,p=[1-infection_prob,infection_prob]).sum() #Calculate the population newly infected
    new_recoveries=np.random.choice([0,1],I,p=[1-gamma,gamma]).sum() #Calculate the population newly recovered
    S-=new_infection #Calculate susecptible population 
    I+=new_infection - new_recoveries #Caalculate population infected
    R+=new_recoveries #Calculate population recovered
    S_array.append(S) #Update the array
    I_array.append(I)
    R_array.append(R)
#Making the plot
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