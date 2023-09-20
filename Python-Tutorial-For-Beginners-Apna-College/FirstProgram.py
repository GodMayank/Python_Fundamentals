# print("Hello World!")

# name = "Mayank kandpal"
# age = 27
# age_fraction = 27.5

# print(name)
# print(age)
# print(age_fraction)

# is_adult = True

# name = input("What is your name?")
# print(name)
# print("Hello " + name)

# superhero_name = input("Hey " + name + ", what is your secret superhero name? ")
# print(name + " is " + superhero_name)

# old_age = input("enter your old age : ")
# new_age = int(old_age) + 2;
# print(new_age)

# print(float(18))
# str()
# bool()

# program to calculate sum of two variables:
# first = input("enter first number : ")
# second = input("enter second number : ")

# sum = int(first) + int(second)

# print("the sum is : " + str(sum))

name = "Tony Stark"
# print(name.upper())
# print(name.lower())
# print(name)

# print(name.find('S')) #This method will return the index of 'S' in string Tony Stark
# print(name.find("Stark"))
# print(name.find('s'))

# print(name.replace("Tony Stark", "Ironman"))
# print(name.replace('T', 'M'))

# print("T" in name)
# print("Stark" in name)
# print("M" in name)

# Operators in python
# print(5 + 2)
# print(5 - 2)
# print(5 * 2)
# print(5 / 2)
# print(5 // 2)
# print(5 % 2)
# print(5 ** 2)

# i = 5
# i = i + 2
# i += 2
# i -= 2
# i *= 2

# operator precedence.
# result = 2 + 3 * 5

# here is a comment

# comparision operator
# print(3 > 2)
# print(2 < 3)
# print(3 <= 2)
# print(3 == 'a')
# print(3 != 'a')

# logical operator
# print(2 > 3 or 2 > 1)
# print(2 > 3 and 3 < 3)
# print(not 2 > 3)

# if else statements
# age = 15
# if age >= 18:
#     print("Adult")
#     print("You can vote")
# else: 
#     print("Teen")
#     print("you can't vote")

# elif
# age = 4
# if age >= 18:
#     print("Adult")
# elif age > 3:
#     print("Teen")
# else:
#     print("Kid")

# Mini project
# first = input("Enter first number : ")
# operator = input("Enter operator (+ , -, *, /, %) : ")
# second = input ("Enter second number : ")

# if operator == '+':
#     print(int(first) + int(second))
# elif operator == '-':
#     print(int(first) - int(second))
# elif operator == '*':
#     print(int(first) * int(second))
# elif operator == '/':
#     print(int(first) / int(second))
# elif operator == '%':
#     print(int(first) % int(second))
# else :
#     print("Wrong choice !")

# range in python
# numbers = range(5)
# print(numbers)

# While loops in python.
# i = 1
# while i <= 5:
#     print(i * "*")
#     i += 1

# i = 5
# while i >= 0:
#     print(i * "*")
#     i = i - 1

# For loop in python
# for i in range(5):
#     print(i)

#  list data type in python
# marks = [95, 98, 97, 'Maths']
# print(marks)
# print(marks[0])
# print(marks[-1]) # Negative index
# print(marks[0:2])

# using for loop for marks list
# for score in marks:
#     print(score)

# marks = [95, 98, 97, 'Maths']
# marks.append(99)
# print(marks)
# marks.insert(0, 23)
# print(marks)

# print(99 in marks)
# print(100 in marks)

# print(len(marks))

# i = 0
# while i < len(marks):
#     print(marks[i])
#     i = i+1

# marks.clear()
# print(marks)

# Break and continue in python
students = ["ram", "shayam", "kishan", "radha", "radhika"]

# for student in students:
#     if student == "radha":
#         break
#     if student == "kishan":
#         continue
#     print(student)

# Tupple in python: same as list but inmutable
# marks = (95, 94, 93, 97, 97, 97)
# marks[0] = 99 # this will give error

# print(marks.count(97))
# print(marks.index(97))

# set in python  - no duplicates are allowed
# marks = {95, 94, 93, 97, 97, 97}

# print(marks)

# # print(marks[0]) # This will give error bcoz no index are allowed in sets. 

# for score in marks:
#     print(score)


# dic in python
# marks = {"eng":95, "chem":94, "maths":93, "phy":97, "phy":97, "phy":97}

# print(marks["chem"])
# marks["phy-edu"] = 99
# print(marks["phy-edu"])
# marks["phy"] = 100
# print(marks["phy"])
# print(marks)

# Functions in python
# 1. in-built function - int(), str(), len()
# 2. module functions - 

# import math
# print(dir(math))
# from math import sqrt
# print(sqrt(4))

# 3. user-defined function
# def function_name(parameter):
#     //do something

# def print_sum(first, second = 4):
#     print(first + second)

# print_sum(1, 4)
# print_sum(1)

# Finished