def get_two_sum(arr:list[int] ,target:int) -> tuple:
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.  
    eg: Input: nums = [2,7,11,15], target = 9  Output: [0,1]  

    """
    sum_map = {}
    for i, num in enumerate(arr):
        if (target - num) in sum_map:
            return (sum_map[target-num], i)
        else :
            sum_map[num] = i
    
    return (-1,-1)

print(get_two_sum([2,7,11,15], 9))
print(get_two_sum([3,2,4], 6))