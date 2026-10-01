class Solution:
    # def isValid(self, s: str) -> bool:
#         # for i in range(int(len(s)/2)):
#         #     last = s.pop
#         #     first = s[i]
#         #     if first != last:
#         #         return False
#         # return True 
#         # Does not work - ()()
    
#         # stack1 = []
#         # stack2 = []
#         # stack3 = []
#         # Does not work

#         # problem loosley comes down to: Yes while ()() = true and ([)] = false, we can delineate these by saying we expect the next closing bracket to always close the next unclosed open bracket that was opened last ([]). How can we keep track of which are yet to be closed: a stack

#         # stack = []
#         # for i in range(len(s)):
#         #     if s[i] == '(' or s[i] == '[' or s[i] == '{':
#         #         stack.append(s[i])
#         #         continue
#         #     # elif not not stack:
#         #     elif is stack:
#         #         last = stack.pop()
#         #         if last == '(' and s[i] == ')':
#         #             if i == (len(s)-1):
#         #                 return True
#         #             else:
#         #                 continue
#         #         elif last == '[' and s[i] == ']':
#         #             if i == (len(s)-1):
#         #                 return True
#         #             else:
#         #                 continue
#         #         elif last == '{' and s[i] == '}':
#         #             if i == (len(s)-1):
#         #                 return True
#         #             else:
#         #                 continue
#         #         else: 
#         #             return False
#         #     else: 
#         #         return False

#         # above returns True and forgets about remaining ( in the stack, in this case it should return False but it returns True -> add "and not stack:"
#         # additionally if its just ( it continues without returning anything (null)

                
#         # stack = []
#         # for i in range(len(s)):
#         #     if s[i] == '(' or s[i] == '[' or s[i] == '{':
#         #         if i == (len(s)-1):
#         #             return False
#         #         else:
#         #             stack.append(s[i])
#         #             continue
#         #     # elif not not stack:
#         #     # is stack would not work:
#         #     elif stack:
#         #         last = stack.pop()
#         #         if last == '(' and s[i] == ')':
#         #             if i == (len(s)-1) and not stack:
#         #                 return True
#         #             else:
#         #                 continue
#         #         elif last == '[' and s[i] == ']':
#         #             if i == (len(s)-1) and not stack:
#         #                 return True
#         #             else:
#         #                 continue
#         #         elif last == '{' and s[i] == '}':
#         #             if i == (len(s)-1) and not stack:
#         #                 return True
#         #             else:
#         #                 continue
#         #         else: 
#         #             return False
#         #     else: 
#         #         return False
        
#         # Does not account for instance where there is a remaining open brack yet to be closed
          
#         # stack = []
#         # for i in range(len(s)):
#         #     if s[i] == '(' or s[i] == '[' or s[i] == '{':
#         #         if i == (len(s)-1):
#         #             return False
#         #         else:
#         #             stack.append(s[i])
#         #             continue
#         #     # elif not not stack:
#         #     # is stack would not work:
#         #     elif stack:
#         #         last = stack.pop()
#         #         if last == '(' and s[i] == ')':
#         #             if i == (len(s)-1) and not stack:
#         #                 return True
#         #             elif i == (len(s)-1):
#         #                 return False
#         #             else:
#         #                 continue
#         #         elif last == '[' and s[i] == ']':
#         #             if i == (len(s)-1) and not stack:
#         #                 return True
#         #             elif i == (len(s)-1):
#         #                 return False
#         #             else:
#         #                 continue
#         #         elif last == '{' and s[i] == '}':
#         #             if i == (len(s)-1) and not stack:
#         #                 return True
#         #             elif i == (len(s)-1):
#         #                 return False
#         #             else:
#         #                 continue
#         #         else: 
#         #             return False
#         #     else: 
#         #         return False
        

# # The above works but what if we simplified it using a map (dictionary). What if we also make it so the beyond i checks are done outside the loop 
# # If True means “the entire input satisfies some condition”, and later elements could still invalidate that condition, then returning True inside the loop is # # #  usually wrong or forces you into awkward caveats.
#         stack = []
#         brMap = {'(':')','[':']','{':'}'}

#         for i in range (len(s)):
#             if s[i] in "([{":
#                 stack.append(s[i])
#                 continue
#             # elif s[i] == brMap[stack[-1]]: remember to account for case where next is trying to close an empty stack
#             elif stack and s[i] == brMap[stack[-1]]: 
#                 stack.pop()
#                 continue
#             else:
#                 return False

#         if stack:
#             return False
#         else:
#             return True




## New
    def isValid(self, s: str) -> bool:
        stack = []
        pare = {'(':')','[':']','{':'}'}

        for i in range (len(s)):
            if s[i] in ['(','[','{']:
                stack.append(s[i])          
            else:
                if stack:
                    if pare[stack[-1]] == s[i]:
                        del stack[-1]
                    else:
                        return False #closing not match last opening
                else:
                    return False #closing empty
        if stack:
            return False
        else:
            return True



# Main things are not trying to account for final in each case
# Also use map for paranthesis
# Also we are not using stack just to check for perfect ([{}]) as there can be multiple consecutive that are not within eachother.
    # Instead we are using a stack to check if the next closing closes the last opening as you cannot have ([)]


# Sorting bigs
# {} for dictionaries
# use s not str
# know when to use [] vs () method vs iterable

