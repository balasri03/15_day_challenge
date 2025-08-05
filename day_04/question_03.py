# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def validParanthsis(s):
    stk=[]
    match={
        ')':'(',
        '}':'{',
        ']':'['
    }
    for i in range(len(s)):
        if s[i] in '({[':
            stk.append(s[i])
        elif s[i] in ')}]':
            if not stk or stk[-1]!=match[s[i]]:
                return False
            stk.pop()
    return not stk

print(validParanthsis("()"))