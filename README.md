# Welcome to GitHub Desktop!

This is your README. READMEs are where you can communicate what your project is and how to use it.

SWAP IN INTEGERS
a = int(input(Enter: ))
b = int(input(Enter: ))
a,b = b,a 
print(a,b)

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

# Lists
l = [2,3,5,7,11]
print(l)

# Add two more primes
l.append(13)
l.append(17)
print(l)

# Removing 5th prime
i = 5
l.pop(i-1)
print(l)

# Converting a list to a tuple
t = tuple(l)
print(t)

# Inserting 5th prime
l.append(11)
print(l)

#Sort list
l.sort()
print(l)

for j in range(len(l)):
    print(l[j]," ",type(l[j]))

# Total elements
print(len(l))

#
# For 2D list....([0]*columns)*rows

n = int(input("Enter the order: "))
row = col = n

unitmatrix = [[0]*col for _ in range(row)]   # This is to create multiple lists ie like matrix
# unitmatrix = [[0]*col]*row This creates a copy of list   

print("0"*7)
print(type(unitmatrix))
print(unitmatrix)
z = 0
for row in range(n):
    for col in range(n):
        if row == col:
            unitmatrix[row][col] = 1
        else:
            unitmatrix[row][col] = 0

print(unitmatrix)


# Factorial series program

n = int(input("Enter the value of n: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i
    print(f"{i}! = {fact}")
    
#* Single            
print("*")

#Horizontal Line
n = 5
print("*" * n)

#Vertical Line
n = 5
for i in range(n):
    print("*")

#Square Pattern
n = 5
for i in range(n):
    print("*" * n)
    
#Right Triangle
n = 5
for i in range(1, n + 1):
    print("*" * i)
    
#Inverted Right Triangle
n = 5
for i in range(n, 0, -1):
    print("*" * i)
    
#Pyramid
n = 5
for i in range(n):
    spaces = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
    
#Inverted Pyramid
n = 5
for i in range(n):
    spaces = " " * i
    stars = "*" * (2 * (n - i) - 1)
    print(spaces + stars)
    
#Diamond
n = 5

# Upper half
for i in range(n):
    spaces = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

# Lower half
for i in range(n - 2, -1, -1):
    spaces = " " * (n - i - 1)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
    
#Hollow Square
n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")

#Project: Password Strength Checker
import string


def check_password_strength(password):
    score = 0
    feedback = []

    # Minimum length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Uppercase
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Lowercase
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Digit
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Special character
    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score == 5:
        strength = "Very Strong 💪"
    elif score == 4:
        strength = "Strong ✅"
    elif score == 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    return strength, feedback


def main():
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)

    print("\nPassword Strength:", strength)

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)


if __name__ == "__main__":
    main()
        
