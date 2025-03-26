def get_min_size_subarray( arr: list ,target:int) -> int: 
    """
    Given an array of positive integers nums and a positive integer target, return the minimal 
    length of a subarray whose sum is greater than or equal to target. 
    If there is no such subarray, return 0 instead.

    """

    left, curr_sum, min_len = 0, 0, 2e33
    
    for right in range(len(arr)):
        curr_sum += arr[right]
        
        while curr_sum >= target :
            #if curr_sum == target :  #Needed if it has to be the target
            min_len = (right - left + 1) if (right-left + 1 ) < min_len else min_len
            curr_sum -= arr[left]
            left += 1
            
    return min_len if min_len < 2e33 else 0

print(get_min_size_subarray([2,3,1,2,4,3], 7))
print(get_min_size_subarray([1,4,4], 17))
print(get_min_size_subarray([1,4,4], 4))
            
            

