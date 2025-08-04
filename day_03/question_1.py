# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def validAnagram(s1,s2):
    return sorted(s1)==sorted(s2)


print(validAnagram("anagram","nagaram"))