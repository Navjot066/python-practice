# function
print("**FUNCTION")

# 1.No Parameter, No Return
print(("--No Parameter, No Return--"))
def hello():
    print("hi")
hello()
hello()

def show():
    print("a")
print("b")
show()

def greet():
    print("hi")
greet()
print("done")
greet()

def show():
    print("x")
for i in range(3):
    show()

def show():
    print("hi")
    print("bye")
for i in range(2):
    show()

def show():
    print("a")
    print("b")
for i in range(3):
    print("x")
    show()

def f():
     print("1")
     print("2")

for i in range(2):
     print("START")
     f()
     print("END")

def greet(name):
     print("Hello", name)

x=greet("Navjot")
print(x)

# 2.PERAMETERS, NO RETURN
print("--PERAMETERS, NO RETURN--")
def show(num):
    print(num+10)

show(5)
show(3)

def display(x):
    print(x)
    print(x*2)
display(4)

def test(a):
    print(a+1)
for i in range(3):
    test(i)

def show(num):
    print(num*10)
show(2)
show(5)
show(1)

def hello(name):
    print("hi",name)
hello("sara")

def show(num):
    print(num*2)
show(4)
show(7)

def add(a,b):
    print(a+b)
add(2,3)

def calc(a,b):
    print(a*b)
calc(3,4)
calc(2,5)

def info(name,age):
    print(name,age)
info("ali","20")

#3.NO Parameter ,Return
print("--NO PARAMETER, RETURN--")
def add(a,b):
    return a+b
result=add(2,3)
print (result)

def double(num):
    return num*2
x=double(5)
print(x)

def add(a,b):
    return a+b
print(add(3,2))

def test():
    return 5
print(test())

def show():
    return 10
x=show()
print(x)

def show():
    return 10
y=show()
print(y+5)

def show():
    return 10
print(show()+show())

def test():
    print(5)
x=test()
print(x)

def show():
    print(10) 
x=show()
print(x)

def test():
    return 5
x= test()
print(x)

# Parameter + Return
print("--Parameter + Return--")

def add(num):
    return num+5
print(add(3))

def add(num):
    return num+5
x=add(3)
print(x)

def double(x):
    return x*2
a=double(5)
print(a)

def square(n):
    return n*n
print(square(2))
print(square(4))

def add(num):
    return num+1
for i in range(3):
    print(add(i))

# Positional Arguments
print("--Positional Arguments--")
def add(a,b):
    print(a+b)
add(2,3)

def show(a,b):
    print(a)
    print(b)
show(5,8)

def show(a,b):
    print(a-b)
show(10,3)

def calc(a,b):
    print(a*b)
calc(2,4)
calc(3,5)

def show(a,b):
    print(a)
    print(b)
show(7,2)
show(1,9)

# Keyword Arguments/
print("--Keyword Arguments--")
def show(a,b):
    print(a)
    print(b)
show(b=10,a=5)

def calc(a,b):
    print(a+b)
calc(b=4,a=2)

def show(name,age):
    print(name)
    print(age)
show(age=20,name="Navjot")

def greet(name="Guest"):
    print(name)
greet()
greet("Navjot")

def show(num=5):
    print(num)
show()
show(10)

def greet(name="Guest"):
    print(name)
greet()
greet("Navjot")
greet(name="Aman")

# *args
print("--*args--")
def show(*nums):
    print(nums)
show(1,2,3)

def show(*x):
    print(x)
show(5,10)

def show(*nums):
    for n in nums:
        print(n)
show(2,4,6)

def show(*nums):
    print(len(nums))
show(1,2,3,4)

def add(*nums):
    total=0
    for n in nums:
        total=total+n
    print(total)
add(1,2,3)

def show(*nums):
    for n in nums:
        print(n*2)
show(2,5,8)

# **kwargs
print("--**kwargs--")
def show(**data):
    print(data)
show(name="navjot",age=20)

def show(**data):
    print(data["name"])
show(name="Aman",age=18)

def show(**data):
    print(data["age"])
show(name="Navjot",age=20)
show(name="Aman",age=18)

# Scope
print("--Scope--")
x=10
def show():
    print(x)
show()

x=10
def show():
    x=5
    print(x)
show()
print(x)

x=100
def show():
    print(x)
show()
print(x)

x=10
def show():
    x=20
    print(x)
show()
print(x)

# Global use
x=5
def show():
    print(x)
show()

