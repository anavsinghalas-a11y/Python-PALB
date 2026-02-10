# given an array and a target value we need to identify 
# the indices of those two elements whose sum is equal to target value

def twosum(nums,target):
     n=len(nums)
     for i in range(n):
       for j in range(i+1,n):
             for k in range(i+2,n):
                 if nums[i] + nums[j] + nums[k] == target:
                    return[i,j,k]
     return[]
print(f"Result:{twosum([0,1,5,6,8,3,2,4,9,7],9)}")