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

