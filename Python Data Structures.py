# List basic test
# Output Prediction
print("-----L I S T-----")
nums = [10,20,30,40]
print(nums[2])

nums=[10,20,30,40]
print(nums[-1])

nums=[10,20,30,40,50]
print(nums[1:4])

# List Methods
nums=[1,2,3]
nums.append(4)
print(nums)

nums=[1,2,3]
nums.extend([4,5])
print(nums)

# INSERT method
print("--INSERT method--")
nums=[10,20,30]
nums.insert(1,99)
print(nums)

nums=[10,20,30]
nums.insert(1,99)
print(nums)

nums=[10.20,30]
nums.insert(0,5)
print(nums)

nums=[10,20,30]
nums.insert(3,40)
print(nums)

nums=[10,20,30]
nums.insert(100,50)
print(nums)

# REMOVE method
print("--REMOVE method--")
nums=[10,20,30,40]
nums.remove(30)
print(nums)

nums=[10,20,30,40]
nums.remove(20)
print(nums)

nums=[10,20,20,30]
nums.remove(20)
print(nums)

nums=[10,20,30,50]
nums.remove(50)
print(nums)

# POP method
print("--POP method--")
nums=[10,20,30,40]
nums.pop(1)
print(nums)

nums=[10,20,30,40]
x=nums.pop()
print(x)
print(nums)

nums=[5,10,15]
a=nums.pop()
b=nums.pop()
print(a)
print(b)
print(nums)

# sort() vs sorted() method
nums=[5,2,8,1]
nums.sort()
print(nums)

nums=[5,2,8,1]
x=sorted(nums)
print(x)
print(nums)

nums=[5,2,8,1]
x=sorted(nums)
print(x)

nums=[3,1,4]
a=sorted(nums)
nums.sort()
print(a)
print(nums)

c=[5,2,8,1]
x=sorted(c,reverse=True)
print(x)

# List Comprehension (Very Important for ML)
nums=[1,2,3,4]
result=[]
for i in nums:
    result.append(i*2)
print(result)

num=[1,2,3,4,]
result=[i*2 for i in nums]
print(result)

nums=[1,2,3,4]
result=[]
for i in nums:
    result.append(i**2)
print(result)

nums=[1,2,3,4]
result=[i**2 for i in nums]
print(result)

# filtering
nums=[1,2,3,4,5,6]
result=[]
for i in nums:
    if i%2==0:
        result.append(i)
print(result)

nums=[1,2,3,4,5,6]
result=[i for i in nums if i%2==0]
print(result)

# clean nagtive Value
data=[10,-5,20,-2,30]
clean_data=[x for x in data if x>=0]
print(clean_data)

nums=[1,2,3]
result=[i+1 for i in nums]
print(result)

