def get_non_repeating_char( s : str) :
    """
    A function to return the first non repeating Character from the string ese returns 0
    """
    map = dict()
    for char in s: 
        if char in map.keys() :
            map[char] += 1
        else :
            map[char] = 1
    for char in map.keys() :
        if map[char] == 1 :
            return char
    return '0'

print( get_non_repeating_char("sara") )
print( get_non_repeating_char("aaa") )
print( get_non_repeating_char("ababa") )
print( get_non_repeating_char("aaac") )