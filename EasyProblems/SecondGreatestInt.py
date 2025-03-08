def get_second_greatest(arr : list) :
    """
    Determine the second greatest numer from teh given list in O(n) time 
    """
    if arr is None or len(arr) < 2:
        return -1
    
    second_largest, largest = -2e33, -2e32

    for i in arr :
        if i > largest:
            second_largest, largest = largest, i
        elif i < largest and i > second_largest :
            second_largest = i
    
    return second_largest

print( get_second_greatest([9,3,5,8,4,7,8]) )
print( get_second_greatest([3,9,8,8,5,3,3]) )
print( get_second_greatest([2,5]) )
print( get_second_greatest([1]) )
