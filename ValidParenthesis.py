def isValid(s):
    map = {')':'(','}':'{',']':'['}
    stack = []

    for x in s:
        if x in map:# checking to see if x is a closed parenthesis
            if stack and stack[-1]==map[x]:# if there is something is the stack and the top of the stack is the correct closing bracket
                stack.pop()#removing the open bracket
            else:
                return False# returning false
        else:
            stack.append(x)#if an open bracket then add to the stack
    return True if not stack else False #if there is still stuff in the stack then return false

print(isValid('{[]}'))
