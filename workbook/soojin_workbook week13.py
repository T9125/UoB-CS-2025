# 1. Write a program to generate the following pattern with nested loops.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

i=1
while i<5:
    j=1
    while j<i+1:
        print(j,end=" ")
        j+=1
    print()
    i+=1

# 2. Write a Python program to print a rectangle of * with 3 rows and 5 columns.
for i in range(3):
    for j in range(5):
        print("*",end=" ")
    print()

i=0
while i<3:
    j=0
    while j<5:
        print("*",end=" ")
        j+=1
    print()
    i+=1

# 3. Write a Python program to generate the following triangle pattern using nested loops.
# *
# **
# ***
# ****
# *****
for i in range(5):
    for j in range (i+1):
        print("*",end="")
    print()

# 4. Write a program to generate the following pattern using letters.
# A
# A B
# A B C
# A B C D
for i in range(4):
    for j in range (i+1):
        print(chr(j+65),end=" ")
    print()

# 5. Write a Python program to generate the following inverted triangle pattern
# *****
# ****
# ***
# **
# *
for i in range(5, 0, -1):
    print("*"*i)

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# 6. Write a program to create the following pyramid using nested loops:
#    *
#   ***
#  *****
# *******
for i in range(5):
    for j in range(4-i):
        print(" ", end="")
    for j in range(2*i-1):
        print("*", end="")
    print()

# 7. Write a program to generate a 4x4 checkerboard pattern with X and O.
for i in range(4):
    for j in range(4):
        if j%2==0:
            print("X", end="")
        else:
            print("O", end="")
    print()

# 8. Write a Python program to calculate the sum of numbers in the following 2D list:
numbers=[
[1, 2],
[3, 4],
[5, 6]
]

total=0
for i in range(3):
    for j in range(2):
        total+=numbers[i][j]
print(total)

total=0
for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        total+=numbers[i][j]
print(total)

# 9. Write a Python program to generate a checkerboard pattern of size 8x8 using nested loops. Use "*" for black squares and " " for white squares.
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            print("*", end="")
        else:
            print(" ", end="")
    print()