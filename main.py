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
###     OOPs in Python (Object-Oriented-Programming in Python)
##      Classes, Objects & Constructor

# Q1. Create a Student class

# Create a class Student with:

# name
# age
# course

# Create one object and display all its information.

# Answer - 
# class Student:
#     name = "Kalpesh"
#     age = 18
#     course = "Computer Science CS"

# obj = Student()

# print(f"Student's name = {obj.name}")
# print(f"Student's age = {obj.age}")
# print(f"Student's course = {obj.course}")

########################################################################################################
# Q2. Create a Car class

# Create a class Car with attributes:

# brand
# model
# color

# Create two objects with different values and display their information.

# Answer -
# class Car:
#     def __init__(self, brand, model, color):
#         self.brand = brand
#         self.model = model
#         self.color = color

#     def show(self):
#         print(f"Brand :- {self.brand}")
#         print(f"Model :- {self.model}")
#         print(f"Color :- {self.color}")

# hyundai = Car("Hyundai", "SX (Dark Knight)", "Black")
# tata = Car("Tata", "Sierra Ev", "Black")

# hyundai.show()
# print("---------------------------------------")
# tata.show()

########################################################################################################
# Q3. Create a Book class with constructor

# Create a class Book with a constructor that accepts:

# title
# author
# price

# Create an object and display the book details.

# Answer - 
# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def display(self):
#         print("Book Details :- ")
#         print(f"Title :- {self.title}")
#         print(f"Author :- {self.author}")
#         print(f"Price :- {self.price}")


# book1 = Book("Engineering Mathematics IV", "J.V.Kumbhojkar", 500)
# book1.display()

########################################################################################################
# Q4. Create a Mobile class

# Create a class Mobile with:

# brand
# model
# price

# Add a method display() that prints all the details.

# Create two objects and call the method for both.


# Answer - 
# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display(self):
#         print("Mobile Detail : ")
#         print(f"Brand : {self.brand}")
#         print(f"Model : {self.model}")
#         print(f"Price : {self.price}")

# samsung = Mobile("Samsung", "S26 ultra", 135000)
# apple = Mobile("Apple", "iphone 17 pro max", 130000)
# samsung.display()
# print("-----------------------------------------")
# apple.display()

########################################################################################################
# Q5. Create an Employee class

# Create a class Employee with a constructor that accepts:

# name
# salary

# Create three employee objects and display their details.


# Answer - 
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def details(self):
#         print("Details : ")
#         print(f"Name : {self.name}")
#         print(f"Salary : ₹{self.salary:,}")

# kalpesh = Employee("Kalpesh", 70000)
# sanika = Employee("Sanika", 80000)
# bunny = Employee("Bunny", 100000)

# kalpesh.details()
# print("..........................")
# sanika.details()
# print("..........................")
# bunny.details()

########################################################################################################
# Q6. Student Marks

# Create a Student class with a constructor accepting:

# name
# marks

# Create a method display_result() that prints:

# Name: Rahul
# Marks: 85
# Result: Pass

# Consider a student Pass if marks >= 40.

# Create at least 3 student objects.


# Answer -
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def display_result(self):
#         print(f"Name : {self.name}")
#         print(f"Marks : {self.marks}")

#         if self.marks >= 40:
#             print(f"Result : Pass")
#         else:
#             print(f"Result : Fail")

# rahul = Student("Rahul", 59)
# shreedhar = Student("Shreedhar", 69)
# kalpesh = Student("Kalpesh", 39)

# rahul.display_result()
# print("<---------------------------->")
# shreedhar.display_result()
# print("<---------------------------->")
# kalpesh.display_result()

########################################################################################################
# Q7. Bank Account

# Create a BankAccount class with a constructor accepting:

# account_holder
# balance

# Create methods:

# deposit(amount)
# withdraw(amount)
# display_balance()

# Rules:

# Deposit should increase the balance.
# Withdrawal should decrease the balance.
# Don't allow withdrawal if the amount is greater than the balance.

# Create an object and perform multiple operations.


# Answer -
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Deposit amount must be greater than 0")


#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be greater than 0")
#         elif amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -= amount

#     def display_balance(self):
#         print(f"Current Balance : {self.balance}")

# kalpesh = BankAccount("Kalpesh", 100000)
# kalpesh.deposit(10000) 
# kalpesh.withdraw(600000)
# kalpesh.display_balance()

########################################################################################################
# Q8. Rectangle

# Create a Rectangle class with a constructor accepting:

# length
# width

# Create methods:

# area()
# perimeter()

# Create two rectangle objects with different dimensions and display their area and perimeter.


# Answer -
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         area = self.length * self.width
#         return area

#     def perimeter(self):
#         perimeter = 2 * (self.length + self.width)
#         return perimeter

# print("Object 1")
# obj1 = Rectangle(12, 12)
# print(f"Area of rectangle : {obj1.area()}")
# print(f"Perimeter of rectangle : {obj1.perimeter()}")

# print("---------------------------------------------")

# print("Object 2")
# obj2 = Rectangle(22, 25)
# print(f"Area of rectangle : {obj2.area()}")
# print(f"Perimeter of rectangle : {obj2.perimeter()}")

########################################################################################################
# Q9. Product

# Create a Product class with:

# name
# price
# quantity

# Use a constructor to initialize these values.

# Create a method:

# total_price()

# which returns:

# price × quantity

# Create three product objects and find the total price of each.


# Answer -
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def total_price(self):
#         return self.price * self.quantity


# shampoo = Product("Shampoo", 50, 200)
# pen = Product("Pen", 44, 400)
# laptop = Product("Laptop", 122, 63)

# print(f"{shampoo.name} Total Price : {shampoo.total_price()}")
# print(f"{pen.name} Total Price : {pen.total_price()}")
# print(f"{laptop.name} Total Price : {laptop.total_price()}")

########################################################################################################
# Q10. Employee Salary

# Create an Employee class with:

# name
# salary
# department

