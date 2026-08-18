##ChatGPT Questions

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")


# print(f"Hello {name}")
# print(f"You are {age} years old")
# print(f"You live in {city}")

#################################################################################

# length = int(input("Enter the length: "))
# breadth = int(input("Enter the Breadth: "))

# area = length * breadth

# perimeter = 2 * (length + breadth)

# print(f"The area of rectangle is {area}.")
# print(f"The perimeter of rectangle is {perimeter}.")

#################################################################################

# n1 = int(input("Enter first number : "))
# n2 = int(input("Enter second number : "))

# n1 = n1 + n2
# n2 = n1 - n2
# n1 = n1 - n2

# print(f"After swapping: \n first number : {n1} \n second number: {n2}")

##########################  or  #################################################

# n1 = int(input("Enter first number : "))
# n2 = int(input("Enter second number : "))

# n1, n2 = n2, n1

# print(f"After swapping :\n first number = {n1}\n second number = {n2}")


#################################################################################


# temp = float(input("Enter the temperature in celsius: "))

# fheit = (9 /5) * temp + 32

# print(f"The temperature in fahrenheit is {fheit}.")


#################################################################################

# maths = int(input("Enter your maths marks : "))
# physics = int(input("Enter your physics marks : "))
# chemistry = int(input("Enter your chemistry marks : "))
# social_science = int(input("Enter your social_science marks : "))
# biology = int(input("Enter your biology marks : "))

# total = maths + physics + chemistry + social_science + biology

# average = total / 5

# print(f"Your total marks are : {total}")

# print(f"Your average is : {average}")

#################################################################################


# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# print(f"Welcome {first_name} {last_name}!" )

#################################################################################


# string = input("Enter the string: ")

# str_length = len(string)

# print(f"The length of string is {str_length}")

#################################################################################

# user_input = input("Enter the string: ")

# print(f"first letter is : {user_input[0]}")
# print(f"Last letter is : {user_input[-1]}")

#################################################################################

# input = input("Enter the string : ")

# print(input[::-1])


#################################################################################

# name = input("ENTER THE STRING : ") 

# middle = len(name) // 2 

# if len(name) % 2 == 0:
#     print(name[middle - 1])
# else:
#     print(name[middle])

#################################################################################


# num = int(input("ENTER THE NUMBER : "))

# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#################################################################################


# num = int(input("ENTER THE NUMBER : "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

#################################################################################

# num = int(input("ENTER THE NUMBER : "))

# if num % 5 == 0 and num % 11 == 0:
#     print("Divisible")
# else:
#     print("Not Divisible")

#################################################################################

# num = int(input("ENTER THE NUMBER : "))

# print(num % 10)

#################################################################################

# num = int(input("ENTER THE NUMBER : "))

# sqr = num ** 2

# cube = num ** 3

# print(f"{num}'s square is {sqr} & cube is {cube}")

#################################################################################


# num1 = int(input("ENTER FIRST NUMBER : "))
# num2 = int(input("ENTER SECOND NUMBER : "))

# if num1 > num2:
#     print(f"{num1} is a largest number.")
# elif num1 < num2:
#     print(f"{num2} is a largest number.")
# else:
#     print("Both numbers are equal.")

#################################################################################

# num1 = int(input("ENTER THE FIRST NUMBER : "))
# num2 = int(input("ENTER THE SECOND NUMBER : "))
# num3 = int(input("ENTER THE THIRD NUMBER : "))

# if num1 == num2 and num1 == num3 and num2 == num3 :
#     print("All three numbers are equal.")
# elif num1 >= num2 and num1 >= num3:
#     print(f"{num1} is the largest number.")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is the largest number.")
# else :
#     print(f"{num3} is the largest number.")


#################################################################################
    

# age = int(input("ENTER AGE : "))

# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")

#################################################################################


# year = int(input("ENTER YEAR : "))

# if year % 400 == 0 :
#     print(f"{year} is leap year ")
# elif year % 100 == 0 and year % 400 != 0:
#     print(f"{year} is not leap year ")
# elif year % 4 == 0 and year % 100 != 0:
#     print(f"{year} is leap year ")
# else:
#     print("Not leap year ")

#################################################################################


# marks = int(input("ENTER MARKS : "))


# if marks < 0 or marks > 100:
#     print("Invalid marks")
# elif marks >= 90 and marks <= 100:
#     print("you got A grade")
# elif marks >= 80 and marks <= 89:
#     print("you got B grade")
# elif marks >= 70 and marks <= 79:
#     print("you got C grade")
# elif marks >= 60 and marks <= 69:
#     print("you got D grade")

# else:
#     print("fail")

#################################################################################

# num1 = int(input("ENTER FIRST NUMBER: "))
# operator = input("ENTER  OPERATOR: ")
# num2 = int(input("ENTER SECOND NUMBER: "))

    
# if operator == "+":
#     result = num1 + num2
#     print(f"Result : {result}")

