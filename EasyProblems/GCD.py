
def gcd(min_num, max_num): 
    while min_num : 
        min_num, max_num = max_num % min_num, min_num
    return max_num

def get_array_minmax_gcd(arr : list):
    #return gcd(min(arr), max(arr))
    min_num, max_num = 2e33, -2e33
    for i in arr:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return gcd(min_num, max_num)

print( f"GCD of [3,4] is {gcd(3,4)}")
print( f"GCD of [4,12] is {gcd(4,12)}")
print( f"GCD of min max of arr is [2,5,6,9,10] {get_array_minmax_gcd([2,5,6,9,10])}")
print( f"GCD of min max of arr is [7,5,6,8,3] {get_array_minmax_gcd([7,5,6,8,3])}")