# Use a constructor to initialize them.

# Create a method display().

# Also create a method:

# annual_salary()

# which returns the employee's yearly salary.

# Create at least 3 employees.


# Answer -
# class Employee:
#     def __init__(self, name, salary, department):
#         self.name = name
#         self.salary = salary
#         self.department = department

#     def display(self):
#         print(f"Employee's name : {self.name}")
#         print(f"Salary : {self.salary}")
#         print(f"Department : {self.department}")

#     def annual_salary(self):
#         return self.salary * 12


# ezio = Employee("Ezio", 75000, "IT")
# hela = Employee("Hela", 65000, "Consulting")
# killer = Employee("killer", 78000, "CS")

# ezio.display()
# print(f"Annual salary : {ezio.annual_salary()}")
# print("------------------------------------------")
# hela.display()
# print(f"Annual salary : {hela.annual_salary()}")
# print("-------------------------------------------")
# killer.display()
# print(f"Annual salary : {killer.annual_salary()}")

########################################################################################################
# Q11. Library Book System

# Create a Book class with:

# title
# author
# price
# available

# Use a constructor to initialize the values.

# Create methods:

# display()
# borrow_book()
# return_book()

# Rules:

# If the book is available, borrow_book() should make it unavailable.
# If it is already borrowed, display an appropriate message.
# return_book() should make it available again.

# Create at least 3 book objects and test different operations.


# Answer -
# class Book:
#     def __init__(self, title, author, price, available):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.available = available.lower()


#     def display(self):
#         print("Book Details : ")
#         print(f"Title : {self.title}")
#         print(f"Author : {self.author}")
#         print(f"Price : {self.price}")
#         print(f"Available : {self.available}")

#     def borrow_book(self):
#         if self.available == "yes":
#             self.available = "no"
#         else:
#             print(f"{self.title}'s book is Not Available")

        
#     def return_book(self):
#         if self.available == "no":
#             self.available = "yes"
#         else:
#             print(f"{self.title} is already available")

# book1 = Book("Engineering Mathemarics IV", "G.V.kumbhojkar", 500, "YES")
# book2 = Book("Mechaninc", "Dr. Dhananjay Wankhede", 200, "No")
# book3 = Book("Social Media Analytics", "Renuka Sanga", 1500, "yes")

# book1.display()
# print("-----------------------")
# book2.display()
# book2.borrow_book()
# print("-----------------------")
# book3.display()
# book3.return_book()

########################################################################################################
# Q12. Bank Account System

# Create a BankAccount class with:

# account_number
# holder_name
# balance

# Methods:

# deposit(amount)
# withdraw(amount)
# display_account()

# Rules:

# Deposit amount must be greater than 0.
# Withdrawal amount must be greater than 0.
# Withdrawal cannot exceed the balance.

# Create two bank account objects and perform different transactions on each.

# Challenge: Make sure changing one account does not affect the other account.


# Answer - 
# class BankAccount:
#     def __init__(self, account_number, holder_name, balance):
#         self.account_number = account_number
#         self.holder_name = holder_name
#         self.balance = balance

#     def display_account(self):
#         print("Account Details : ")
#         print(f"Name : {self.holder_name}")
#         print(f"Account Number : {self.account_number}")
#         print(f"Balance : {self.balance}")


#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#         else:
#             print("Amount must be greater than 0")


#     def withdrawal(self, amount):
#         if amount <= 0:
#             print("Amount must be greater than 0")
#         elif amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Balance")


# kalpesh = BankAccount("1245", "Kalpesh", 35600)
# kalpesh.deposit(50000)
# kalpesh.display_account()
# print("-----------------------------------------")
# sanika = BankAccount("4567", "Sanika", 60000)
# sanika.withdrawal(8050)
# sanika.display_account()

########################################################################################################
# Q13. Shopping Cart

# Create a Product class with:

# name
# price

# Create a ShoppingCart class.

# The cart should be able to:

# add_product()
# remove_product()
# display_cart()
# calculate_total()

# Create multiple Product objects and add them to the shopping cart.

# For example:

# Laptop → ₹50000
# Mouse → ₹1000
# Keyboard → ₹2000

# The cart should calculate:

# Total = ₹53000 


# Answer -
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class ShoppingCart:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)
#         print("Product Added successfully.")


#     def display_cart(self):
#         cart_items = {}
#         for product in self.products:
#             cart_items[product.name] = product.price

#         print(f"Cart : {cart_items}")

#     def calculate_price(self):
#         total = 0
#         for product in self.products:
#             total += product.price

#         print(f"Total Price : {total}")
        

#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)
#             print("Product Removed successfully.")
#         else:
#             print("Product not found in cart")


# cart = ShoppingCart()
# keyboard = Product("Ant Esports mk500 pro", 1229)
# laptop = Product("Lenovo loq", 75000)
# mouse = Product("Apple Mini mouse", 5000)
# ipad = Product("One plus 9pro", 4520)
# cart.add_product(laptop)
# cart.add_product(keyboard)
# cart.add_product(mouse)
# cart.add_product(ipad)
# cart.remove_product(ipad)
# cart.display_cart()
# cart.calculate_price()

########################################################################################################
# Q14. Student Result System

# Create a Student class with:

# name
# roll_number
# marks

# Use a constructor.

# Create methods:

# calculate_total()
# calculate_percentage()
# display_result()

# Rules:

# Store marks for 5 subjects.
# Calculate total marks.
# Calculate percentage.
# Display whether the student passed or failed.
# Assume the student must score at least 40 in every subject to pass.

# Create at least 3 student objects.

# Challenge: Display the student with the highest percentage.


# Answer - 

# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         if len(marks) == 5:
#             self.marks = marks
#         else:
#             print("Please enter  marks of 5 subjects")

#     def calculate_total(self):
#         total = 0 
#         for score in self.marks:
#             total += score

#         return total

