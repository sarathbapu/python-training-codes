def get_robot_location(encodedSeq :str):
    """
    A robot can move in 4 directions up, down, left and right. 
    It's path is encoded in a string with characters U, D, L and R. 
    If the bot starts at coordinate { 0,0} then find it's final coordinate based on the input path string. 
    """
    location = [0,0]
    for c in encodedSeq.upper():
        if c == 'U':
            location[1] += 1
        elif c == 'D':
            location[1] -= 1
        elif c == 'L':
            location[0] -= 1
        elif c == 'R':
            location[0] += 1
        else :
            raise Exception("Unexpected input")
        
    return (location[0], location[1])


print( get_robot_location("UDRR"))
print( get_robot_location("DD"))
