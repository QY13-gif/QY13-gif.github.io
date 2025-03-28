import numpy as np #Import necessary libraries
import matplotlib . pyplot as plt
#Define the variabes
population=np.zeros((100,100))
outbreak = np.random. choice(range(100) ,2)
population [ outbreak [0] , outbreak [1]] = 1
#Making a plot of the initial outbreak
plt . figure ( figsize =(6,4),dpi=150)
plt .imshow(population , cmap='viridis' , interpolation='nearest' )
plt.show()
#Making an infection model
def spatial_spread(pop, beta=0.3, gamma=0.05):
    new_pop=pop.copy()
    infected_pos=np.where(pop==1)

    for x, y in zip(*infected_pos):
        for i in [x-1,x,x+1]:
            for j in [y-1,y,y+1]:
                if (i,j)!=(x,y) and 0<=i<100 and 0<=j<100:
                    if pop[i,j]==0 and np.random.rand()<beta:
                        new_pop[i,j]=1
        if np.random.rand()<gamma:
             new_pop[x,y]=2

    return new_pop
#Making a plot of the infection
plt.figure(figsize=(12,4))
for day in range(1,101):
    population=spatial_spread(population)
    if day in[1,10,50,100]: #Making subplots of specific time points
        plt.subplot(1,4,[1,10,50,100].index(day)+1)
        plt.imshow(population,cmap='viridis',interpolation='nearest')
        plt.title(f"Day{day}")
plt.tight_layout()
plt.show()