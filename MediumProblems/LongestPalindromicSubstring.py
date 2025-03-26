def get_longest_palin_substring( s: str) -> str:
    """
    Given a string, find the longest substring which is palindrome. 
    For example, if the given string is “forgeeksskeegfor”, the output should be “geeksskeeg”.
    """
    
    if len(s) <= 1:
        return s
        
    max_len=1
    res=s[0]
    dp = [[False for _ in range(len(s))] for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
        for j in range(i):
            if s[j] == s[i] and (i-j <= 2 or dp[j+1][i-1]): 
                dp[j][i] = True
                if i-j+1 > max_len:
                    max_len = i-j+1
                    res = s[j:i+1]
    return res

print( get_longest_palin_substring("racecar"))
print( get_longest_palin_substring("forgeeksaskeegfor"))