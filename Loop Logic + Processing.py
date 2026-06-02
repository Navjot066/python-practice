# CONDITION'S STATMENTS 

# loop + conditions
print("**loop + conditions**")
nums=[2,4,6,8]
for i in nums:
    print(i)

nums=[1,3,5]
for i in nums:
    print(i*2)

nums=[2,4,6,8]
for i in nums:
        if i%2==0:
             print(i)

nums=[3,6,9,12]
for i in nums:
     if i%3==0:
          print(i)

nums=[1,2,3,4,5,6]
for i in nums:
     if i%2==0:
          print(i*2)

nums=[5,10,15]
for i in nums:
     print(i)

nums=[2,4,6]
for i in nums:
     print(i+1)

nums=[1,2,3,4,5]
for i in nums:
     if i%2!=0:
          print(i)

nums=[2,3,4,5,6]
for i in nums:
     if i%2==0:
          print(i*10)

nums=[1,2]
for i in nums:
     print(i)
print("done") 

nums=[4,2,7]
for i in nums:
     print("A")
print("B")

nums=[1,2,3]
for i in nums:
     print("x")
print(i)

nums=[5,10]
for i in nums:
     print(i)
print("end")
print(i)

nums=[1,2,3]
for i in nums:
     print(i)

nums=[1,2]
for i in nums:
     print("A")
print("B")

nums=[2,4,6]
for i in nums:
     if i%2==0:
          print(i)

# loop + Accumulator
# Total
print("**loop + Accumulator**")
nums=[1,2,3,4,5,6]
total=0
for i in nums:
     if i%2==0:
          total=total+i
print(total)

nums=[1,2,3,4]
total=0
for i in nums:
     if i%2==0:
          total=total+i
print(total)

# Counting loop
nums=[1,2,3,4,6]
count=0
for i in nums:
     if i%2==0:
          count=count+1
print(count)

nums=[2,5,8,9,10]
count=0
for i in nums:
     if i%2==0:
          count=count+1
print("count:",count)

# Average 
nums=[2,4,6]
total=0
count=0
for i in nums:
     if i%2==0:
          total=total+i
          count=count+1
average=total/count
print(average)

nums=[10,20,30]
total=0
count=0
for i in nums:
     if i%2==0:
          total=total+i
          count=count+1
average=total/count
print(average)

# Data Processing
nums=[1,2,3]
new_nums=[]     
for i in nums:
     new_nums.append(i*2)
print(new_nums)

nums=[2,4,6]
new_nums=[]
for i in nums:
     new_nums.append(i+5)
print(new_nums)

nums=[1,2,3,4,5,6]
new_nums=[]
for i in nums:
     if i%2==0:
          new_nums.append(i)
print(new_nums)

# RANGE
print("**RANGE**")
for i in range(5):
     print(i)

for i in range(3):
     print(i)

for i in range(1,4):
     print(i)

for i in range(1,10,2):
     print(i)

for i in range(2,9,2):
     print(i)

print("**Mixed test**")
for i in range(4):
     print(i)

for i in range(3,7):
     print(i)

for i in range(1,8,3):
     print(i)

# Range + Condition
print("**Range + Condition**")

for i in range(1,7):
     if i%2!=0:
          print(i)

total=0
for i in range(1,10):
     if i%2!=0:
          total=total+i
print(total)

count=0
for i in range(1,16):
     if i%2!=0:
          count=count+1
print(count)

#Even Filter Processing
new_nums=[]
for i in range(1,11):
     if i%2==0:
          new_nums.append(i)
print(new_nums)
#Odd + Processing (Medium)
new_nums=[]
for i in range(1,8):
     if i%2!=0:
          new_nums.append(i*10)
print(new_nums)
#Divisible Processing (Challenge)
new_nums=[]
for i in range(1,16):
     if i%3==0:
          new_nums.append(i+2)
print(new_nums)

# Break and Continue
print("**Break and Continue**")

for i in range(1,7):
     if i==5:
          break
     print(i)

for i in range(1,7):
     if i==4:
          continue
     print(i)

for i in range(1,6):
     if i==2:
          break
     print("i=",i)

for i in range(1,6):
     if i==2:
          continue
     print(i)

# NESTED LOOP
print("**NESTED LOOP**")
for i in range(3):
     for j in range(2):
          print("x")

for i in range(2):
     print("a")
     for i in range(2):
      print("b")

