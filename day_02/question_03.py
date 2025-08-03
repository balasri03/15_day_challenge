# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


def isValidPalindrome(s):
    st="".join(filter(lambda c:c.isalnum(),s)).lower()
    return st == st[::-1]

print(isValidPalindrome("A man, a plan, a canal: Panama"))