# elif operator == "-":
#     result = num1 - num2
#     print(f"Result : {result}")

# elif operator == "*":
#     result = num1 * num2
#     print(f"Result : {result}")
    
# elif operator == "/":
#     if num2 != 0:
#         result = num1 / num2
#         print(f"Result : {result}")
#     else:
#         print("cannot divide by zero")

# elif operator == "%":
#     if num2 != 0:
#         result = num1 % num2
#         print(f"Result : {result}")
#     else:
#         print("cannot divide by zero")

# else:
#     print("Invalid operator")

#################################################################################


# password = input("ENTER YOUR PASSWORD: ")

# if len(password) >= 8:
#     print("Strong password")
# else:
#     print("Weak password")

#################################################################################

# chr = input("ENTER CHARACTER: ")

# if chr == "a" or chr == "e" or chr == "i" or chr == "o" or chr == "u" or chr == "A" or chr == "E" or chr == "I" or chr == "O" or chr == "U":
#     print("Vowels")
# else:
#     print("Consonant") 

#################################################################################

# character = input("ENTER SINGLE CHARACTER : ")

# if character >= "A" and character <= "Z":
#     print("Uppercase")
# elif character >= "a" and character <= "z":
#     print("Lowercase")
# else:
#     print("Not an alphabet")

#################################################################################

# n = int(input("ENTER THE NUMBER : "))

# if n < 0:
#     n *= -1
#     print(n)
# else:
#     print(n)

#################################################################################

# cost_price = int(input("Enter cost price : "))
# selling_price = int(input("Enter selling price : "))

# if selling_price == cost_price:
#     print("No profit No loss")
# elif selling_price > cost_price:
#     print("Profit")
# else:
#     print("loss")

#################################################################################

# principal = int(input("Enter principal : "))
# rate = int(input("Enter rate : "))
# time =  int(input("Enter time : "))

# simple_interest = (principal * rate * time ) / 100

# print(simple_interest)

#################################################################################

# weight = float(input("Enter your weight (in kg): "))
# height = float(input("Enter your height (in m): "))

# bmi = weight / (height ** 2)

# if bmi < 18.5:
#     print(f"your BMI is {bmi}")
#     print("You are underweight")

# elif bmi >= 18.5 and bmi <= 24.9:
#     print(f"your BMI is {bmi}")
#     print("You are normal")

# elif bmi >= 25 and bmi <= 29.9:
#     print(f"your BMI is {bmi}")
#     print("You are overweight")
    
# else:
#     print(f"your BMI is {bmi}")
#     print("you are obese")

#################################################################################


# username = input("Enter your username : ")
# password = input("Enter your password : ")

# if username == "admin" and password == "python123":
#     print("Login successful")
# else:
#     print("Invalid credentials")

#################################################################################


#Print numbers from 1 to n
#For loop
# n = int(input("Enter number :  "))

# for i in range(1,n+1):
#     print(i)

#While loop
# n = int(input("ENTER NUMBER : "))

# i = 1

# while i <= n:
#     print(i)
#     i += 1

#################################################################################

# n = int(input("ENTER A NUMBER : "))

# i = 2

# while i <= n:
#     # if i % 2 == 0:
#     print(i)
#     i = i + 2

#################################################################################

# n = int(input("Enter number : "))

# i = 1

# sum = 0

# while i <= n:
#     sum = sum + i
#     i = i + 1

# print(f"sum is {sum}")

#################################################################################

# n = int(input("Enter the number whose table you want : "))

# for i in range(1,11):
#     result = n * i
#     print(f"{n} * {i} = {result}")

#################################################################################

# n = int(input("Enter a number whose factorial you want : "))

# fact = 1

# for i in range(n,0,-1):
#     fact = fact * i
    
# print(f"factorial of {n} is {fact}")

#################################################################################

# n = int(input("Enter number : "))

# count = 0 

# while n != 0:
#     n = n // 10 
#     count = count + 1

# print(f"Number of digits : {count}") 

#################################################################################

# n = int(input("ENTER NUMBER : "))

# sum = 0 

# while n != 0 :
#     rem = n % 10
#     sum = sum + rem
#     n = n // 10

# print(f"The sum of digits of number is {sum}")



#################################################################################


# n = int(input("ENTER NUMBER : "))

# r_num = 0

# while n != 0:
#     rem = n % 10
#     r_num = r_num * 10 + rem
#     n = n // 10

# print(f"Reverse Number : {r_num}")


#################################################################################


# n = int(input("ENTER NUMBER : "))

# copy = n

# r_num = 0

# while n != 0:
#     rem = n % 10
#     r_num = r_num * 10 + rem
#     n = n // 10

# if r_num == copy :
#     print("palindrome number")
# else:
#     print("Not palindrome")


#################################################################################

# n = int(input("ENTER NUMBER : "))

# print(f"Factors of {n} are :")
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

#################################################################################

# n = int(input("Enter number : "))

