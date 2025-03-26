def get_total_subarrays(arr: list[int], target: int) -> int :
    """
    Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
    https://leetcode.com/problems/subarray-sum-equals-k/description/

    """
    res, curr_sum, prefix_map = 0, 0, { 0 : 1 }
    for num in arr:
        prefix_sum += num
        if prefix_sum - target in prefix_map :
            res += prefix_map[prefix_sum - target]
        if prefix_sum in prefix_map:
            prefix_map[prefix_sum] += 1
        else :
            prefix_map[prefix_sum] = 1
        
        # Shortcut 
        # curr_sum += num
        # diff = curr_sum - target
        # res += prefix_map.get(diff, 0)
        # prefix_map[curr_sum] = 1 + prefix_map.get(curr_sum, 0)

    return res

        

print(get_total_subarrays([1,1,1], 2))
print(get_total_subarrays([1,1,0,0,1], 2))
print(get_total_subarrays([1,2,3], 3))
