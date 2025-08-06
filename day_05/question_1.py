class Solution(object):
    def binarySearch(self,nums,start,end,key):
        if start>end:
            return -1
        mid=(start+end)//2
        if nums[mid]==key:
            return mid
        elif key<nums[mid]:
            return self.binarySearch(nums,start,mid-1,key)
        return self.binarySearch(nums,mid+1,end,key)
    def search(self, nums, target):
        return self.binarySearch(nums,0,len(nums)-1,target)

sol = Solution()
nums = [1, 3, 5, 7, 9, 11]
target = 9
result = sol.search(nums, target)
print("Index:", result) 