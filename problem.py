
# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.

# Follow up: If you have figured out the O(n) solution, 
# try coding another solution using the divide and conquer 
# approach, which is more subtle.



def max_subarray(nums):
    """Given an integer array nums, find the contiguous subarray ."""

    largest_sum = 0 


    for num in nums:
        
        
    # if len(nums) == 1:
    #     return 





print(max_subarray([1])) #1
print(max_subarray([-1])) #-1
print(max_subarray([0])) #0
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4])) #6,  [4,-1,2,1]