nums=[2,4,6]
result=[i//2 for i in nums]
print(result)

nums=[1,2,3,4,5]
result=[i for i in nums if i>3]
print(result)

# if-else List Comprehension
print("--if-else List Comprehension--")
nums=[1,2,3,4]
result=[]
for i in num:
    if i%2==0:
        result.append("Even")
    else:
        result.append("Odd")
print(result)

nums=[1,2,3,4]
result=["Even" if i%2==0 else "Odd" for i in nums]
print(result)

# Knowledge Check (Test)
print("--Knowledge Check (Test)--")
nums=[1,2,3]
result=["Big" if i>2 else "Small" for i in nums]
print(result)

nums=[2,4,6,7]
result=["Even" if i%2==0 else "Odd" for i in nums]
print(result)

nums=[5,10,15]
result=[i*2 if i>5 else i for i in nums]
print(result)

# Final List Assessment Test
# Question 1: Indexing
fruits=["Apple","Banana","Orange","Mango"]
print(fruits[3])
# Question 2: Slicing
data=[10,20,30,40,50]
print(data[1:4])
# Question 3: append()
nums=[1,2,3]
nums.append(4)
print(nums)
# Question 4: extend()
num=[1,2,3]
num.extend([4,5])
print(num)
# Question 5: insert()
a=[10,20,30]
a.insert(1,99)
print(a)
# Question 6: remove()
b=[10,20,30,40]
b.remove(30)
print(b)
# Question 7: pop()
e=[10, 20, 30, 40]
f=e.pop()
print(f)
print(e)
# Question 8: sort()
g=[5, 2, 8, 1]
g.sort()
print(g)
# Question 9: sorted()
h=[5, 2, 8, 1]
h_new=sorted(h)
print(h_new)
print(h)
# Question 10: List Comprehension
numss=[1, 2, 3, 4]
result=[i*2 for i in numss] 
print(result)
# Question 11: Filtering Comprehension
n=[1, 2, 3, 4, 5, 6]
result=[i for i in n if i%2==0]
print(result)
# Question 12: If-Else Comprehension
l=[1,2,3,4]
result=["Even" if i%2==0 else "Odd" for i in l ]
print(result)

# Copy vs Reference Roadmap
print("--Copy vs Reference Roadmap--")
x=[1,2]
y=x
x.append(3)
print(x)
print(y)

a = [1,2]
b = a
print(id(a))
print(id(b))

a=[1,2,3,4]
b=a
a.append(5)
print(a)
print(b)

a=[1,2,3,4,5]
b=a.copy()
b.append(6)
print(a)
print(b)

# Nested Lists
print("--Nested Lists Assessment Test--")
# Nested Lists Assessment Test
a=[[10,20],
   [30,40]]
print(a) #Q1
print(a[0]) #Q2
print(a[0][1]) #Q3
print(a[1][0]) #Q4

data=[["Navjot", 90],
["Deepika", 85],
["Komal", 78]]
print(data) #Q5
print(data[1][0]) #Q6
print(data[2][1]) #Q7

Data=[
 [100,200],
 [300,400]
]
print(Data[0]) #Q9.a 100
print(Data[1]) #b 300
print(Data[0][1]) #c 200
print(Data[1][0]) #d 300

data=[
 ["Python", 95],
 ["ML", 88],
 ["AI", 99]
]
print(data[2][1])
print(data[0][0]) 
print(data[1][0])

# Nested Lists + For Loop
print("--Nested Lists + For Loop--")
data=[
    ["Navjot", 90],
    ["Deepika", 85],
    ["Komal", 78]
]
for row in data:
    print(row)

data=[
    ["Navjot", 90],
    ["Deepika", 85],
    ["Komal", 78]
]
for row in data:
    print(row[0])

data=[
    ["Navjot", 90],
    ["Deepika", 85],
    ["Komal", 78]
]
for row in data:
    print(row[1])

data=[["Navjot", 90],
    ["Deepika", 85],
    ["Komal", 78]
]
for row in data:
    print(row[0],row[1])

dataa=[["Navjot", 90],
    ["Deepika",85],
    ["Komal",78]
]
for row in dataa:
    if row[1]>=85:
        print("row:",row[0])

data=[["Navjot", 90],
    ["Deepika",85],
    ["Komal",78]]
for row in data:
    if row[1]<80:
        print(row[0])

# Final Lists Assessment (Comprehensive)
# Question 1: Indexing
list=[10, 20, 30, 40, 50]
print(list[2])
print(list[1:4]) # Question 2: Slicing
# Question 3: append()
list=[1, 2, 3]
list.append(4)
print(list)
# Question 4: extend()
list=[1, 2, 3]
list.extend([4,5])
print(list)
# Question 5: insert()
list=[10, 20, 30]
list.insert(1,99)
print(list)
# Question 6: remove()
list=[10, 20, 30, 40]
list.remove(30)
print(list)
# Question 7: pop()
list=[10, 20, 30, 40]
new_list=list.pop()
print(new_list)
print(list)
# Question 8: sort() vs sorted()
list=[5, 2, 8, 1]
new_list=sorted(list)
# Part A
print(new_list)
print(list)
# Part B
list.sort()
print(list)
# Question 9: Filtering Comprehension
list=[1, 2, 3, 4, 5, 6]
result=[i for i in list if i%2==0]
print(result)
# Question 10: If-Else Comprehension
list=[1, 2, 3, 4]
result=["Even" if i%2==0 else "Odd" for i in list ]
print(result)
# Question 12: Nested List
list=[["Navjot", 90],
["Deepika", 85],
["Komal", 78]]
print(list[1][0])
# Question 13: Nested List + Loop
list=[["Navjot", 90],
["Deepika", 85],
["Komal", 78]]
for row in list:
    if row[1]>=85:
        print(row[0])

# Exercise 1: Training Losses Store Karna (ML Mini Exercise)
epoch=[0.90,0.75,0.60,0.45,0.30]
for i in epoch:
    print(i)
# Exercise 2: Outlier / Noise Filter
values=[10, 15, 20, 999, 18, 22, 1000]
new_list=[i for i in values if i<=100]
print(new_list)

# Tuple
print("-----T U P L E-----")
t=(10,20,30)
print(t)

t=(10,20,30)
print(t[0])
print(t[2])

t=(10,20,30)
print(t[1])

# len()
t=(10,20,30)
print(len(t))

# Slicing
print("--Slicing--")
t=(10,20,30,40,50)
print(t[1:4])
print(t[-1])
print(t[-2])

# Tuple Packing
print("--Tuple Packing--")
a=10,20,30
print(a)
print(type(a))

x=5,
print(x)
print(type(x))

x = (5)
print(type(x))

# Tuple Unpacking
print("--Tuple Unpacking--")
student=("Navjot",90)
name,marks=student
print(name)
print(marks)

person=("Navjot",20,"Python")
name,age,subject=person
print(subject)
print(age)

# Wildcard Unpacking (*)
print("--Wildcard Unpacking (*)--")
data=(10,20,30,40,50)
a,*b,c=data
print(a)
print(b)
print(c)

student = ("Navjot", 90, 85, 88, 92)
name,*marks,rollno=student
print(name)
print(marks)

data = (100,200,300,400)
*a, b = data
print(a)
print(b)

# Tuple methods
# Count()
print("--Count()--")
t=(10,20,10,30,10)
print(t.count(10))

t=(5,5,10,20,5,30)
print(t.count(20))
print(t.count(100))

# index()
print("--index()--")
t=(10,20,30,40)
print(t.index(30))

# Tuple as Dictionary Key
print("--Tuple as Dictionary Key--")
student={
    "name" : "Navjot",
    "marks" : 90
}
print(student["name"])

data={
    (1,2):"A",
    (3,4):"B"
}
print(data[(3,4)])

# DICTIONARY
print("-----DICTIONARY-----")
student={
    "name":"navjot",
    "marks": 90
}
print(student["name"])

student={
    "name":"Navjot",
    "marks": 90,  
    "city":"Nurmahal"
}
print(student["marks"])
print(student["city"])

# Updating Value
print("--Updating Value--")
student={
    "name":"navjot",
    "marks":90
}
student["marks"]=95
print(student["marks"])

student={
    "name":"navjot",
    "marks":90
}
student["city"]="nurmahal"
print(student)

person={
    "name":"deepika"
}
person["age"]=20
person["name"]="komal"
print(person)

# .get()
print("--.get()--")
student={
    "name":"navjot",
    "marks":90
}
print(student.get("name"))

student={
    "name":"navjot",
    "marks":90
}
print(student.get("city"))

student={
    "name":"navjot",
    "marks":90
}
print(student.get("marks"))
print(student.get("city"))

# .keys()
print("--.keys()--")
student={
    "name":"navjot",
    "marks":90,
    "city":"nurmahal"
}
print(student.keys())
print(student.values())

student={
    "name":"navjot",
    "marks":90,
    "city":"nurmahal"
}
print(student.items())

# Next Topic: Dictionary Iteration (For Loop)
print("--Next Topic: Dictionary Iteration (For Loop)--")
student={
    "name":"navjot",
    "marks":90,
    "city":"nurmahal"
}
for key in student:
    print(key)

student={
    "name":"navjot",
    "marks":90,
    "city":"nurmahal"
}
for key in student:
    print(student[key])

student={
    "name":"navjot",
    "marks":90,
}
for key,value in student.items():
    print(key,value)

student={
    "name":"navjot",
    "marks":90,
}
for key,value in student.items():
    print(value)

# Dictionary Assessment Test
print("---Dictionary Assessment Test---")
student={
    "name":"navjot",
    "marks":90
}
print(student["marks"]) #Question 1: Dictionary Creation + Access
student["marks"]=95 #Question 2: Update Value
print(student["marks"])
print(student)
# Question 3: Add New Key
student={"name":"Navjot"}
student["city"]="Nurmahal" 
# Question 4: .get()
student={
    "name":"navjot",
    "marks":90
}
print(student.get("marks"))
print(student.get("city"))
# Question 5: .keys()
student={
    "name":"Navjot",
    "marks":90,
    "city":"Nurmahal"
}
print(student.keys())
print(student.values()) # Question 6: .values()
print(student.items()) # Question 7: .items()
# Question 8: Dictionary Loop
student={
    "name":"navjot",
    "marks":90
}
for key in student:
    print(key)
# Question 9: Dictionary Loop + Values
student={
    "name":"navjot",
    "marks":90
}
for key in student:
    print(student[key])
# Question 10: .items() + Unpacking
student={
    "name":"navjot",
    "marks":90
}
for key,value in student.items():
    print(key,value)

# Nested Dictionaries
print("--Nested Dictionaries--")
student={
    "name":"Navjot",
    "marks":{
        "python":90,
        "ml":85
        }
}
print(student["name"])

student={
    "name":"Navjot",
    "marks":{
        "python":90,
        "ml":85
        }
}
print(student["marks"])

student={
    "name":"Navjot",
    "marks":{
        "python":90,
        "ml":85
        }
}
print(student["marks"]["python"])
print(student["marks"]["ml"])

student={
    "name":"Navjot",
    "marks":{
        "python":90,
        "ml":85
        }
}
student["marks"]["python"]=95
print(student["marks"]["python"])

student={
    "name":"Navjot",
    "marks":{
        "python":90,
        }
}
student["marks"]["ml"]=85
print(student["marks"]["ml"])

students={
    "student1":{
        "name":"Navjot",
        "marks":85
    },
    "student2":{
        "name":"Komal",
        "marks":85
    }
}
print(students["student2"]["name"])
# Dictionary Comprehension
print("--Dictionary Comprehension--")
nums=[1,2,3]
result={i:i*10 for i in nums}
print(result)

nums=[1,2,3,4]
result={i:i**2 for i in nums if i%2==0}
print(result)

words=["ai","ml","ai"]
result={i: words.count(i)for i in words}
print(result)

words = ["a", "b", "a", "c", "b"]
result = {i: words.count(i) for i in set(words)}
print(result)

nums=[1,2,3]
result={i:i+5 for i in nums}
print (result)

num=[1,2,3]
result={i:i*2 for i in num}
print(result)

nums=[5,10,15]
result={i:i+5 for i in nums}
print(result)

nums=[1,2,3,4]
result={i:i*10 for i in nums if i%2==0}
print(result)

nums=[3,4,5,6]
result={i:i*3 for i in nums if i>4}
print(result)

words=["ai","ml","python"]
result={i:len(i) for i in words}
print(result)

nums=[2,4]
result={i:i**3 for i in nums}
print(result)

words=["AL","ML","PYTHON"]
result={word: word.upper() for word in words}
print(result)

words=["cat", "dog", "bird"]
result={word: len(word) for word in words}
print(result)

words = ["ai", "ml", "ai"]
result={i:words.count(i) for i in words}
print(result)

words=["cat","dog","cat","cat","bird"]
result={i:words.count(i) for i in words}
print(result)

nums=[1,2,3]
result={i: i**2 for i in nums}
print(result)

# Question 1 (Easy)
nums=[2,4,6]
result={i:i*5 for i in nums}
print(result)

# Question 2 (Easy)
words=["apple","mango","banana"]
result={}
for word in words:
    result[word]=len(word)
print(result)

# Question 3 (Medium)
words=["AI","ML","AI"]
result={i:words.count(i) for i in words}
print(result)

# Question 4 (Medium)
words = ["AI","ML","AI"]
result = {i: words.count(i) for i in set(words)}
print(result)

# Question 5 (Thoda Different)

nums = [1,2,3]
result = {i: i**2 for i in nums if i != 2}
print(result)