# count = 0 

# for i in range(1, n+1):
#       if n % i == 0:
#           count = count + 1

# if count == 2 :
#      print(f"{n} is prime number")
# else:
#      print(f"{n} is not prime number")

#################################################################################

# n = int(input("Enter number : "))

# for i in range(1,n+1):
#     num = i

#     count = 0 

#     for i in range(1, num+1):
#          if num % i == 0:
#               count = count + 1

#     if count == 2 :
#          print(f"{num} is prime number")
    

#################################################################################

# n = int(input("Enter number : "))

# sum = 0

# for i in range(1,n):
#     if n % i == 0:
#         sum = sum + i

# if sum == n:
#     print(f"{n} is perfect number")
# else:
#     print(f"{n} is not perfect number")

#################################################################################

# n =  int(input("Check number is armstrong or not (Enter 3 digit number only): "))

# copy = n

# total = 0

# while n != 0 :
#     rem = n % 10
#     cube = rem ** 3
#     total = total + cube
#     n = n // 10

# if total == copy:
#     print(f"{copy} is armstrong number")
# else:
#     print(f"{copy} is not armstrong number")

#################################################################################

# n = int(input("Enter number : "))

# previous = 0
# current = 1

# print(f"Fibonacci series of {n} : \n{previous}\n{current}")


# for i in range(2,n):
#     next = current + previous
#     print(next)
#     previous = current
#     current = next 

#################################################################################


# l = [12, 435, 67, 89, 23, 25, 69]

# greatest = l[0]
# sec_greatest = l[0]

# for i in range(0,len(l)):
#     if l[i] > greatest:
#        sec_greatest = greatest
#        greatest = l[i]

#     elif l[i] > sec_greatest:
#         sec_greatest = l[i]
    
# print(f"{greatest} is greatest & {sec_greatest} is 2nd greatest")

#################################################################################

# l = [12,13,14,15,16]

# for i in range(len(l) -1 ):
#     if l[i] < l[i+1]:
#         continue
#     else:
#         print("List is not sorted")
#         break
# else:
#     print("List is sorted")


########################################################################################################
### WEEK 1 - BASICS - VARIABLES , DATA TYPES, INPUT/OUTPUT, LOOPS, CONDITONALS 

# Q1. Write a Python program to swap two variables 

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# a = a + b 
# b = a - b 
# a = a - b

# print("After swapping :")
# print(f"first number : {a}")
# print(f"second number : {b}")

                        #OR

# a = int(input("Enter first number : "))
# b = int(input("Enter second number : "))

# Swap the variables in one line
# a, b = b, a

# print("After swapping :")
# print(f"first number : {a}")
# print(f"second number : {b}")

#########################################################################################################

# Q2. Take user input and display it back to the user

# user_input = input("Enter input : ")

# print(f"You entered : {user_input}")

#########################################################################################################

# # Q6. Convert temperature from Celcius to Fahrenheit

# celcius = float(input("Enter temperature in celcius : "))

# f = (celcius * 9/5) + 32

# print(f"{celcius} degree celcius in Fahrenheit is {f}")

#########################################################################################################

# # Q8. Create a program to count the number of vowels in a string.

# word = input("Enter the string : ")

# count = 0

# for i in range(0,len(word)):
#     if word[i] == "a" or word[i] == "A":
#         count = count + 1

#     elif word[i] == "e" or word[i] == "E":
#         count = count + 1

#     elif word[i] == "i" or word[i] == "I":
#         count = count + 1

#     elif word[i] == "o" or word[i] == "O":
#         count = count + 1

#     elif word[i] == "u" or word[i] == "U":
#         count = count + 1

# print(f"Total counts of vowels in string : {count}")

#########################################################################################################

# # Q11. Write a program to find the sum of first N natural numbers.

# n = int(input("Enter Number (Must be positive & Not a zero) : "))

# sum = 0

# for i in range(1,n+1):
#     sum = sum + i


# print(f"Sum upto {n} is {sum}")

#########################################################################################################

# Q12. Create a number guessing game.

# import random 

# random_number = random.randint(1,10)

# attempts =  0

# while True:
#     guess = int(input("Enter number : "))

#     attempts += 1

#     if guess > random_number:
#         print("Too high")
        

#     elif guess < random_number:
#         print("Too low")
        

#     else:
#         print("Congratulations !! you guessed it !!!")
#         print(f"You guessed the number in {attempts} attempts")
#         break

#########################################################################################################

### WEEK 2 - FUNCTIONS, LIST, TUPLE, SET, DICTIONARY
            
#1. Write a function to check if a number is even.

# def evenOrOdd():
#     n = int(input("Enter number : "))

#     if n % 2 == 0:
#         print(f"{n} is even")
#     else:
#         print(f"{n} is a odd")

# evenOrOdd()

#########################################################################################################

# 2. Create a list and find the sum of all its elements.

# ls = [1,2,3,4,2,5,1]

# total = 0

