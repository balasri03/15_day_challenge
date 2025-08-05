# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

from collections import defaultdict
def subarraySum(nums, k):
    n=len(nums)
    mpp=defaultdict(int)
    presum=0
    cnt=0
    mpp[0]=1
    for i in range(n):
        presum=presum+nums[i]
        remove=presum-k
        cnt=cnt+mpp[remove]
        mpp[presum]+=1
    return cnt

print(subarraySum([1,2,3],3))
