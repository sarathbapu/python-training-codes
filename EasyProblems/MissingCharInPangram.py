from string import ascii_lowercase

def get_missing_char( s : str) :
    """
    find the missing characters from a given string to make it pangram 
    """
    s = s.lower()
    map = {}
    for c in ascii_lowercase :
        map[c] = 0
    
    for c in s :
        if c in ascii_lowercase: 
            map[c] += 1
    
    res = ""
    for c in map.keys():
        if map[c] == 0:
            res += c
    
    return res if len(res) > 0 else "-1"

print( get_missing_char("The quick brown fox jumps over a lazy dog") )
print( get_missing_char("The quick brown jumps over a lazy dog") )
    