#     def calculate_percentage(self):
#         total = self.calculate_total()        
#         percentage = (total / 500) * 100
#         # print(f"Percentage : {percentage}")
#         return percentage


#     def display_result(self):
#         for marks in self.marks:
#             if marks >= 40:
#                 continue
#             else:
#                 print("Student Failed")
#                 break
#         else:
#             print("Student Passed")

# kalpesh = Student("Kalpesh", 5, [50, 55, 45, 75, 85])
# print(kalpesh.calculate_total())
# kalpesh.calculate_percentage()
# kalpesh.display_result()
# print("--------------------------------------------------")
# sanika = Student("Sanika", 6, [45, 60, 58, 85, 90])
# print(sanika.calculate_total())
# sanika.calculate_percentage()
# sanika.display_result()
# print("--------------------------------------------------")
# bunny = Student("Bunny", 7, [75, 78, 38, 75, 90])
# print(bunny.calculate_total())
# bunny.calculate_percentage()
# bunny.display_result()
# print("--------------------------------------------------")

# students = [kalpesh, sanika, bunny]
# highest_student = None
# highest_percentage = 0

# for student in students:
#     percentage = student.calculate_percentage()
#     if percentage > highest_percentage:
#         highest_percentage = percentage
#         highest_student = student

# print(f"Highest Student : {highest_student.name}")
# print(f"Highest percentage : {highest_percentage}")

########################################################################################################
# Q15. Mini ATM System ⭐

# Create a class ATM with:

# account_holder
# pin
# balance

# Use a constructor to initialize them.

# Create methods:

# check_balance()
# deposit()
# withdraw()
# change_pin()

# The user should only be allowed to perform operations after entering the correct PIN.

# Rules:

# Correct PIN → allow operations.
# Wrong PIN → deny access.
# Withdrawal cannot exceed balance.
# Deposit must be positive.
# New PIN should replace the old PIN.

# Create two ATM/account objects and make sure their data remains separate.

# Challenge: Create a simple menu:

# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Change PIN
# 5. Exit


# Answer -

# class ATM:
#     def __init__(self, account_holder, pin, balance):
#         self.account_holder = account_holder
#         self.pin = pin
#         self.balance = balance

#     def check_balance(self, pin):
#         if pin == self.pin:
#             print(f"Balance : {self.balance}") 
#         else:
#             print("Please Enter correct pin")



#     def deposit(self, amount, pin):
#         if pin == self.pin: 
#             if amount > 0:
#                 self.balance += amount
#             else:
#                 print("Amount must be greater than 0")
#         else:
#             print("Please Enter correct pin")



#     def withdraw(self, amount, pin):
#         if pin == self.pin:
#             if amount <= 0:
#                 print("Amount must be greater than 0")
#             elif amount > self.balance:
#                 print("Insufficient Balance")
#             else:
#                 self.balance -= amount
#         else:
#             print("Please Enter correct pin")
    


#     def change_pin(self, pin):
#         if pin == self.pin:
#             new_pin = int(input("Enter New PIN : "))
#             if len(str(new_pin)) == 4:
#                 self.pin = new_pin
#                 print("PIN changed successfully")
#             else:
#                 print("PIN must contain exactly 4 digits")
#         else:
#             print("Please Enter correct pin")


# user1 = ATM("Kalpesh", 5566, 45500)

    

# while True:
#     print("Menu")
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. change pin")
#     print("5. Exit")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         user1.check_balance(5566)
#     elif choice == 2:
#         user1.deposit(75000,5566)
#     elif choice == 3:
#         user1.withdraw(5000, 5566)
#     elif choice == 4:
#         user1.change_pin(5566)
#     elif choice == 5:
#         print("Exit")
#         break
#     else:
#         print("Invalid Choice")

# Half code of this question
########################################################################################################

###Types of Attributes & Methods 
# Class Attributes , Instance Attributes
# Instance Method, Class Method, Static Method

# Q1. Create a class Student with an instance attribute name set via the constructor. 
# Add an instance method greet() that prints "Hi, I'm <name>".

# Answer -
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hi, I'm {self.name}"

# student1 = Student("Bunny")
# print(student1.greet())

########################################################################################################
# Q2. Create a class Circle with a class attribute pi = 3.14.
# Write an instance method area(self, radius) that uses pi to calculate and return the area.

# Answer -
# class Circle:
#     pi = 3.14

#     def area(self, radius):
#         area = self.pi * radius ** 2
#         return area

# area1 = Circle()
# print(area1.area(50))

########################################################################################################
# Q3.  Create a class Counter with a class attribute count = 0. Every time an object is created, increment count in the constructor. 
# Print Counter.count after creating 3 objects.

# Answer -
# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1

# obj1 = Counter()
# obj2 = Counter()
# obj3 = Counter()

# print(Counter.count)

########################################################################################################
# Q4. Create a class BankAccount with an instance attribute balance. 
# Add a static method is_valid_amount(amount) that returns True if amount > 0, else False. 
# Use it inside a deposit() instance method before updating balance.

# Answer -
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     @staticmethod
#     def is_valid_amount(amount):
#         if amount > 0: 
#             return True
#         else:
#             return False

#     def deposit(self, amount):
#         result = self.is_valid_amount(amount)
#         if result:
#             self.balance += amount
#         else:
#             print("Amount must be greater than 0")

# user1 = BankAccount(75000)
# user1.deposit(25000)
# print(user1.balance)

########################################################################################################
# Q5. Create a class Employee with instance attributes name and salary, and a class attribute company_name = "TechCorp". 
# Add a class method change_company(cls, new_name) that updates company_name for the class.

# Answer -
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     company_name = "TechCorp"
    

#     @classmethod
#     def change_company(cls, new_name):
#        cls.company_name = new_name


# obj = Employee("Kalpesh", 75000)
# obj.change_company("freeFire")
# print(obj.company_name)

# obj2 = Employee("Sanika", 60000)
# print(obj2.company_name)

