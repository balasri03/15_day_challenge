# Given a string s, return the longest palindromic substring in s.

def longestPalindrome(s):
    if len(s)<=1:
        return s
    def match(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    longest=""
    for i in range(len(s)):
        odd_palindrome=match(i,i)
        if len(odd_palindrome)>len(longest):
            longest=odd_palindrome
        even_palindrome=match(i,i+1)
        if len(even_palindrome)>len(longest):
            longest=even_palindrome
    return longest

print(longestPalindrome("babad"))  # Output: "bab" or "aba"