# for i in ls:
#     total += i

# print(total)

#########################################################################################################

# 3. Write a program to find the maximum and minimum in a list.

# ls = [12,41,25,45,100,20]

# minimum = ls[0]
# maximum = ls[0]


# for i in range(len(ls)):
#     if maximum < ls[i]:
#         maximum = ls[i]
#     elif minimum > ls[i]:
#         minimum = ls[i]
    
# print(f"{maximum} is maximum and {minimum} is minimum")

#########################################################################################################

# Q1. Write a function to check if a number is even
# def evenOrnot():
#     user_input = int(input("Enter number : "))

#     if user_input % 2 == 0:
#         print(f"{user_input} is an even number ")
#     else:
#         print(f"{user_input} is not an even number ")

# evenOrnot()

########################################################################################################

# Q2. Create a list and find the sum of all its elements.
# ls = [10,20,40,40]

# total = 0

# for num in ls:
#     total += num

# print(f"{total} is sum of all elements")

########################################################################################################

# Q3. Write a program to find the maximum and minimum in a list.
# ls = [123,458,254,365,203]

# maximum = ls[0]
# minimum = ls[0]

# for num in ls:
#     if num > maximum:
#         maximum = num
#     elif num < minimum:
#         minimum = num

# print(f"{maximum} is maximum & {minimum} is minimum")

########################################################################################################

# Q4. Create a program that removes duplicates from a list.
# ls = [1, 2, 2, 4, 3, 1, 5, 1]

# new_list = []

# for num in ls:
#     for i in new_list:
#         if i == num:
#             break
#     else: 
#         new_list.append(num)

# print(f"After removing duplicates new list is :\n{new_list}")

########################################################################################################

# Q5. Write a function to reverse a list
# def reverseList():
#     ls = [14, 24, 44, 34, 54, 64]

#     rev_ls = []

#     for i in range(len(ls) - 1, -1, -1):
#         rev_ls.append(ls[i])

#     print(f"reversed list is {rev_ls}")

# reverseList()

##########################################   OR   #####################################################
#Correct Way
# def reverseList(ls):
#     rev_ls = []

#     for i in range(len(ls) - 1, -1, -1):
#         rev_ls.append(ls[i])

#     print(f"reversed list is {rev_ls}")


# numbers = [10, 20, 54, 41, 12, 58, 86]

# reverseList(numbers)

########################################################################################################
# Q6. Create a tuple and access its elements.

# tp = (10, 20, 40, 40, 50)

# for num in tp:
#     print(num)

########################################################################################################
# Q7. Convert a list into a tuple and vice versa.

# ls = [10, 2, 3, 40, 58]

# my_tp = tuple(ls)     #tuple constructor

# print(f"List converted to tuple : {my_tp}")

# new_ls = list(my_tp)     #list constructor

# print(f"Tuple converted to list : {new_ls}")

########################################################################################################
#  Q8. Write a program to merge two dictionaries.
# d1 = {
#     1:10,
#     2:20,
#     3:30,
#     4:40 
# }

# d2 = {
#     5:50,
#     6:60,
#     7:70,
#     8:80 
# }

# for i in d2:
#     d1[i] = d2[i]

# print(f"After merging d1 dictionary is :- \n{d1}")

########################################################################################################
# # 9. Write a function to count the frequency of elements in a list.
# def countFreqOfElement(ls):

#     freq = {}

#     for element in ls:
#         if element in freq:
#             freq[element] = freq[element] + 1
#         else:
#             freq[element] = 1
        
#     print(f"frequency of element in list: \n{freq}")
        
# # lst = [10, 20, 10, 30, 20, 10]

# lst = [1, 2, 2, 2, 5, 4, 5, 5, 8, 4, 1, 2, 1, 2, 5, 6, 6, 3, 3]

# countFreqOfElement(lst)

########################################################################################################
# # Q10. Create a dictionary of squares of numbers from 1 to 10.
# d1 = {}

# for i in range(1,11,1):
#     d1[i] = i ** 2

# print(f"Dictionary of squares from 1 to 10 : \n{d1}")

########################################################################################################
# Q11. Write a program to sort a list in ascending order.

########################################################################################################
# Q12. Create a program to check if a key exists in a dictionary.

# d1 = {
#     "name" : "Kalpesh",
#     "age" : 22,
#     "role" :"AI engineer",
# }

# key = input("Enter the key : ")

# if key in d1:
#     print(f"{key} is present in dictionary")
# else:
#     print(f"{key} is not present in dictionary")

########################################################################################################
# # Q13. Create a set and perform union, intersection, and difference

# s1 = {12, 12, 14, 15, 16, 16, 18, 15, 16}
# s2 = {15, 16, 17, 18, 14, 12, 13, 18, 19}

# union = s1 | s2
# print(union)

# intersection = s1 & s2
# print(intersection)

# difference = s2 - s1
# print(difference)