########################################################################################################
# Q6. Create a class Product with instance attributes price and quantity. 
# Add an instance method total_cost() and a static method apply_tax(amount, tax_rate) that returns amount + (amount * tax_rate). 
# Combine both to print the total cost with 5% tax.


# Answer -
# class Product:
#     def __init__(self, price, quantity):
#         self.price = price
#         self.quantity = quantity

#     def total_cost(self):
#         total_cost = self.price * self.quantity
#         return total_cost

#     @staticmethod
#     def apply_tax(amount, tax_rate):
#         result = amount * tax_rate
#         applied_tax = result + amount
#         return applied_tax


# milk = Product(56, 10)
# total_cost_of_milk = milk.total_cost()
# final_value_of_milk = milk.apply_tax(total_cost_of_milk,0.05)
# print(f"Total cost of milk : {total_cost_of_milk}")
# print(f"Final value with tax : {final_value_of_milk}")

########################################################################################################
# Q7. Demonstrate the difference between an instance attribute and a class attribute by creating a class Dog with class attribute species = "Canine" and instance attribute name. 
# Change species using one object and show that it does not affect other objects (explain why, based on how you changed it).

# Answer -
# class Dog:
#     species = "Canine"

#     def __init__(self, name):
#         self.name = name 


# dog1 = Dog("rocky")
# dog2 = Dog("Simha")
# dog1.species = "Wolf"
# print(dog1.species)
# print(dog2.species)
# print(Dog.species)

########################################################################################################

### Types of attributes & methods,
### Four Pillars of OOPs :
### Inheritance, polymorphism, encapsulation, abstraction

# Q1. Instance Attribute
# Create a Student class with an instance attribute name and age. 
# Create 3 student objects with different values.

# Answer-
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# student1 = Student("Kalpesh", 22)
# student2 = Student("Sanika", 12)
# student3 = Student("Bunny", 20)

########################################################################################################
# Q2. Class Attribute
# Create a Car class with a class attribute wheels = 4. 
# Create two car objects and display the wheels of both.

# Answer -
# class Car:
#     wheels = 4

# innova = Car()
# fortuner = Car()
# print(f"Innova has {innova.wheels} wheels")
# print(f"Fortuner has {fortuner.wheels} wheels")

########################################################################################################
# Q3. Instance Method
# Create a BankAccount class with an instance attribute balance. 
# Create an instance method show_balance() that displays the balance.

# Answer -
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def show_balance(self):
#         return self.balance

# kalpesh = BankAccount(75000)
# print(f"Kalpesh's balance : {kalpesh.show_balance()}")

########################################################################################################
# Q4. Class Method
# Create a Student class with a class attribute school_name = "ABC School". 
# Create a class method that changes the school name.

# Answer -
# class Student:
#     school_name = "ABC School"

#     @classmethod
#     def change_name(cls, new_name):
#         cls.school_name = new_name

# obj1 = Student()
# obj1.change_name("XYZ School")
# print(obj1.school_name)

########################################################################################################
# Q5. Static Method
# Create a Calculator class with a static method is_even(number) that returns True if the number is even.

# Answer -
# class Calculator:
#     @staticmethod
#     def is_even(number):
#         if number % 2 == 0:
#             return True
#         else:
#             return False


# result = Calculator.is_even(4)
# print(result)

########################################################################################################
# Q6. Combined Attributes
# Create an Employee class containing:

# instance attribute: name
# instance attribute: salary
# class attribute: company = "ABC"

# Display all three values.

# Answer -
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     company = "ABC"

# kalpesh = Employee("kalpesh", 75000)
# print(kalpesh.name)
# print(kalpesh.salary)
# print(kalpesh.company)
# print("-----------------------------------------")
# bunny = Employee("Bunny", 70000)
# print(bunny.name)
# print(bunny.salary)
# print(bunny.company)

########################################################################################################
# Q7. Combined Methods
# Create a MathUtils class containing:

# an instance method to calculate square
# a class method to display the class name
# a static method to check whether a number is positive

# Answer -
# class MathUtils:
#     def calculate_square(self, number):
#         return number ** 2

#     @classmethod
#     def class_name(cls):
#         print(f"Class name is {cls.__name__}")

#     @staticmethod
#     def is_positive(number):
#         if number > 0 :
#             return True
#         else:
#             return False

# obj1 = MathUtils()
# print(obj1.calculate_square(45))
# MathUtils.class_name()
# print(obj1.is_positive(5))

########################################################################################################
# Q8. Basic Inheritance
# Create a Vehicle class with a method start(). Create a Car class that inherits from Vehicle.

# Answer -

# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")

# class Car(Vehicle):
#     name = "Innova"

# car1 = Car()
# car1.start()

########################################################################################################
# Q9. Parent + Child Methods
# Create a Person class with eat(). Create a Student class inheriting from Person with an additional method study().

# Answer -
# class Person:
#     def eat(self):
#         print("Person is eating")

# class Student(Person):
#     def study(self):
#         print("Student is studying")

# kalpesh = Student()
# kalpesh.eat()
# kalpesh.study()

########################################################################################################
# Q10. Constructor Inheritance
# Create a Person class with a constructor accepting name. 
# Create a Student class that inherits from it and adds roll_no.

# Answer -
# class Person:
#     def __init__(self,name):
#         self.name = name


# class Student(Person):
#     def __init__(self, name, roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no

# kalpesh = Student("Kalpesh", 101 )
# print(kalpesh.name)
# print(kalpesh.roll_no)

########################################################################################################
# Q11. Method Overriding
# Create a Animal class with sound(). Create Dog and Cat classes that override sound().

# Anser -
# class Animal:
#     def sound(self):
#         print("Animal makes Sound")

# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")

# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# dog1 = Dog()
# dog1.sound()

# cat1 = Cat()
# cat1.sound()

########################################################################################################
# Q12. super()
# Create a Vehicle class with a constructor that initializes brand. Create a Car class that adds model. Use super().

# Answer -

# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         print("Vehicle is starting")

# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

#     def start(self):
#         super().start()
#         print("Car is ready to drive")


# car1 = Car("Toyota", "Innova")
# car1.start()

########################################################################################################
# Q13. Private Attribute
# Create a BankAccount class with a private attribute __balance. Create methods to deposit and display the balance.

# Answer -
# class BankAccount:
#     def __init__(self, balance, account_no):
#         self.__balance = balance
#         self.account_no = account_no

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Amount Deposited successfully")

#     def show_balance(self):
#         print(f"Current Balance : {self.__balance}")

# user1 = BankAccount(75000, 1234)
# user1.deposit(25000)
# user1.show_balance()

########################################################################################################
# Q14. Protected Attribute
# Create a Person class with a protected attribute _age. Create a Student class that accesses the protected attribute.

# Answer -
# class Person:
#     def __init__(self, age):
#         self._age = age

# class Student(Person):
#     def __init__(self, age):
#         super().__init__(age)

#     def show_age(self):
#         print(f"Person's age is {self._age}")

# s1 = Student(26)
# s1.show_age()

########################################################################################################
# Q15. Private Method
# Create a User class with a private method __show_password(). Call it through another public method.

# Answer -
# class User:
#     def __show_password(self, password):
#         print(f"Password : {password}")


#     def display_password(self):
#         self.__show_password(12345)

# obj = User()
# obj.display_password()

########################################################################################################
# Attributes & Methods

# Q16. Class Attribute Counter
# Create an Employee class with a class attribute employee_count.

# Every time an object is created, increase the count.

# Display the total number of employees created.

# Answer -

# class Employee:
#     employee_count = 0

#     def __init__(self):
#         Employee.employee_count +=  1

# employee1 = Employee()
# employee2 = Employee()
# employee3 = Employee()

# print(f"Total Employees: {Employee.employee_count}")

########################################################################################################
# Q17. Class Method as Alternative Constructor
# Create a Student class with name and age.

# Create a class method:

# from_string("Rahul,21")

# It should create and return a Student object.

# Answer -
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, data):
#         result = data.split(",")
#         name , age = result
#         age = int(age)
#         obj = cls(name, age)

#         return obj

# print(Student.from_string("Kalpesh,22"))
# obj_student = Student.from_string("Kalpesh,22")
# print(obj_student.name)
# print(obj_student.age)

########################################################################################################
# Q18. Static Validation Method
# Create a BankAccount class with an instance attribute balance.

# Create a static method:

# is_valid_amount(amount)

# It should return True if amount > 0.

# Use this method inside deposit().


# Answer -
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     @staticmethod
#     def is_valid_amount(amount):
#         if amount > 0:
#             return True
#         else:
#             return False

#     def deposit(self, amount):
#         if BankAccount.is_valid_amount(amount):
#             self.balance += amount
#         else:
#             print("Deposit Rejected")

# user1 = BankAccount(75000)
# user1.deposit(25000)
# print(user1.balance)

########################################################################################################
# Q19. Class Method + Class Attribute
# Create a Company class with:

# company_name
# employee_count

# Create a class method that changes the company name.

# Create another class method that displays the number of employees.

# Answer -
# class Company:
#     company_name = "AB Company"
#     employee_count = 0

#     def __init__(self):
#         Company.employee_count += 1

#     @classmethod
#     def change_company_name(cls, new_name):
#         cls.company_name = new_name
#         print(f"New Company name : {cls.company_name}")

#     @classmethod
#     def show_employee_count(cls):
#         print(f"No of Employees : {cls.employee_count}") 

# employee1 = Company()
# employee1.change_company_name("Bunny Esportsz")
# employee1.show_employee_count()
# print("---------------------------------------------")
# employee2 = Company()
# employee2.change_company_name("Coding Community")
# employee2.show_employee_count()

########################################################################################################
# Q20. Identify Method Type
# Create a class containing:

# one instance attribute
# one class attribute
# one instance method
# one class method
# one static method

# Then create objects and demonstrate how each one is accessed.

# Answer -
# class Student:
#     def __init__(self, name, age):
#         self.name = name

#         if Student.is_valid_age(age):
#             self.age = age
#         else:
#             print("Age must be greater than 4 or less than 26")

#     school = "JP Morgan"
#     student_count = 0

#     def display_info(self):
#         print(f"Student's Name : {self.name}")
#         print(f"Student's age : {self.age}")
#         print(f"School : {Student.school}")

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school

#     @staticmethod
#     def is_valid_age(age):
#         if 5 <= age <= 25:          #AND operator works here
#             return True
#         else:
#             return False


# kalpesh = Student("Kalpesh", 22)
# kalpesh.display_info()
# Student.change_school("Apna college")
# Student.is_valid_age(22)
# kalpesh.display_info()

########################################################################################################
# Q21. Multilevel Inheritance
# Create:

# Animal
#    ↓
# Mammal
#    ↓
# Dog

# Give each class one unique method and demonstrate that a Dog object can access all three.


# Answer -
# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Mammal(Animal):
#     def walk(self):
#         print("Mammal is walking")

# class Dog(Mammal):
#     def bark(self):
#         print("Dog is barking")

# obj = Dog()

# obj.eat()
# obj.walk()
# obj.bark()

########################################################################################################
# Q22. Hierarchical Inheritance
# Create a parent class Shape.

# Create:

# Circle
# Rectangle
# Triangle

# as child classes.

# Give each child class its own area() method.


# Answer -
# class Shape:
#     def display(self):
#         print("This is a shape")

# class Circle(Shape):
#     pi = 3.14

#     @classmethod
#     def area(cls,radius):
#         return cls.pi * radius ** 2
    
# class Rectangle(Shape):
#     def area(self, length, width):
#         return length * width

# class Triangle(Shape):
#     def area(self, base, height):
#         area = 1/2 * base * height
#         return area


