#Imort models
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Import the path into the work directory
os.chdir(r"C:\Users\cqy111\Desktop\IBI1\QY13-gif.github.io\practical 10")  
#Ensure the work directory
print(os.getcwd())  
print(os.listdir())  

#Let pandas read the csv file
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

#Show the first 5 rows of the file data
print(dalys_data.head(5))

#Show the differnect types of the data in the file and the memeory usage
print(dalys_data.info())

#Show some typical data in this file
print(dalys_data.describe())
#Show the first 10 rows and the third column data
years = dalys_data.iloc[0:10, 2]  
print(years)


#Show each data with the year as 1990
year_1990 = dalys_data.loc[dalys_data["Year"] == 1990, :]
print(year_1990)

#Show each "DALYs" with the year as 1990
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]
print(dalys_1990)
#Select each year and its corresponding DALYs in UK and France
uk= dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
france= dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]
 #Calculate the mean value of DALYs of UK and France
uk_mean = uk["DALYs"].mean()
france_mean = france["DALYs"].mean()
#Show the mean DALYs
print(f"UK mean DALYs: {uk_mean}")
print(f"France mean DALYs: {france_mean}")

#Compare the mean DALYs of UK and France
if uk_mean>france_mean:
    print("UK mean DALYs is bigger than France mean DALYs")
#Make a plot showing the DALYs' change with time in UK (in red color)
plt.plot(uk.Year, uk.DALYs, 'r+')
plt.xticks(uk.Year,rotation=-90)
plt.show()

#Anser the additional question
#Selcet UK and France DALYs data
uk_data = dalys_data[dalys_data["Entity"] == "United Kingdom"]
france_data = dalys_data[dalys_data["Entity"] == "France"]

#Make subplots(Up and down)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 8))

#Make the upper one
axes[0].plot(uk_data["Year"], uk_data["DALYs"], 'b-', label="UK")
axes[0].set_title("DALYs in the United Kingdom")
axes[0].set_ylabel("DALYs")
axes[0].legend()

#Make the lower one
axes[1].plot(france_data["Year"], france_data["DALYs"], 'r-', label="France")
axes[1].set_title("DALYs in France")
axes[1].set_xlabel("Year")
axes[1].set_ylabel("DALYs")
axes[1].legend()

#Ensure the suitable distribution and show the plot
plt.tight_layout()
plt.show()


         
