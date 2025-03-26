def find_trapped_water(height: list[int]) -> int :
    """
    Find the trapped water between buildings
    https://leetcode.com/problems/trapping-rain-water/description/

    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
    Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
    Output: 6
    Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

    """
    left_ptr, left_max = 0, height[0]
    right_ptr = len(height) - 1
    right_max = height[right_ptr]
    res = 0

    while left_ptr < right_ptr:
        if left_max <= right_max :
            res += left_max - height[left_ptr]
            left_ptr += 1
            left_max = left_max if left_max > height[left_ptr] else height[left_ptr]
        else :
            res += right_max - height[right_ptr]
            right_ptr -= 1
            right_max = right_max if right_max > height[right_ptr] else height[right_ptr]
    
    return res

print( find_trapped_water([0,1,0,2,1,0,1,3,2,1,2,1]))
print( find_trapped_water([4,2,0,3,2,5]))