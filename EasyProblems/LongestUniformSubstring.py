def get_longest_uniform_substring(s : str):
    """
    Gets the longest uniform substring from given string Return start index and length 
    eg: aaabbbbccda => (3,4)

    """

    start, max_len = 0, 1
    curr_char,curr_len = s[0], 1
    for i in range(1, len(s)):
        if curr_char == s[i]:
            curr_len += 1
        else :
            if curr_len > max_len :
                start ,max_len = i - curr_len, curr_len
            curr_char,curr_len = s[i], 1
            
    if curr_len > max_len :
        start ,max_len = len(s) - curr_len, curr_len

    return (start, max_len)

print( get_longest_uniform_substring("aaabbbbccda"))
print( get_longest_uniform_substring("abcd"))
print( get_longest_uniform_substring("aaa"))
print( get_longest_uniform_substring("aaabbbb"))