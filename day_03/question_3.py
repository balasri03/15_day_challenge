# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

def group_anagrams(arr):
    res={}
    for s in arr:
        count=[0]*26
        for i in s:
            count[ord(i)-ord('a')]+=1
        key=tuple(count)
        if key not in res:
            res[key]=[]
        res[key].append(s)
    return list(res.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))