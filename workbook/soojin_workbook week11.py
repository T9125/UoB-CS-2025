# 1. Calculating the total of numbers from 1 to 10
total=0
for i in range (1, 11):
    total+=i
print(total)

i=1
total=0
while i<11:
    total+=i
    i+=1
print(total)

# 2. Create password validation with while loop.
password="1234"
value=input("Input password: ")
while value!=password:
   print("Wrong password")
   value=input("Input password again: ")
print("Access granted")

# 3. Calculate total of all numbers from 1 to a given number.
total=0
num=int(input("Input number: "))
for i in range (1, num+1):
    total+=i
print(total)

i=1
total=0
num=int(input("Input number: "))
while i<num+1:
    total+=i
    i+=1
print(total)

# 4. Write a Python program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 100, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
# numbers = [12, 75, 100, 150, 180, 145, 525, 50]
numbers=[12, 75, 100, 150, 180, 145, 525, 50]
for num in numbers:
    if num>500:
        break
    if num>100:
        continue
    if num%5==0:
        print(num)

# 5. Reverse an integer number
# number - 598762
number=598762
result=0
for i in range(len(str(number))):
    temp=number%10
    result=result*10+temp
    number=number//10
print(result)

number=598762
result=0
while number>0:
    temp=number%10
    result=result*10+temp
    number=number//10
print(result)

# 6. Write a Python code to print the following number pattern using a while and for loop.
# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):
    print(i*"*")

i=5
while i>0:
    print(i*"*")
    i-=1

# 7. Write a Python program to print the multiplication table of a given number. The user should input the number, and the program should print the table from 1 to 15.
num=int(input("Input number: "))
for i in range(1, 16):
    print(f"{num}*{i}={num*i}")

num=int(input("Input number: "))
i=1
while i<16:
    print(f"{num}*{i}={num*i}")
    i+=1