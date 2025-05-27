#Make two lists
uk_countries=[57.11, 3.13, 1.91, 5.45]
china_provinces=[65.77, 41.88, 45.28, 61.27, 85.15]
#Sort the two lists
uk_countries_sorted= sorted(uk_countries)
china_provinces_sorted= sorted(china_provinces)
#Show the sorted lists
print("Sorted UK countries population:", uk_countries_sorted)
print("Sorted China provincces population:", china_provinces_sorted)
#Import models
import numpy as np
import matplotlib.pyplot as plt
#Provide with data
labels_uk=['England','Scotland','Wales','North Ireland']
labels_china=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu']
colorsA=['gold','yellowgreen','lightcoral','lightskyblue']
colorsB=['pink','purple','green','blue','red']
#Make two subplots
plt.subplot(1,2,1)
plt.pie(uk_countries, labels=labels_uk, autopct='%1.1f%%',colors=colorsA,explode=(0.1,0,0,0))
plt.title('Population Distribution in UK Province')

plt.subplot(1,2,2)
plt.pie(china_provinces,labels=labels_china, autopct='%1.1f%%',colors=colorsB,explode=(0.1,0,0,0,0))
plt.title('Population Distribution in Zhejiang neighbouring Provinces')

#Show the plots
plt.show()



