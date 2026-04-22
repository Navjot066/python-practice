# Level 1 (Basic)
# Addition + Update
x=5+10
print(x)
# Division vs Floor Division
a=7
b=2
x=(a/b)
print(x)
x=(a//b)
print(x)
# Remainder check
num=9
if num % 2 == 0:
    print("even")
else:
    print("odd")

# Level 2 (Conditions + Operators)
# Range check
x=25 
if x>=10 and x<=30:
    print("in range")
else:
    print("out of range")
# Greater number
a=15
b=30
if a>b:
    print("a is greater")
else:
    print("b is greater")
# equal or not
x=10
y=10
if x==y:
    print("x is equal to y")
else:
    print("x is not equal to y")

# Level 3 (Real Logic 🔥)
# Special Number
num=30
if num%5==0 and num>=10:
    print("Special")
else:
    print("not special")
# Update + Logic mix
score=50
score+=20
score*=2
if score>100:
    print("High Score")
else:
    print("Normal Score")
# Mixed Operators
num=24
if num%2==0 and num%3==0 and num>10:
    print("Valid Number")
else:
    print("Invalid number")