# ball = Circle()
# ball.display()
# print(f"Area of ball : {ball.area(4)}")
# print("---------------------------------------------")
# table = Rectangle()
# table.display()
# print(f"Area of table : {table.area(12, 45)}")
# print("---------------------------------------------")
# pyramid = Triangle()
# pyramid.display()
# print(f"Area of Triangle : {pyramid.area(36, 18)}")

########################################################################################################
# Q23. Multiple Inheritance
# Create:

# Father
# Mother
# Child

# where Child inherits from both Father and Mother.

# Give Father and Mother different methods and access them using the Child object.


# Answer -
# class Mother:
#     def mother_method(self):
#         print("Mother's method")

# class Father:
#     def father_method(self):
#         print("Father's method")
   

# class Child(Mother, Father):
#     def child_method(self):
#         print("Child's method")


# obj_child = Child()
# obj_child.father_method()
# obj_child.mother_method()
# obj_child.child_method()

########################################################################################################
# Q24 — Constructor + super()

# Create a Person class with:

# name
# age

# Then create an Employee class that inherits from Person and adds:

# salary
# Requirements

# Person:

# Person("Kalpesh", 25)

# should initialize:

# name
# age

# Employee:

# Employee("Kalpesh", 25, 75000)

# should initialize:

# name
# age
# salary
# Important

# Inside Employee.__init__(), use:

# super().__init__(...)

# to initialize the parent attributes.

# Then display all three values.


# Answer -
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary


# employee1 = Employee("Kalpesh", 22, 75000)
# print(f"Employee name : {employee1.name}")
# print(f"Employee's age : {employee1.age}")
# print(f"Salary : {employee1.salary}")

########################################################################################################
# 🟡 Q25 — Method Overriding + super()

# Now let's combine method overriding and super().

# Create a Vehicle class with a method:

# start()

# that prints:

# Vehicle is starting

# Then create a Car class that inherits from Vehicle.

# Inside Car, override start().

# Your Car.start() should:

# Call the parent's start() using super()
# Then print:
# Car is ready to drive
# Expected output:
# Vehicle is starting
# Car is ready to drive
# 🧠 The important part

# Your Car should have its own:

# start()

# but inside it, you should also call:

# super().start()

# This is different from Q11 because there you overrode the method without calling the parent version.


# Answer -
# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")


# class Car(Vehicle):
#     def start(self):
#         super().start()
#         print("Car is ready to drive")


# porsche = Car()
# porsche.start()

########################################################################################################
# 🟡 Q26 — Polymorphism: Same Method, Different Behavior

# Now we're moving into polymorphism.

# Create three classes:

# Dog
# Cat
# Cow

# Each class should have the same method:

# sound()

# But each should behave differently:

# Dog  → "Dog barks"
# Cat  → "Cat meows"
# Cow  → "Cow moos"

# Then create a function:

# make_sound(animal)

# The function should call:

# animal.sound()

# Finally, pass a Dog, Cat, and Cow object to make_sound().

# 🧠 Important

# Don't use:

# if animal is Dog:
#     ...
# elif animal is Cat:
#     ...

# The whole point is that the same function should work with different objects because they all provide the same sound() method.

# This is polymorphism.



# Answer -
# class Dog:
#     def sound(self):
#         print("Dog Barks")

# class Cat:
#     def sound(self):
#         print("Cat Meows")

# class Cow:
#     def sound(self):
#         print("Cow Moos")


# def make_sound(animal):
#     animal.sound()

# dog = Dog()
# cat = Cat()
# cow = Cow()

# make_sound(dog)
# make_sound(cat)
# make_sound(cow)

########################################################################################################
# 🟡 Q27 — Polymorphism with Different Classes

# Create two classes:

# Circle
# Rectangle

# Both classes should have:
# area()

# Circle
# Take radius and calculate:
# π × radius²

# You can use:
# 3.14

# Rectangle
# Take length and width and calculate:
# length × width

# Then create a function:
# print_area(shape)
# which simply calls:
# shape.area()

# Finally, pass both a Circle object and a Rectangle object to print_area().

# 🧠 Important
# Again, don't use if/elif to determine the object's type.
# The function should work because both objects provide an area() method.



# Answer -
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     pi = 3.14
    
#     def area(self):
#         return Circle.pi * self.radius ** 2

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width 

#     def area(self):
#         return self.length * self.width


# def print_area(shape):
#     return shape.area()

# ball = Circle(5)
# table = Rectangle(12, 26)
# print(f"Area of Ball : {print_area(ball)}")
# print(f"Area of Table : {print_area(table)}")

########################################################################################################
# 🟡 Q28 — Duck Typing

# Now we're going one step deeper into polymorphism.

# Create three completely unrelated classes:
# Printer
# Scanner
# Camera

# Do not make them inherit from one another.

# Each class should have the same method:
# start()

# They should print:
# Printer → Printer is starting
# Scanner → Scanner is starting
# Camera  → Camera is starting

# Then create:
# start_device(device)
# This function should simply call:
# device.start()

# Finally:
# start_device(printer)
# start_device(scanner)
# start_device(camera)

# 🧠 Important
# There should be no inheritance between these classes.
# The function doesn't care what type of object it receives.

# It only cares:
# Does this object have a start() method?
# This is called duck typing in Python.


# Answer -
# class Printer:
#     def start(self):
#         print("Printer is starting")

# class Scanner:
#     def start(self):
#         print("Scanner is starting")

# class Camera:
#     def start(self):
#         print("Camera is starting")


# def start_device(device):
#     device.start()

# obj_printer = Printer()
# obj_scanner = Scanner()
# obj_camera = Camera()

# start_device(obj_printer)
# start_device(obj_scanner)
# start_device(obj_camera)

########################################################################################################
# 🟡 Q29 — Encapsulation: Controlled Bank Balance

# Create a BankAccount class with a private attribute:
# __balance

# Requirements
# 1. Constructor
# Accept:
# balance
# and store it privately.

