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

########################################################################################################
