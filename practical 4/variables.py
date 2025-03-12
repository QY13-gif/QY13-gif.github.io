a=15
b=75
c=a+b
d=90
e=5
f=d+e
if c < f:
    print("walk+bus is faster, full time is:", c,"minutes")
x=True
y=False
w=x and y
print("the value of w is",w)
'''
|x    |y      |w(x and y)     |x or y    |
|True |True   |True           |True      |
|True |False  |False          |True      |
|False|False  |False          |False     |'
'''