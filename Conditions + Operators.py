# Conditions
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

# 1 conditions
num=45
if num%5==0 and not(num%2==0) and num>20:
    print("valid")
else:
    print("invalid")

#2
num=18
if num%2==0 and num%3==0 and num<50:
    print("special")
else:
    print("not spacial")

#3
num=7
if num%2==0 and num>10:
    print("pass")
else:
    print("fail")

#4
num=25
if num%5==0 and not(num%2==0) and num>15:
    print("correct")
else:
    print("wrong")

#5
num=15
if num%5==0 and num%3==0 and not(num%2==0):
    print("perfect")
else:
    print("not perfect")

# Membership Operators
#1
nums=[2,4,6,8,10]
if 6 in nums:
    print("found")
else:
    print("not found")
#2
fruits=["Apple","Banana","Mango"]
if "Grapes" not in fruits:
    print("not available")
else:
    print("available")
#3
num=15
nums=[5,10,15,20]
if num in nums and not(num%2==0):
    print("valid")
else:
    print("invalid")
#4
nums=[3,6,9,12,15]
num=9
if num in nums and num%3==0:
    print("correct")
else:
    print("wrong")
#5
fruits=["apple","banana","mango"]
item="banana"
if item in fruits and item != "apple":
    print("allowed")
else:
    print("not allowed")
#6
nums=[10,15,20,25]
num=20
if num in nums and num%2==0 and num%5==0:
    print("perfect")
else:
    print("not perfect")
#7
fruits=["apple","banana","mango","grapes"]
item="apple"
if item in fruits and item!="banana" and item!="grapes":
    print("allowed")
else:
    print("not allowed")

# comparison vs membership
# Q1
colors=["red","blue","green"]
item="blue"
if item in colors and item!="red":
    print("valid")
else:
    print("invalid")
# Q2
names=["raj","aman","sita"]
name="aman"
if name in names and name!="raj" and name!="sita":
    print("selected")
else:
    print("rejected")
# Q3
fruits=["apple","banana","mango"]
item="mango"
if item in fruits and item!="apple" and item!="banana":
    print("accept")
else:
    print("reject")

# Identity Operators
a=[10,20]
b=[10,20]
c=a
print(a==b)
print(a is b)
print(a is c)

# Q1 
x=[1,2]
y=x
z=[1,2]
print (x is y)
print(x is z)
print(x==z)
# Q2
a=1000
b=1000
print(a==b)
print(a is b)
# Q3 
a=[5,10]
b=a
b.append(20)
print(a)
print(a is b)
# Q4
a=[5,10]
b=a
c=[5,10]
d=c
print(a is b)
print(a==b)
print(c is d)
print(a is c)

# Task 1
a=[1,2,3]
b=a
c=[1,2,3]
a.append(4)
print(a)
print(b)
print(a is b)
print(a==c)

# Task 2
x=[10,20]
y=x.copy()
z=x
x.append(30)
print(x)
print(y)
print(z)
print(x is y)
print(x is z)

# Mini Task
nums=[10,20]
nums.append(30)
print(nums)

a=[5,10]
b=a.copy()
a.append(15)
print(a)
print(b)

nums=[1,2,3,2]
nums.remove(2)
print(nums)

# TASk
#1
nums=[10,15,20,25]
num=15
new_nums=nums.copy()
if num in nums and not(num%2==0) and num%5==0:
    new_nums.append(num)
    print(new_nums)
# Q1
nums=[1,2,3]
new_nums=nums.copy()
new_nums.append(4)
print(new_nums)
print(nums)
# Q2
nums=[10,20,30]
nums.remove(20)
print(nums)
# Q3
nums=[15,10]
new_nums=nums.copy()
nums.append(15)
print(nums)
print(new_nums)
# Q4 
nums=[2,4,6]
num=3
if num not in nums and num%2!=0:
    new_nums=nums.copy()
    new_nums.append(num)
    print("new_nums:",new_nums)
else:
    print("nums:",nums)

# TASK 
# Q1
num=8
if num%2==0:
    print("even")
# Q2
num=9
if num%2!=0 and num%3==0:
    print("valid")
else:
    print("invalid")
# Q3 
nums=[2,4,6]
num=5
if num not in nums and num%2!=0:
    nums.append(num)
    print(nums)
# Q4
nums=[10,20]
new_nums=nums.copy()
nums.append(30)
print("nums:",nums)
print("new_nums",new_nums)
# Q5
nums=[5,10,15]
num=10
if num in nums and num%2==0:
    new_nums=nums.copy()
    new_nums.append(num)
    print("new_nums:",new_nums)
else:
    print("nums:",nums)
# TASK 
# Q1 
num=11
if num%2!=0 :
    print("odd")
else:
    print("even")
# Q2
num=12
if num%3==0 and num%2==0:
    print("yes")
else:
    print("no")
# Q3
nums=[1,3,5]
num=2
if num not in nums and num%2==0:
    nums.append(num)
    print(nums)
# Q4
nums=[17,14]
new_nums=nums
nums.append(21)
print(new_nums)
print(nums)
# Q5
nums=[2,4,6]
num=4
if num in nums and num%2==0:
    new_nums=nums.copy()
    new_nums.append(num)
    print(new_nums)
else:
    print(nums)
#TASK 
# Q!
num=14
if num%2==0:
    print("even")
else:
    print("odd")
# Q2
num=7
if num%2!=0:
    print("valid")
else:
    print("invalid")
# Q3
nums=[2,4,6]
num=3
if num not in nums and num%2!=0:
    nums.append(num)
    print(nums)
# Q4
nums=[10,20]
new_nums=nums.copy()
nums.append(30)
new_nums.append(40)
print(new_nums)
print(nums)
# Q5
nums=[5,10,15]
num=10
if num in nums and num%2==0 and num%5==0:
    new_nums=nums.copy()
    new_nums.append(num)
    print(new_nums)
else:
    print(nums)