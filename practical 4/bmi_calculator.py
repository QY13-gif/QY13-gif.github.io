weight=float(input("your weight(kg):"))
height=float(input("your height(m):"))
BMI=weight/(height**2)
if BMI<18.5:
    category="under weight"
elif 18.5<=BMI<30:
    category="normal weight"
else:
    category="obese"
print("your BMI is",BMI)
print("your situation is",category)
    
