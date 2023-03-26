def isValid(s):
    map = {')':'(','}':'{',']':'['}
    stack = []

    for x in s:
        if x not in map:
            stack.append(x)
            
        if not stack or stack[-1] != map[x]:
            return False
        stack.pop()
    return not stack

print(isValid('{[]}'))