def show():
    x=10
    print(x)
show()

# global keyword
print("--global keyword--")
x=10
def show():
    global x
    x=20
    print(x)
show()
print(x)

x=5
def fun():
    global x
    x=x+10
    print(x)
fun()
print(x)

# Return Concepts = Single Return
print("--Return Concepts Single Return--")
def show():
    return 10
x=show()
print(x+5)

def test():
    return 7
print(test()*2)

# Multiple Return
print("--Multiple Return--")
def calc():
    return 10,20
a,b=calc()
print(f"a is {a}")
print(f"b is {b}")

def test():
    return 5,8
x,y=test()
print(x+y)

def calc():
    return 2,4
a,b=calc()
print(a*b)

# Returning Lists/Tuples
print("--Returning Lists/Tuples--")
def show():
    return [1,2,3]
x=show()
print(x)

def show():
    return [2,4,6]
data=show()
print(data[1])

def show():
    return (10,20,30)
x=show()
print(x[2])

def get_data():
    return [10,20,30]
data=get_data()
total=0
for value in data:
    total=total+value
print(total)

# Task 1 — Parameter + Return
def add(a,b):
    return a+b
print(add(3,7))

# Task 2 — Default Argument
def greet(name="Guest"):
    print(name)
greet()
greet("Navjot")

# Task 3 — Multiple Return
def data():
    return 10,20
a,b=data()
print(a)
print(b)

# Task 4 — Returning List
def numbers():
    return [1,2,3,4]
data=numbers()
for value in data:
    print(value)

# Task 5 — Scope
x=100
def a():
    print(x)
a()
print(x)

# Task 6 — *args
def total(*nums):
    t=0
    for values in nums:
        t=t+values
    return t
print(total(2,3,5))

# Task 7 — **kwargs
def show(**keyword):
    print(keyword["age"])
show(name="navjot",age=20)

# TASK 1 — Basic Return + Parameter
def multiply(a,b):
    return a*b
print(multiply(4,5))

# TASK 2 — Default + Override
def say_hi(name="user"):
    print("hello",name)
say_hi()
say_hi("Navjot")   

# TASK 3 — Multiple Return (slightly twist
def calc():
    return 15,25
a,b=calc()
print(a)
print(b)

# TASK 4 — List Return + Loop
def get_nums():
    return [3,6,9]
data=get_nums()
for value in data:
    print(value)

# TASK 5 — Scope Check
x=50
def pin():
    print(x)
pin()
print(x)

# TASK 6 — *args (sum)
def add_all(*n):
    total=0
    for value in n:
        total=total+value
    return total
print(add_all(1,2,3,4))

# TASK 7 — **kwargs (simple extract
def info(**keyword):
    print(keyword["name"])
info(name="Aman", age=18)

# FINAL TEST — *args (basic + sum + loop)
def show_all(*n):
    for value in n:
        print(value)
show_all(1,2,3)

# TASK 2 — *args (sum logic)
def total(*n):
    addition=0
    for value in n:
        addition=addition+value
    print(addition)
total(2,3,5)

# TASK 3 — **kwargs (basic print)
def show_data(**keyword):
    print(keyword)
show_data(name="Navjot", age=20)

# TASK 4 — **kwargs (specific value
def get_age(**keyword):
    print(keyword["age"])
get_age(name="Aman", age=18)

# TASK 5 — MIXED (IMPORTANT ⚠️
def test(*args,**kwargs):
    print(args,kwargs)
test(1,2,3,name="Navjot",age=20)

# Lambda Functions (Short Functions)
add=lambda a,b: a+b
print(add(3,4))

f=lambda x: x*2
print(f(5))

# INTERVIEW TEST 1 — Function + Return + Scope
x=10
def show():
     x=20
     print(x)
show()
print(x)

# TASK 2 — Return + Calculation
def calc(a,b):
    return a+b , a*b
sum_result,mul_result=calc(3,4)
print(sum_result)
print(mul_result)

# TASK 3 — *args (interview pattern
def add_all(*n):
    total=0
    for value in n:
        total=total+value
    print(total)
add_all(1,2,3,4)

# TASK 4 — **kwargs (real interview)
def student(**keyword):
    print(keyword["age"])
student(name="Navjot", age=20, city="Punjab")

# MIXED (VERY IMPORTANT ⚠️)
def test(*args,**kwargs):
    print(args,kwargs)
test(1,2,3,name="Aman",age=18)  