for i in range(2):
     for j in range(3):
          print(j)
     print("end")

print("Final Strength")
for i in range(2):
     print("A")
     for j in range(1):
          print("B")

for i in range(3):
     print(i)
     for j in range(2):
          print("x")

for i in range(2):
     for j in range(2):
          print("i")

for i in range(2):
     print("START")
     for j in range(3):
          print(j)
     print("END")
 
# Nested List Loop / Matrix Loop

matrix=[[1,2],
        [3,4]]
for row in matrix:
     print(row)

matrix=[[5,6],
        [7,8]]
for row in matrix:
     for value in row:
          print(value*2)

matrix=[[1,2,3],
        [4,5,6]]
for row in matrix:
     for value in row:
          if value%2==0:
               print(value)

matrix=[[2,3],
        [4,5]]
total=0
for row in matrix:
     for value in row:
          total=total+value
print(total)

matrix=[
     [1,2],
        [3,4]
        ]
new_data=[]
for row in matrix:
     for value in row:
          if value%2==0:
               new_data.append(value*10)
print(new_data)

# Final Matrix + Loop Test
print("**Final Matrix + Loop Test**")
#Matrix Even Count
matrix=[
[2,5,8],
[1,4,6]
]
count=0
for row in matrix:
     for value in row:
          if value%2==0:
               count=count+1
print(count)
# Matrix Even Count
matrix=[
 [3,7],
 [2,8]
]
total=0
for row in matrix:
     for value in row:
          total=total+value
print(total)
# Matrix Filtering + New List
matrix=[
 [1,2,3],
 [4,5,6]
]
new_data=[]
for row in matrix:
     for value in row:
          if value%2!=0:
               new_data.append(value*5)
print(new_data)
# Matrix Processing Challenge (Final Boss 👀)
matrix=[
[10,15],
[20,25]
]
new_data=[]
for row in matrix:
     for value in row:
          if value>15:
               new_data.append(value+2)
print(new_data)

# WHILE lOOP
print("**WHILE lOOP**")
i=1
while i<=4:
     print(i)
     i=i+1

i=2
while i<=6:
     print(i)
     i=i+2

i=1
while i<=5:
     print(i)
     i=i+2
# WHILE BREAK 
print("--WHILE BREAK--")
i=1
while True:
     print(i)
     if i==5:
          break
     i=i+1

i=2
while True:
     print(i)
     if i==8:
          break
     i=i+2

i=1
while True:
     if i%2!=0:
          print(i)
          if i==7:
               break
     i=i+1

i=1
while True:
     print(i)
     if i==4:
          break
     i=i+1

i=2
while True:
     print(i)
     if i==10:
          break
     i=i+2

i=1
while True:
     if i==4:
          break
     print(i)
     i=i+1

i=1
while True:
     if i%2!=0:
          print(i)
          if i==9:
               break
     i=i+1

# BREAK
print("--BREAK--")
for i in range(1,6):
     if i==2:
          continue
     print(i)

for i in range(1,6):
     if i==3:
          continue
     print(i)

for i in range(1,6):
     if i%2==0:
          continue
     print(i)

for i in range(1,4):
     if i==2:
          continue
     print("a")
     print(i)

i=0

# WHILE CONTINUE
print("--WHILE CONTINUE--")
i=0
while i<4:
     i=i+1
     if i==2:
          continue
     print(i)

i=0
while i<5:
     i=i+1
     if i==3:
          continue
     print(i)

i=0
while i<7:
     i=i+1
     if i%2==0:
          continue
     if i%2!=0:
          print(i)

i=0
while i<4:
     i=i+1
     if i==2:
          continue
     print("x")
     print(i)

# LOOP REVISION FINAL TEST
print("**--LOOP REVISION FINAL TEST--**")

for i in range(1,9):
     if i%2==0:
          continue
     if i%2!=0:
          print(i)

i=1
while True:
     print(i)
     if i==6:
          break
     i=i+1

for i in range(2):
     for j in range(3):
          print("x")
     
matrix=[
     [1,2],
     [3,4]
]
total=0
for row in matrix:
     for value in row:
          total=total+value
print(total)

i=0
while i<6:
     i=i+1
     if i==4:
          continue
     print(i)

matrix=[
     [2,3],
     [4,5]
]
new_data=[]
for row in matrix:
     for value in row:
          if value%2!=0:
               new_data.append(value*10)
print(new_data)