# symmetric_difference = s1 ^ s2
# print(symmetric_difference)

########################################################################################################
# Q14. Write a function to find common elements in two lists.

# def commonElementsInList(ls1, ls2):
#     common = []

#     for element in ls1:
#         if element in ls2:
#             if element in common:
#                 continue
#             else:
#                 common.append(element)
    
#     return common


# l1 = [10, 20, 20, 40]
# l2 = [20, 40, 50, 60]



# result = commonElementsInList(l1, l2)

# print(f"Common elements in list {result}")

#####################################  Better approach   ###############################################

# def common_elements_in_lists(l1, l2):
#     new_l1 = set(l1)
#     new_l2 = set(l2)

#     common = new_l1 & new_l2

#     common_elements = list(common)
                           
#     return common_elements 


# ls1 = [10, 20, 30]
# ls2 = [10, 20, 40, 50]

# result = common_elements_in_lists(ls1, ls2)

# print(f"Common elements in lists are : {result}")

########################################################################################################
# Q15. Write a function that returns the factorial of a number

# def factorial_of_number(num):
#     fact = 1

#     if num < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")

#     for i in range(num, 0, -1):
#         fact *= i

#     return fact

# user_input = int(input("Enter your number : "))

# result = factorial_of_number(user_input)

# print(f"factorial of {user_input} is {result}")

########################################################################################################
# Q16. Create a function that checks whether a string is a palindrome.

# def palindrome_or_not(word):
#     rev_string = ""

#     for i in range(len(word) - 1, -1, -1):
#         rev_string += word[i]

#     if rev_string == word:
#         return "String is palindrome"
#     else:
#         return "String is not palindrome"

    
# user_input = input("Enter your string : ").lower()

# result = palindrome_or_not(user_input)

# print(result)

########################################################################################################
# # Q17. Write a function to count vowels in a string.

# def count_vowels(word):
#     count = 0

#     for i in word:
#         if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
#             count += 1

#     return count


# user_input = input("Enter string : ").lower()

# result = count_vowels(user_input)

# print(f"There are {result} vowels in string")

########################################################################################################
# 18. Create a dictionary and iterate over its keys and values.
# d1 = {
#     "Name" : "Kalpesh",
#     "Age" : 22,
#     "Role" : "AI Engineer",
#     10 : 40,
#     11 : 11,
#     28 : 78
# }

# print("Keys in dictionary are : ")
# for keys in d1.keys():
#     print(keys)

# print("Values in dictionary are : ")
# for values in d1.values():
#     print(values)


# #Both keys & values
# print("Keys & Values in dictionary : ")
# for i, j in d1.items():
#     print(f"{i} : {j}")

########################################################################################################
# 19. Write a function to remove all punctuation from a string.
# def remove_punctuation(text):
#     punctuations = """~`!@#$%^&*()_-+={}[]|\\/:;"'<>,.?"""

#     result = ""

#     for char in text:
#         if char not in punctuations:
#             result += char

#     return result

# user_input = input("Enter your string :")

# output = remove_punctuation(user_input)

# print(f"String after removing punctuation is :\n{output}")

########################################################################################################
# 20. Write a function to capitalize the first letter of each word in a string.

# def capitalize_the_string(text):
#     updated_text = ""

#     for i in range(len(text)):
#         if i == 0:
#             updated_text += text[i].upper()
#         elif text[i - 1] == " ":
#             updated_text += text[i].upper()
#         else:
#             updated_text += text[i]

#     return updated_text


# user_input = input("Enter string : ")

# result = capitalize_the_string(user_input)

# print(f"Updated string is : {result}")

########################################################################################################
# 22. Write a function to check if two strings are an anagram.

# def is_anagram(str1, str2):
#     if len(str1) != len(str2):
#         return f"{str1} & {str2} are not anagram"
    
#     d1 = {}
#     d2 = {}

#     for i in range(len(str1)):
#         if str1[i] not in d1:
#             d1[str1[i]] = 1
#         else:
#             d1[str1[i]] = d1[str1[i]] + 1


#     for j in range(len(str2)):
#         if str2[j] not in d2:
#             d2[str2[j]] = 1
#         else:
#             d2[str2[j]] = d2[str2[j]] + 1


#     if d1 == d2:
#         return f"{str1} & {str2} are anagram"
#     else:
#         return f"{str1} & {str2} are not anagram"


# user_input1 = input("Enter first string : ")
# user_input2 = input("Enter second string : ")

# result = is_anagram(user_input1, user_input2)

# print(result)

########################################################################################################
# 23. Create a nested dictionary to represent student records.

# dictionary = {
#    "students" : {
#        "kalpesh" : {
#            "math" : 98,
#            "science" : 99,
#            "physics" : 95,
#            "chemistry" : 96
#        },

#        "sanika" : {
#            "biology" : 100,
#            "physics" : 98,
#            "chemistry" : 97,
#            "science" : 95
#        },

