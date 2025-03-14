#Define weight as the number the user inputs, with the unit as kg, can be decimal friction
weight=float(input("your weight(kg):"))
#Define height as the number the user inputs, with the unit as m, can be decimal friction
height=float(input("your height(m):"))
#Define BMI 
BMI=weight/(height**2)
#Calculate BMI of the user, show the situation of the user's weight according to the BMI
if BMI<18.5:
    category="under weight"
elif 18.5<=BMI<30:
    category="normal weight"
else:
    category="obese"
print("your BMI is",BMI)
print("your situation is",category)
    
