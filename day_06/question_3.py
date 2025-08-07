# Given a string s, find the length of the longest substring without duplicate characters.

def length_of_longest_substring(s):
    mp=set()
    left=0
    maxLen=0
    for right in range(len(s)):
        while s[right] in mp:
            mp.remove(s[right])
            left+=1
        mp.add(s[right])
        maxLen=max(maxLen,right-left+1)
    return maxLen

print(length_of_longest_substring("abcabcbb"))