#        "bhanvase" : {
#            "english" : 97,
#            "marathi" : 98,
#            "hindi" : 96,
#            "science" : 95
#        }
#    }
# }

# print(dictionary)

########################################################################################################
# 24. Write a function to flatten a nested list.

# def convert_to_flatten(ls):
#     flatten_list = []

#     for element in ls:
#         if type(element) == list:
#             for ch in element:
#                 flatten_list.append(ch)
#         else:
#             flatten_list.append(element)


#     return flatten_list

# list1 = [1, 2, [3, 4], [5, 6]]

# result = convert_to_flatten(list1)

# print(f"flatten_list is : {result}")

########################################################################################################
# 25. Write a program to find the second highest number in a list.

# ls = [1, 2, 3, 4, 5]

# highest = ls[0]
# sec_highest = ls[0] 

# for i in range(len(ls)):
#     if ls[i] > highest:
#         sec_highest = highest
#         highest = ls[i]

#     elif ls[i] > sec_highest:
#         sec_highest = ls[i]

# print(f"second highest number in list : {sec_highest}")

########################################################################################################
# 26. Create a function to rotate a list left by k positions.

# def rotate_list_by_k_position(k, l1):
    
#     l2 = []

#     if type(l1) != list:
#         raise TypeError("Please provide list..")
    
#     for i in range(k, len(l1)):
#         l2.append(l1[i])
#         # l1.remove(l1[i])

#     for i in range(k):
#         l2.append(l1[i])

#     return l2

# value_of_k = int(input("Enter the value of k : "))

# ls = [22, 44, 55, 88, 99]

# result = rotate_list_by_k_position(value_of_k, ls)

# print(f"Rotated list is : {result}")

########################################################################################################
# 27. Write a function to find the missing number from a list of 1 to N.

# def find_missing_value(ls, n):
#     for i in range(1,n+1):
#         if i not in ls:
#             return i
        

# l = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20]

# result = find_missing_value(l, 20)

# print(f"Missing value in list : {result}")

########################################################################################################
# # 28. Write a program to remove all None values from a list.

# ls = [None,10, 20, None, 25, 45, None, 40, None]

# ls1 = []

# for element in ls:
#     if element is not None:
#         ls1.append(element)

# print(f"list after removing None values : {ls1}")

########################################################################################################
# 29. Write a function to merge two dictionaries and handle key collisions by summing values.

# def merging_two_dictionaries(d1, d2):
#     for element in d2:
#         if element not in d1:
#             d1[element] = d2[element]
#         else:
#             d1[element] = d2[element] + d1[element]

#     return d1

# dc1 = {10:100, 20:200, 30:300}
# dc2 = {40:400, 50:500, 60:600, 30:200, 10: 11, 20:22}

# result = merging_two_dictionaries(d2 = dc2, d1 = dc1)

# print(f"final dictionary : {result}")

########################################################################################################
# # 30. Create a function to find unique elements present in only one of two lists.

# def find_unique_elements(ls1, ls2):
#     new_ls1 = set(ls1)
#     new_ls2 = set(ls2)

#     unique_elements = new_ls1 ^ new_ls2

#     return unique_elements

# l1 = [1, 2, 3, 4, 5]
# l2 = [4, 5, 6, 7, 8]

# result = find_unique_elements(l1, l2)

# print(f"Unique elements present in only one list are :{result}")

##################################################  OR   ######################################################

# def find_unique_elements(ls1, ls2):
#     unique_elements = []

#     for element in ls1:
#         if element not in ls2:
#             unique_elements.append(element)

#     for item in ls2:
#         if item not in ls1:
#             unique_elements.append(item)

#     return unique_elements

# l1 = [1,2,3,4,5]
# l2 = [4,5,6,7,8]

# result = find_unique_elements(l1, l2)

# print(f"Unique elements present in only one list are :{result}")

########################################################################################################
# # Q. Write a Python program to sum all the values in a dictionary?

# d1 = {10: 10, 20:200, 30:300, 40:4, 50: 4, 45: 800}

# total = 0 

# for i in d1:
#     total += d1[i]

# print(f"Sum of all values in dictionary is {total}")

########################################################################################################
# Week 3: File Handling, Error Handling,
# Q1. Write a Python script to read a file and print its contents.

# with open("bio_data.txt") as f:
#     data  = f.read()
#     print(data)

########################################################################################################
# Q2. Create a file and write your name into it.

# with open("my_name.txt","w") as f:
#     data = "My name is Kalpesh Bapurao Bhanvase" 
#     f.write(data)

########################################################################################################
# Q3. Handle a ZeroDivisionError using try-except

# def division(a,b):
#     return a /  b

# try:
#     print(division(10,0))
# except ZeroDivisionError as err:
#     print(err)

########################################################################################################
# # Q4. Write a program to handle file not found error.

# try:
#     with open("Bunny.txt", "r") as f:
#         print(f.read())

# except FileNotFoundError as err:
#     print(err)

