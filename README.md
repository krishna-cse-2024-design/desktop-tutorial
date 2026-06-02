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



        
