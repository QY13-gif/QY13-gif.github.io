# Define the time for walking to the bus stop as 15 minutes
a=15
# Define the time for the bus joiurney as 75 minutes
b=75
# Calculate the total time for taking bus 
c=a+b
# Define the time for driving as 90 minutes
d=90
# Define the time for walking from the car park as 5 minutes
e=5
# Calculate the total time for taking the car
f=d+e
# Compare the total time of these two ways to identify which is faster
if c < f:
    print("walk+bus is faster, full time is:", c,"minutes")
elif c==f:
    print("the two ways are same,full time is:",c,"minutes")
else:
    print("bike+bus is faster, full time is:",f,"minutes")
# Define x as True and y as False
x=True
y=False
# Calculate w as the logical AND of x and y
w=x and y
# Print the truth table for w
print("the value of w is",w)
'''
|x    |y      |w(x and y)     |x or y    |
|True |True   |True           |True      |
|True |False  |False          |True      |
|False|False  |False          |False     |'
'''