########################################################################################################
# Q8. Create a program to count lines and words in a file.

# with open("dummy.txt", "r") as f:
#         line_count = 0
#         word_count = 0
#         for line in f:
#             line_count += 1
#             words = line.split()
#             word_count += len(words)

#         print(f"{line_count} words in file")
#         print(f"{word_count} lines in file")

########################################################################################################
# Q9. Write a program to read a CSV file and print its contents.

# with open(r"C:\Users\ADMIN\Downloads\student_data.csv") as f:
#     print(f.read())

########################################################################################################
# Q10. Handle multiple exceptions in a single try block.
# print("1 for reading the file")
# print("2 for perform the division")
# print("3 for import module")

# try:
#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         with open("esfjkdc") as f:
#             f.read()

#     elif choice == 2:
#         num1 = 10
#         num2 = 0
#         result = num1 / num2
#         print(result)

#     elif choice == 3:
#         from something import nothing

#     else:
#         print("Invalid Choice! Please enter 1, 2 or 3")

# except ZeroDivisionError as err:
#     print(err)

# except FileNotFoundError as err:
#     print(err)

# except ModuleNotFoundError as err:
#     print(err)

# except ValueError as err:
#     print(err)

########################################################################################################
# Q1. Write a program that:

# Opens data.txt in read mode.
# Reads and prints its contents.
# Handles FileNotFoundError.
# Uses with open() so the file is automatically closed.

# try:
#     with open("data.txt") as f:
#         print(f.read())
# except FileNotFoundError as err:
#     print(err)

########################################################################################################

# Q2. Write a program that:

# Takes two numbers from the user.
# Divides the first by the second.
# Handles:
# ValueError if the user enters something that isn't a number.
# ZeroDivisionError if the second number is 0.
# Uses else to print the result only when no exception occurs.
# Uses finally to print "Program finished".


# try:
#     num1 = int(input("Enter first number : "))
#     num2 = int(input("Enter second number : "))

#     result = num1 / num2

# except ValueError as err:
#     print(err)

# except ZeroDivisionError as err:
#     print(err)

# else:
#     print(result)

# finally:
#     print("PROGRAM FINISHED")

########################################################################################################
# Q3. Write a program that opens notes.txt and:

# Reads all lines.
# Prints the total number of lines.
# Handles FileNotFoundError.
# Handles any unexpected exception using a general Exception.

# Bonus: Print the exception message.


# try:
#     with open("notes.txt") as f:
#         data = f.readlines()
#         count = len(data)
#         print(f"Total number of lines in notes.txt are {count}")

# except FileNotFoundError as err:
#     print(err)

# except Exception as err:
#     print(err)

########################################################################################################

# Q4. Ask the user to enter:

# Name
# Age
# City

# Store the information in user_data.txt.

# Your program should:

# Open the file in write mode.
# Write the information.
# Handle possible exceptions.
# Confirm that the data was successfully written using else.
# Print a completion message using finally.

# try:
#     name = input("Enter your name : ")
#     age = int(input("Enter your age : "))
#     city = input("Enter your city : ")


#     with open("user_data.txt", "w") as f:
#         f.write(f"Name : {name}\n")
#         f.write(f"Age : {age}\n")
#         f.write(f"City : {city}")

# except ValueError as err:
#     print(err)

# except FileNotFoundError as err:
#     print(err)

# except Exception as err:
#     print(err)

# else:
#     print("Data successfully written")

# finally:
#     print("Task Completed")

########################################################################################################
# Q5. Simple file manager

# Create a menu:

# 1. Read file
# 2. Write to file
# 3. Append to file
# 4. Exit

# Depending on the user's choice:

# 1 → Read data.txt
# 2 → Overwrite data.txt
# 3 → Add content to the end of data.txt
# 4 → Exit

# Handle:

# Invalid menu input
# FileNotFoundError
# ValueError
# Other unexpected exceptions


# try:
#     print("1. Read File")
#     print("2. Write to File")
#     print("3. Append to File")
#     print("4. Exit")

#     choice = int(input("Enter Your choice : "))

#     if choice == 1:
#         with open("data.txt", "r") as f:
#             print(f.read())

#     elif choice == 2:
#         content = input("Enter content : ")
#         with open("data.txt", "w") as f:
#             f.write(content)

#     elif choice == 3:
#         content = input("Enter content : ")
#         with open("data.txt", "a") as f:
#             f.write(f"\n{content}")

#     elif choice == 4:
#         print("Exiting from file menu")

#     else:
#         print("Invalid menu input")

# except FileNotFoundError as err:
#     print(err)

# except ValueError as err:
#     print(err)

# except Exception as err:
#     print(err)

########################################################################################################

# Q6. Copy one file into another

# Write a program that:

# source.txt → destination.txt

# The program should:

# Open source.txt.
# Read its contents.
# Create/overwrite destination.txt.
# Write the contents into it.
# Handle the situation where the source file doesn't exist.
# Handle other possible exceptions.

