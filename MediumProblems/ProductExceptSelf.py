def get_product_array_except_self(arr:list[int]) -> list[int] :
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the 
    product of all the elements of nums except nums[i].
    """
    res = [1 for _ in range(len(arr))]

    for i in range(1, len(arr)):
        res[i] = res[i-1] * arr[i-1]
    
    right = 1
    for i in range( len(arr)-1, -1,-1):
        res[i] *= right
        right *= arr[i]
    return res

print(get_product_array_except_self([1,2,3,4]))
print(get_product_array_except_self([-1,1,0,3,-3]))
print(get_product_array_except_self([1,-1,2]))
