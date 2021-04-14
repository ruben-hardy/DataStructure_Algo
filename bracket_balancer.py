from collections import deque

def bracket_balancer(s: str) -> bool:
    bracket_stream = deque()
    bracket_dict = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    balanced = True
    for char in s:
        if char in bracket_dict.values():
            bracket_stream.extend(char)
        else:
            temp = bracket_stream.pop()
            if char == ']':
                if bracket_dict[char] != temp:
                    balanced = False
                    break
            elif char == '}':
                if bracket_dict[char] != temp:
                    balanced = False
                    break
            elif char == ')':
                if bracket_dict[char] != temp:
                    balanced = False
                    break
    if balanced:
        print("Balanced")
    else:
        print('Not balanced')

a = "[{[()])}]]"
bracket_balancer(a)

