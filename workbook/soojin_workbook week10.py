# 1. Write a program that calculates the Body Mass Index (BMI) and categorises it based on the following:
# BMI < 18.5: Underweight
# 18.5 <= BMI < 24.9: Normal weight
# 25 <= BMI < 29.9: Overweight
# BMI >= 30: Obesity
# Formula: BMI = weight (kg) / height (m)^2
weight=float(input("Input weight(kg): "))
height=float(input("Input height(cm): "))
bmi=weight/((height/100)**2)

if bmi<18.5:
    print("Underweight")
elif bmi<24.9:
    print("Normal weight")
elif bmi<29.9:
    print("Overweight")
else:
    print("Obesity")

# 2. Write a program that calculates Income Tax Calculator tailored for the UK, using the UK's income tax brackets (for the tax year 2024/2025)
# Personal exemption        0%	        Up to £12,570
# Basic rate	            20%	        £12,571 to £50,270
# Higher rate	            40%	        £50,271 to £125,140
# Additional rate	        45%	        Over £125,140
income=float(input("Input annual income: "))
tax=0
basic=12570
higher=50270
additional=125140

if income>additional:
    tax+=(income-additional)*0.45
    tax+=(additional-higher)*0.40
    tax+=(higher-basic)*0.20
elif income>higher:
    tax+=(income-higher)*0.40
    tax+=(higher-basic)*0.20
elif income>basic:
    tax+=(income-basic)*0.20
else:
    tax+=0
print(f"Tax: {tax:.2f}")
print(f"Income: {(income-tax):.2f}")

# 3. Write a Python program to convert temperatures to and from Celsius and Fahrenheit.
print("Choose temperature converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

option=int(input("Choose temperature converter(1 or 2): "))

if option==1:
    c=float(input("Input temperature in celsius: "))
    f=c*9/5+32
    print(f"Temperature in fahrenheit: {f}")
elif option==2:
    f=float(input("Input temperature in fahrenheit: "))
    c=(f-32)*5/9
    print(f"Temperature in celsius: {c}")
else:
    print("Invalid choice")

# 4. Write a program to check if a given number is: Positive or Negative.
# If it’s positive, check if it's even or odd.
# If it’s negative, check if it’s divisible by 3.
number=int(input("Input number: "))
if(number>0):
    if(number%2==0):
        print("Even")
    else:
        print("Odd")
elif(number<0):
    if(number%3==0):
        print("Divisible by 3")
    else:
        print("Indivisible by 3")
else:
    print("Zero")

# 5. Write a program to calculate the bonus of an employee based on the following:
# If the employee's service years are greater than 5:
# If their salary is above £50,000, the bonus is 10%.
# Otherwise, the bonus is 15%.
# If the service years are 5 or below, there is no bonus.
year=int(input("Input service years: "))
salary=int(input("Input salary: "))

if(year>5):
    if(salary>50000):
        print("10% bonus")
    else:
        print("15% bonus")
else:
    print("No bonus")