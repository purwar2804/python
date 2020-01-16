def find_nine(nums):
    if(len(nums)<=4 and 9 in nums):
        return True
    elif(9 in nums[0:4]):
        return True
    else:
        return False
        
    

nums=[1,9,4,5,6]
print(find_nine(nums))
