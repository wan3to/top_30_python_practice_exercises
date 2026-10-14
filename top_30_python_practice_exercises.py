def sum_two_numbers():
    a = 4
    b = 5
    # Your code here
    return

def check_even_odd():
    n = 7
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd())  # Output: Odd

def largest_of_three():
    a, b, c = 3, 9, 2
    return max(a, b, c)

print(largest_of_three())  # Output: 9

def reverse_string():
    s = "hello"
    return s[::-1]

print(reverse_string())  # Output: olleh

def is_palindrome():
    s = "madam"
    return s == s[::-1]

print(is_palindrome())  # Output: True

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
n = 5
print(factorial(n))  # Output: 120

def sum_of_list():
    lst = [1, 2, 3, 4, 5]
    return sum(lst)

print(sum_of_list())  # Output: 15

def fibonacci():
    n = 5
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci())  # Output: [0, 1, 1, 2, 3]

def second_largest():
    lst = [4, 3, 1, 2]
    unique_list = list(set(lst))  # Remove duplicates
    unique_list.sort(reverse=True)
    return unique_list[1]

print(second_largest())  # Output: 3

import math

def find_gcd():
    a, b = 8, 12
    return math.gcd(a, b)

print(find_gcd())  # Output: 4

import math

def find_lcm():
    a, b = 4, 5
    return (a * b) // math.gcd(a, b)

print(find_lcm())  # Output: 20

def is_prime():
    n = 7
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime())  # Output: True

def longest_word_length(s):
    words = s.split()
    return len(max(words, key=len))
longest_word='Python is amazing'
print(longest_word_length(longest_word))  # Output: 7

def to_uppercase(s):
    return s.upper()
words_case='python java cpp'
print(to_uppercase(words_case))  # Output: PYTHON JAVA CPP


def remove_duplicates(lst):
    return list(set(lst))
duplicate_list=[1, 2, 2, 3, 3, 3, 4]
print(remove_duplicates(duplicate_list))  # Output: [1, 2, 3, 4]

def sort_list(lst):
    return sorted(lst)
un_sorted=[5, 3, 8, 1, 2]
print(sort_list(un_sorted))  # Output: [1, 2, 3, 5, 8]

def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))
lst1=[1, 2, 3, 4]
lst2=[3, 4, 5, 6]
print(common_elements(lst1,lst2))  # Output: [3, 4]

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
word_1='listen'
word_2='silent'
print(are_anagrams(word_1, word_2))  # Output: True

def find_intersection(set1, set2):
    return set(set1).intersection(set(set2))
set_1=[1, 2, 3]
set_2=[3, 4, 5]
print(find_intersection(set_1, set_2))  # Output: {3}

def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)
list_1 = [1, 3, 5]
list_2 = [2, 4, 6]
print(merge_sorted_lists(list_1, list_2)) #Output [1, 2, 3, 4, 5, 6]


def most_frequent(lst):
    return max(lst, key=lst.count)
lst=[1, 2, 3, 3, 2, 2]
print(most_frequent(lst))  # Output: 2

def flatten_list(lst):
    return [item for sublist in lst for item in sublist]
lst=[[1, 2], [3, 4], [5, 6]]
print(flatten_list(lst))  # Output: [1, 2, 3, 4, 5, 6]

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))
digits=123
print(sum_of_digits(digits))  # Output: 6

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
matrix=[[1, 2], [3, 4]]
print(transpose_matrix(matrix))  # Output: [[1, 3], [2, 4]]

def remove_element(lst, element):
    return [x for x in lst if x != element]
lst=[1, 2, 3, 2, 4]
element=2
print(remove_element(lst, element))  # Output: [1, 3, 4]

def second_smallest(lst):
    unique_list = sorted(set(lst))
    return unique_list[1]
lst=[4, 3, 1, 2]
print(second_smallest(lst))  # Output: 2

def is_perfect_square(n):
    return int(n ** 0.5) ** 2 == n
n=25
print(is_perfect_square(n))  # Output: True

def sum_of_even(lst):
    return sum(x for x in lst if x % 2 == 0)
lst=[1, 2, 3, 4, 5]
print(sum_of_even(lst))  # Output: 6

def rotate_list(lst, k):
    k = k % len(lst)  # To handle cases where k is larger than list size
    return lst[-k:] + lst[:-k]
lst = [1, 2, 3, 4, 5]
k = 2
print(rotate_list(lst, k)) # Output: [4, 5, 1, 2, 3]
