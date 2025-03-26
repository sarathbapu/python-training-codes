
def gcd(min_num: int, max_num: int) -> int: 
    while min_num : 
        min_num, max_num = max_num % min_num, min_num
    return max_num

def sum_of_fractions( num1: tuple, num2: tuple) -> tuple: 
    """
    Given two valid fractions ( den != 0), find the sum of fractions in reduced form. 
    Also only num may contain signs( i -ve number)
    eg: (1,2),(1,6) => (1,3)
    """
    den = num1[1] * num2[1]
    num = num1[0] * num2[1] + num1[1] * num2[0]

    gcd_val = gcd(num if num > 0 else -num, den)
    return (num//gcd_val, den//gcd_val)

print( sum_of_fractions((1,2), (1,6)))
print( sum_of_fractions((-1,2), (1,6)))