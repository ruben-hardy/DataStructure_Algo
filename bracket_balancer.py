from collections import deque

def bracket_balancer(s: str) -> bool:
    bracket_stream = deque()
    bracket_dict = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    balanced = True
    count = 0
    for char in s:
        if char in bracket_dict.values():
            bracket_stream.extend(char)
        else:
            if bracket_stream:
                temp = bracket_stream.pop()
            else:
                balanced = False
                count += 1
                continue
            if char == ']':
                if bracket_dict[char] != temp:
                    balanced = False
                    bracket_stream.extend(temp)
                    count += 1
                    #break
            elif char == '}':
                if bracket_dict[char] != temp:
                    balanced = False
                    bracket_stream.extend(temp)
                    count += 1
                    #break
            elif char == ')':
                if bracket_dict[char] != temp:
                    balanced = False
                    bracket_stream.extend(temp)
                    count += 1                    
                    #break
    if balanced and len(bracket_stream) == 0:
        print("Balanced")
        print(count)
    else:
        print('Not balanced')
        print(count + len(bracket_stream))

a = "((]))"
bracket_balancer(a)

