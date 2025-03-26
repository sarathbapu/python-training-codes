def convert_fraction_to_recurring_decimal( num: int, den: int) -> str :
    """
    Given two integers representing the numerator and denominator of a fraction, return the fraction in string format. 
    If the fractional part is repeating, enclose the repeating part in parentheses.  
    Eg: num = 1, den = 3 op = '0.(3)'
    """
    res = ''
    if num < 0 :
        res += '-'
        num *= 1

    quot, rem = num // den, num % den
    res += str( quot )
    if rem == 0 :
        return res
    
    res += '.'
    rem_map = {} # stores remainder and indices

    while rem != 0:
        if rem in rem_map.keys():
            index = rem_map[rem] 
            res = res[:index] + '(' + res[index:] + ')'
            return res
        else :
            rem_map[rem] = len(res)
            
        num *= 10
        quot, rem = num // den, num % den
        num = rem
        res += str(quot)

    return res

print( convert_fraction_to_recurring_decimal(1,2))
print( convert_fraction_to_recurring_decimal(1,3))
print( convert_fraction_to_recurring_decimal(1,70))
print( convert_fraction_to_recurring_decimal(14,2))
print( convert_fraction_to_recurring_decimal(1,7))