# 2. deposit(amount)
# Add money to the balance.
# But only allow the deposit if:
# amount > 0

# 3. withdraw(amount)
# Subtract money from the balance only if:
# amount > 0
# and:
# amount <= balance
# If the amount is greater than the balance, print:
# Insufficient balance

# 4. get_balance()
# Return or display the private balance.

# 🧠 Important
# Outside the class, you should not directly access:
# account.__balance

# The balance should be controlled through:
# deposit()
# withdraw()
# get_balance()

# Test your class with:
# Initial balance: 10000
# Deposit: 5000
# Withdraw: 3000
# Try withdrawing: 20000

# This question is testing encapsulation + validation + instance methods.


# Answer -
# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance 

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Amount must be greater than 0")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance")

#     def get_balance(self):
#         print(f"Current Balance : {self.__balance}")


# user1 = BankAccount(10000)
# user1.deposit(5000)
# user1.withdraw(3000)
# user1.get_balance()
# user1.withdraw(20000)

########################################################################################################
# 🟡 Q30 — Encapsulation: Password Protection

# Create a User class with two private attributes:
# __username
# __password

# Requirements
# Constructor
# Accept:
# username
# password
# and store both privately.

# 1. change_password(new_password)
# Allow the user to change their password.

# 2. verify_password(password)
# Check whether the supplied password matches the stored password.
# It should return:
# True
# if correct, otherwise:
# False

# 3. display_username()
# Display the username.

# Important 🔐
# You should not provide a method that directly displays the password.
# And outside the class, don't do:
# user.__password

# Test your class
# Create:
# username = "Kalpesh"
# password = "12345"

# Then:
# Verify "12345" → should return True
# Verify "99999" → should return False
# Change password to "54321"
# Verify "54321" → should return True


# Answer -
# class User:
#     def __init__(self, username, password):
#         self.__username = username
#         self.__password = password

#     def change_password(self, new_password):
#         self.__password = new_password

#     def verify_password(self, password):
#         if password == self.__password:
#             return True
#         else:
#             return False

#     def display_username(self):
#         print(f"Username : {self.__username}")

# kalpesh = User("Kalpesh", 12345)
# print(kalpesh.verify_password(12345))
# print(kalpesh.verify_password(99999))
# kalpesh.change_password(54321)
# print(kalpesh.verify_password(54321))
# kalpesh.display_username()

########################################################################################################
# 🔴 Q31 — Bank Account System

# Build a BankAccount class with the following requirements.
# Attributes
# Instance attributes:
# account_holder
# __balance
# __balance must be private.

# Class attribute:
# bank_name = "ABC Bank"

# Methods
# 1. deposit(amount)
# Deposit money only if the amount is valid.

# 2. withdraw(amount)
# Withdraw money only if:
# amount > 0
# and sufficient balance exists.

# 3. check_balance()
# Display the current balance.

# 4. Static method
# Create:
# is_valid_amount(amount)
# It should return True if the amount is greater than 0.

# 5. Class method
# Create:
# change_bank_name(new_name)
# which changes the bank name for all accounts.

# Test your system
# Create two accounts:
# Kalpesh → ₹75,000
# Bunny   → ₹50,000

# Perform some deposits and withdrawals.
# Then change the bank name using the class method.
# Finally, display:
# Account holder
# Balance
# Bank name

# 🔥 Challenge
# Think carefully about which things should be:
# Instance attribute
# Class attribute
# Instance method
# Class method
# Static method
# Private attribute

# Don't just code it—design the class first in your head.

# This is your first hard-level question. Take your time. 💪


# Answer -
# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.account_holder = account_holder
#         self.__balance = balance


#     bank_name = "ABC Bank"

#     def deposit(self, amount):
#         if BankAccount.is_valid_amount(amount):
#             self.__balance += amount
#         else:
#             print("Amount must be greater than 0")

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance")

#     def current_balance(self):
#         return self.__balance

#     @staticmethod
#     def is_valid_amount(amount):
#         if amount > 0:
#             return True
#         else:
#             return False

#     @classmethod
#     def change_bank_name(cls, new_name):
#         cls.bank_name = new_name


# kalpesh = BankAccount("Kalpesh", 75000)
# bunny = BankAccount("Bunny", 50000)
# kalpesh.deposit(45000)
# bunny.deposit(100000)
# kalpesh.deposit(-20000)
# kalpesh.change_bank_name("Free Fire")
# print("---------------------------------------------------")
# print(f"Account Holder : {kalpesh.account_holder}")
# print(f"Account Holder : {bunny.account_holder}")
# print("---------------------------------------------------")
# print(f"Kalpesh's Balance : {kalpesh.current_balance()}")
# print(f"Bunny's Balance : {bunny.current_balance()}")
# print("---------------------------------------------------")
# print(f"Kalpesh's Bank name : {kalpesh.bank_name}")
# print(f"Bunny's Bank name : {bunny.bank_name}")
# print("---------------------------------------------------")

########################################################################################################
# 🔴 Q32 — Employee Management System

# Create an Employee class.

# Requirements

# Class attributes
# company = "ABC Ltd"
# employee_count = 0

# Instance attributes
# Each employee should have:
# name
# salary

# Every time an employee is created, employee_count should increase.

# Methods
# 1. display_info()

# Display:
# Employee name
# Salary
# Company

# 2. change_company(new_company)
# Use a class method to change the company name for all employees.

# 3. is_valid_salary(salary)
# Use a static method.
# A salary is valid only if:
# salary > 0

# 4. Salary validation
# The constructor should use is_valid_salary() before accepting the salary.
# If an invalid salary is provided, display:
# Invalid salary

# 🔥 Test your system
# Create three employees:
# Kalpesh → 75,000
# Bunny   → 70,000
# Sanika  → 60,000

# Then:
# Display all employee information.
# Display total employee count.
# Change the company name.
# Display employee information again.
# Try creating an employee with a negative salary.

