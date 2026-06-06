# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

Write your name on line 6, save it, and then head back to GitHub Desktop.
TWO SUM
class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit

Check Palindrome String
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print(is_palindrome("madam"))

Count Frequency of Characters
def char_frequency(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

print(char_frequency("hello"))

Remove Duplicates from List
def remove_duplicates(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)

    return result

nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))

Find Second Largest Number
def second_largest(nums):
    largest = second = float('-inf')

    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif largest > num > second:
            second = num

    return second

nums = [10, 20, 4, 45, 99]
print(second_largest(nums))

Fibonacci Series
def fibonacci(n):
    fib = [0, 1]

    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])

    return fib[:n]

print(fibonacci(7))

Find Missing Number
def find_missing(nums):
    n = len(nums) + 1

    exp_sum = n * (n + 1) // 2
    act_sum = sum(nums)

    return exp_sum - act_sum

nums = [1, 2, 4, 5, 6]
print(find_missing(nums))

Merge Two Dictionaries
def merge_dicts(d1, d2):
    result = d1.copy()

    for i, val in d2.items():
        if i in result:
            result[i] += val
        else:
            result[i] = val

    return result

d1 = {'a': 11, 'b': 22}
d2 = {'b': 0, 'c': 44}

print(merge_dicts(d1, d2))

Matrix Addition
def matrix_addition(A, B):
    r = len(A)
    c = len(A[0])

    res = []

    for i in range(r):
        r = []
        for j in range(c):
            row.append(A[i][j] + B[i][j])
        res.append(r)

    return res

A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

print(matrix_addition(A, B))

print("Hello, World!")
age = 18      # age is of type int
name = "John" # name is now of type str
print(name)

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
sub = a - b
sum = a + b
print("The Sum and Sub is: ",sum,sub)

#Armstrong = 153 = 1^3+5^3+3^3=153
n = int(input("Enter: "))
temp = n
s = 0
while n > 0:
    r = n % 10
    s += r**3
    n //= 10
if s == temp:
    print("Armstrong")
else:
    print("Not Armstrong")

#GCD=GREATEST COMMON DIVISOR Ctrl + A to select all ,  Ctrl + / = # 
a = int(input("Enter any number: ")) #int
b = int(input("Enter any number: ")) #int
while b != 0:
    a,b = b,a%b
print(a)

#LCM=LEAST COMMON MULTIPLE
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
x, y = a, b
while y:
    x, y = y, x%y
print((a*b) // x)

#Perfect number or not
n = int(input("Enter any number: "))
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i
if s == n:
    print("Perfect")
else:
    print("Not Perfect")

#All prime no. between two numbers
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
for n in range(a, b+1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
            else:
                print(n, end=" ")

#Strong number or not
import math 
n = int(input("Enter any number: "))
temp = n
s = 0
while n > 0:
    s += math.factorial(n % 10)
    n //= 10
if s == temp:
    print("Strong")
else:
    print("Not Strong")

#Reverse a given number
n = int(input("Enter any number: "))
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)

#Palindrome or not 
n = int(input("Enter any number: "))
temp = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
if temp == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

#Convert decimal number into binary
n = int(input("Enter any number: "))
print(bin(n)[2:])

# #Nth term of the fibonnaci series
n = int(input("Enter any number: "))
a, b = 0, 1
for i in range(n):
    a, b = b, a + b
print(a)

# #Two strings are anagrams
s1 = input("Enter a string: ")
s2 = input("Enter a string: ")
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")

#python with matplotlib
import matplotlib.pyplot as plt

# Programming languages and their percentages
languages = ['Python', 'Java', 'C++', 'JavaScript', 'C']
percentages = [35, 25, 15, 15, 10]

# Create pie chart
plt.pie(
    percentages,
    labels=languages,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Programming Language Popularity (%)")
plt.show()
        
