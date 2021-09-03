#1 Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.
def hello_name(user_name):
    print(f"Hello, {user_name.title()}!")

hello_name("christian")

#2 Print first 100 odd numbers in Python.
def odd_numbers_only(numbers):
    for number in range(numbers):
        if number % 2 != 0:
            print(number)

odd_numbers_only(100)

#3 Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.
def max_num_in_list(a_list):
    max = 0
    for num in a_list:
        if num > max:
            max = num
    print(max)

max_num_in_list([2,78,67,50,85])

# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    return False

print(is_leap_year(2004))

# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.
def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    range_list = list(range(min(a_list), max(a_list)+1))
    if sorted_list == range_list:
        return True
    return False
lst = [2,3,4,5,7]
print(is_consecutive(lst))
