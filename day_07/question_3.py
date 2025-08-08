from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0:
            return []
        dq = deque() 
        res = []
        for i in range(len(nums)):
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res

s=Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3, 3, 5, 5, 6, 7]