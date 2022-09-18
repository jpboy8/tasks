# 1) Write a program in Python to display the cube of the number upto given an integer. Go to the editor

# num = input('Print num: ')
# cube = int(num)**3
# print(f'Number is : {num} and cube of the {num} is :{cube}')


# 2) Print list in reverse order using a loop

# arr = [i for i in range(10, 51, 10)]
# arr.sort(reverse=True)
# print(arr)


# 3) Find the factorial of a given number

# num = int(input('Print num: '))
# rez = 1
# for i in range(1, num + 1):
#     rez *= i

# print(rez)


# 4) Calculate the sum of all numbers from 1 to a given number

# num = int(input('Print num: '))
# arr = [i for i in range(1, num + 1)]
# rez = 0

# for i in arr:
#     rez += i

# print(rez)


# 5) Given an integer x, return true if x is palindrome integer.

# num = int(input('Print num: '))
# str_num = str(num)[::-1]

# if str(num) == str_num:
#     print('True')
# else:
#     print('False')


# Solve Problems using nested loops
# 1) Write a program to use for loop to print the following reverse number pattern


# num = int(input('Print num: '))


# string_num = ''.join([str(i) for i in range(num, 0, -1)])

# for i in range(num):
#     print(string_num[i:])

# 2) Write a program to use for loop to print the following number pattern

# num = int(input('Print num: '))

# for i in range(1, num + 1):
#     print(str(i) * i)


# Solve problems using regular or lambda functions
# 1) Create a lambda function get_discount that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

# get_count = lambda price, prec: price - (price * prec/100)

# print(get_count(100,75))


# 2) Write a function sum_numbers that finds the sum of the first n natural numbers. Make your function recursive


# sum_numbers = lambda n: sum([i for i in range(1, n+1)])


# print(sum_numbers(5))


# 3) Create a function is_triplet that validates whether three given integers form a Pythagorean triplet. The sum of the squares of the two smallest integers must equal the square of the largest number to be validated.

# is_triplet = lambda a,b,c: a**2 + b**2 == c**2

# print(is_triplet(3,4,5))

