def smallest_subarray(arr,x):
    n=len(arr)
    current_num=0
    left=0
    num_lenght=n+1
    for right in range(n):
       current_num +=arr[right]
    while current_num>x:
       minimum_len=min(num_lenght,right-left+1)
       current_num -=arr[left]
       left +=1
    return minimum_len if minimum_len != n+1 else -1    #! use for not equal to n+1
arr=[1,10,5]
x=11
result=smallest_subarray(arr,x)
print("smallest subarray length is:",result)