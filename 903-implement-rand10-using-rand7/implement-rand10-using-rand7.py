# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self) -> int:
        while True:
            # rand7() gives 1-7, so (rand7()-1)*7 gives 0,7,14,21,28,35,42
            # Add rand7() gives uniform 1-49
            num = (rand7() - 1) * 7 + rand7()

            if num <= 40: # take only 1-40, reject 41-49
                return (num - 1) % 10 + 1 # map 1-40 -> 1-10