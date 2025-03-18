#Make the dictionary
Language_popularity = {"JavaScript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5}
#Import models
import numpy as np
import matplotlib.pyplot as plt
#Define 'languages' and 'percentages'
languages= list(Language_popularity.keys())
percentages= list(Language_popularity.values())

#Provide with information of the plot
plt.bar(languages, percentages)
plt.xlabel('Programming Languages')
plt.ylabel('Percentage of Developers')
plt.title('Popularity of Programming Languages')
#Show the plot
plt.show()
#Identify the language to query
language_to_query="Python"
#Show the conclusion
print(f"The percentage of developers using {language_to_query} is {Language_popularity[language_to_query]}%")