# 🧠 Design challenge
# Before coding, identify:
# name           → ?
# salary         → ?
# company        → ?
# employee_count → ?

# display_info()      → ?
# change_company()    → ?
# is_valid_salary()   → ?

# This question is very similar to Q20, but now you're applying the concepts in a more realistic employee-management scenario.


# Answer -
# class Employee:
#     company = "ABC ltd"
#     employee_count = 0

#     def __init__(self, name, salary):
#         self.name = name
#         if Employee.is_valid_salary(salary):
#             self.salary = salary
#             Employee.employee_count += 1

#         else:
#             print("Invalid salary")

#     def display_info(self):
#         print(f"Employee name : {self.name}")
#         print(f"Salary : {self.salary}")
#         print(f"Company : {Employee.company}")

#     @classmethod
#     def change_company(cls, new_company):
#         cls.company = new_company

#     @staticmethod
#     def is_valid_salary(salary):
#         if salary > 0:
#             return True
#         else:
#             return False

# kalpesh = Employee("Kalpesh", 75000)
# bunny = Employee("Bunny", 70000)
# sanika = Employee("Sanika", 60000)
# killer = Employee("Killer", -70000)

# kalpesh.display_info()
# sanika.display_info()
# bunny.display_info()
# kalpesh.change_company("XXX ltd")
# print("-----------     After Changing Company    ---------------------------")
# kalpesh.display_info()
# sanika.display_info()
# bunny.display_info()
# print("------    ---------------")
# print(f"Total Employees : {Employee.employee_count}")

########################################################################################################
# 🔴 Q33 — E-Commerce Product System

# Now we're going to combine Inheritance + Method Overriding + Polymorphism.

# Create a parent class:
# Product
# It should have:
# name
# price
# as instance attributes.
# And a method:
# calculate_discount()
# The parent version can simply return the original price.

# Create three child classes
# Electronics
# Clothing
# Food

# All three should inherit from Product.
# Each should override calculate_discount() with a different discount.
# For example:
# Electronics → 10% discount
# Clothing    → 20% discount
# Food        → 5% discount

# You can calculate the final price like:
# final_price = price - discount
# Then create a polymorphic function
# Create:
# show_final_price(product)

# It should simply do:
# print(product.calculate_discount())

# Don't use if/elif to check whether the product is Electronics, Clothing, or Food.
# Test it
# Create:
# Laptop → ₹50,000
# T-Shirt → ₹2,000
# Pizza → ₹500

# Then pass all three objects to:
# show_final_price()

# 🧠 Concepts you're combining
# Product
#    │
#    ├── Electronics → calculate_discount()
#    ├── Clothing    → calculate_discount()
#    └── Food        → calculate_discount()
#                        ↓
#                polymorphic function

# This is a real OOP design pattern: the caller doesn't need to know which child class it's dealing with.
# Take your time with this one. 💪


# Answer -
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def calculate_discount(self):
#         return self.price

# class Electronic(Product):
#     def __init__(self, name, price):
#         super().__init__(name, price)

#     def calculate_discount(self):
#         final_price = self.price - (self.price * 0.1)
#         return final_price

# class Clothing(Product):
#     def __init__(self, name, price):
#         super().__init__(name, price)

#     def calculate_discount(self):
#         final_price = self.price - (self.price * 0.2)
#         return final_price

# class Food(Product):
#     def __init__(self, name, price):
#         super().__init__(name, price)

#     def calculate_discount(self):
#         final_price = self.price - (self.price *  0.05)
#         return final_price


# def show_final_price(product):
#     print(f"Final price of {product.name} : {product.calculate_discount()}")


# laptop = Electronic("Laptop", 85000)
# t_shirt = Clothing("Tees", 2000)
# pizza = Food("Pizza", 500)

# show_final_price(laptop)
# show_final_price(t_shirt)
# show_final_price(pizza)

########################################################################################################
# 🔴 Q34 — Vehicle Rental System

# Create a parent class:
# Vehicle

# Vehicle attributes:
# brand
# rent_per_day

# Vehicle method:
# Create:
# calculate_rent(days)

# The parent version can simply return:
# rent_per_day × days


# Create three child classes:
# Car
# Bike
# Truck

# All inherit from Vehicle.

# Each should override calculate_rent(days).

# Use different pricing rules:
# Car
# Normal rent:
# rent_per_day × days

# Bike
# Give a 10% discount on the total rent.

# Truck
# Add a ₹500 service charge to the total rent.

# Static method
# Create:
# is_valid_days(days)
# It should return True if:
# days > 0
# Otherwise False.
# Use this validation before calculating rent.

# Polymorphic function
# Create:
# show_rent(vehicle, days)
# It should call:
# vehicle.calculate_rent(days)

# Do not use if/elif to determine whether it's a Car, Bike, or Truck.

# Test with
# Car   → ₹2,000/day
# Bike  → ₹800/day
# Truck → ₹3,000/day

# Calculate rent for:
# 5 days

# Also test an invalid value such as:
# 0 days

# 🧠 Concepts being tested
# Inheritance
#      ↓
# Method Overriding
#      ↓
# Polymorphism
#      ↓
# Static Method
#      ↓
# Validation

# This one is harder because you need to decide where the validation belongs and how each child should calculate its own rent.

# Try it yourself. 💪


# Answer -
class Vehicle:
    def __init__(self, brand, rent_per_days):
        self.brand = brand
        self.rent_per_days = rent_per_days

    def calculate_rent(self, days):
        return self.rent_per_days * days


class Car(Vehicle):
    def calculate_rent(self, days):
        return self.rent_per_days * days

class Bike(Vehicle):
    def calculate_rent(self, days):
        rent = self.rent_per_days * days
        discount = rent * 0.1
        total_rent = rent - discount
        return total_rent

class Truck(Vehicle):
    service_charge = 500
    def calculate_rent(self, days):
        rent = self.rent_per_days * days
        total_rent = rent + Truck.service_charge
        return total_rent
