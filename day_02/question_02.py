# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.


def productExceptSelf(arr):
    numberOfZeros=0
    idx=-1
    totalProduct=1
    for i in range(len(arr)):
        if arr[i]==0:
            numberOfZeros+=1
            idx=i
        else:
            totalProduct*=arr[i]
    res=[0]*len(arr)
    if numberOfZeros==0:
        for j in range(len(arr)):
            res[j]=totalProduct//arr[j]
    elif numberOfZeros==1:
        res[idx]=totalProduct
    return res

print(productExceptSelf([-1,1,0,-3,3]))

