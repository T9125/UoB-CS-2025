# 1.
num1=int(input("Input number: "))
if num1>0:
    print("Positive")
elif num1<0:
    print("Negative")
else:
    print("Zero")

# 2.
grade=int(input("Input grade: "))
if 70<=grade<=100:
    print("1st")
elif 60<=grade<=69:
    print("2.1")
elif 50<=grade<=59:
    print("2.2")
elif 40<=grade<=49:
    print("3rd")
elif 0<=grade<=39:
    print("F")
else:
    print("Invalid grade")

# 3.
year=int(input("Input year: "))
if year%400==0:
    print("Leap year")
elif year%100==0:
    print("Not a leap year")
elif year%4==0:
    print("Leap year")
else:
    print("Not a leap year")

# 4.
age=int(input("Input age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 5.
num2= int(input("Input number: "))
if num2%5==0 and num2%11==0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by both")

# 6.
units=int(input("Input units consumed: "))
bill = 0
if units<=100:
    bill=units*0.50
elif units<=200:
    bill=100*0.50+(units-100)*0.75
elif units<=300:
    bill=100*0.50+100*0.75+(units-200)*1.20
else:
    bill =100*0.50+100*0.75+100*1.20+(units-300)*1.50
print("Total bill:", bill)

# 7.
num3 = int(input("Input first number: "))
num4 = int(input("Input second number: "))
operator = input("Input operator (+, -, *, /): ")

if operator=="+":
    print(num3+num4)
elif operator=="-":
    print(num3-num4)
elif operator=="*":
    print(num3*num4)
elif operator=="/":
    print(num3/num4)
else:
    print("invalid operator")

# 8.
month=int(input("Input month: "))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print(31)
elif month==4 or month==6 or month==9 or month==11:
    print(30)
elif month==2:
    print(28)
else:
    print("Invalid month")