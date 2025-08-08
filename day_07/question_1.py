# Given an array of n integers nums, a 132 pattern is a subsequence of three 
# integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise, return false.


def find132pattern(nums):
    if len(nums) < 3:
        return False

    stk = []  # potential nums[j] values
    third = float('-inf')  # best nums[k] candidate so far

    for num in reversed(nums):
        if num < third:
            return True
        while stk and num > stk[-1]:
            third = stk.pop()
        stk.append(num)

    return False

print(find132pattern([1,-2,3]))