# Bonus: Display how many characters were copied.

# try:
#     with open("source.txt", "r") as f:
#         content = f.read()
#         character = len(content)

#     with open("Destination.txt", "w") as f1:
#         f1.write(content)


# except FileNotFoundError as err:
#     print(err)

# except PermissionError as err:
#     print(err)

# except Exception as err:
#     print(err)

# else:
#     print(f"No of character were copied are {character}")
#     print("Successfully file Copied!!!")

########################################################################################################

# 7. File-based calculator

# Create a file called numbers.txt containing numbers like:

# 10
# 20
# 30
# abc
# 40
# 0
# 50

# Write a program that:

# Reads the file line by line.
# Converts each line to an integer.
# Calculates the sum.
# Ignores invalid lines such as "abc".
# Handles ValueError for invalid numbers.
# Handles FileNotFoundError.
# Prints the final sum.

# Bonus: Also count:

# Valid numbers
# Invalid numbers



# total = 0
# valid_count = 0
# invalid_count = 0

# try:
#     with open("numbers.txt", "r") as f:
#         for line in f:
#             try:
#                 number = int(line)
#                 total += number
#                 valid_count += 1

#             except ValueError as err:
#                 invalid_count += 1
   
# except FileNotFoundError as err:
#     print(err)

# print(f"Final sum is {total}")
# print(f"Valid numbers : {valid_count}")
# print(f"Invalid Numbers : {invalid_count}")
    
########################################################################################################

# 8. Search for a word in a file

# Ask the user:

# Enter a word to search:

# Then search for that word in article.txt.

# Print:

# Word found

# or

# Word not found

# Also print the number of times the word appears.

# Handle:

# File not found
# Empty file
# Invalid input

# Bonus: Make the search case-insensitive.

# count = 0

# try:
#     user_word = input("Enter a word to search : ").lower()

#     if user_word == "":
#         user_word = input("Please enter word : ")

#     else:
#         with open("Article.txt", "r") as f:
#             content = f.read().lower()

#             if not content:
#                 print("File is empty")
#             else:
#                 words = content.lower().split()
#                 count = words.count(user_word)

#             if count > 0:
#                 print("Word found")
#             else:
#                 print("Word not found")

#         print(f"{count} times word appears")

# except FileNotFoundError as err:
#     print(err)

########################################################################################################

# 9. Student records system

# Create a program that stores student information in a file:

# 101,Kalpesh,85
# 102,Rahul,72
# 103,Priya,91

# Create a menu:

# 1. Add student
# 2. Display all students
# 3. Search student by ID
# 4. Exit

# Requirements:

# Store records in students.txt.
# When adding a student, validate the ID and marks.
# Handle invalid numeric input with ValueError.
# Handle missing files with FileNotFoundError.
# When searching, display "Student not found" if the ID doesn't exist.
# Use with open() for every file operation.
# Don't let one bad input crash the entire program.


# print("Menu : ")
# print("1. Add Student")
# print("2. Display all students")
# print("3. Search student by ID")
# print("4. Exit")


# try:

#     choice = int(input("Enter your choice : "))


#     if choice == 1:
#         student_id = int(input("Enter Student's ID : "))
#         student_name = input("Enter Student's name : ")
#         student_marks = int(input("Enter Student's marks : "))

#         with open("Students.txt", "a") as f:
#             f.write(f"{student_id},{student_name},{student_marks}\n")
        
#     elif choice == 2:
#         with open("Students.txt", "r") as f:
#             print(f.read())

#     elif choice == 3:
#         search = input("Enter ID to search student : ")
#         with open("Students.txt", "r") as f:
#             content = f.read()
#             for line in f:
#                 if search not in content:
#                     print("Student not found")
#                 else:
#                     print(line)
#                     break

#     elif choice == 4:
#         print("Exit")

#     else:
#         print("Invalid Choice")
    

# except ValueError as err:
#     print(err)

# except FileNotFoundError as err:
#     print(err)

# except Exception as err:
#     print(err)

########################################################################################################

# 10. Create a file called server.log:

# INFO: Server started
# ERROR: Database connection failed
# INFO: User logged in
# WARNING: Low memory
# ERROR: File not found
# INFO: User logged out
# ERROR: Database connection failed

# Write a program that:

# Opens the file.
# Reads it line by line.
# Counts:
# INFO
# WARNING
# ERROR
# Displays something like:
# INFO: 3
# WARNING: 1
# ERROR: 3
# Creates a new file called errors.txt.
# Stores only ERROR lines in it.
# Handles:
# FileNotFoundError
# PermissionError
# Unexpected exceptions
# Uses try-except-else-finally.
# Uses with open() wherever appropriate.

# Bonus challenge: Ask the user for a keyword and find how many times that keyword appears in the log.


########################################################################################################
# NOTE -- Q8, Q9, Q10  Not solved of Exeption handling & File handling 

########################################################################################################
