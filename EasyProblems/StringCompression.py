def get_compressed_string( s: str) :
    """
    Returns compressed string
    """
    if s.strip() == "" or s.isspace() :
        return ""
    
    curr_char = s[0]
    curr_count = 1
    res = ""
    for i in range(1, len(s)):
        if( curr_char == s[i] ):
            curr_count += 1
        else :
            res += ( curr_char + str(curr_count) )
            curr_char = s[i]
            curr_count = 1
    
    res += ( curr_char + str(curr_count) )
    return res

print( f'Compress string = "abc" value = "{get_compressed_string("abc")}" ' )
print( f'Compress string = "aaa" value = "{get_compressed_string("aaa")}" ' )
print( f'Compress string = "aaabbc" value = "{get_compressed_string("aaabbc")}" ' )
print( f'Compress string = "aaaaac" value = "{get_compressed_string("aaaaac")}" ' )

