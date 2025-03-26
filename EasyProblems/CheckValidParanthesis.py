def check_if_valid_seq(s : str) -> bool :
    stack = [] # can be implemented using list, deque, or lifoqueue
    for c in s:
        if c == '(' or c == '[' or c == '{' :
            stack.append(c)
        elif c == ')' :
            if stack.pop() != '(' :
                return False
        elif c == '}' :
            if stack.pop() != '{' :
                return False
        elif c == ']' :
            if stack.pop() != '[' :
                return False
    
    return len(stack) == 0

print(check_if_valid_seq("()"))
print(check_if_valid_seq("(())"))
print(check_if_valid_seq("([{}])"))
print(check_if_valid_seq("()[]{}"))
print(check_if_valid_seq("()("))
print(check_if_valid_seq("(()"))

            