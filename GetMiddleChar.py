def get_middle(s):
    lens = len(s)
    middle = (lens/2)
    middleplus = middle+1
    if(lens % 2 == 0):
        return s[int(middle-1):int(middle+1)]
    else:
        return s[int(middle)]

print(get_middle("henok"))
print(get_middle("john"))
print(get_middle("abcdefg"))
print(get_middle("abcdef"))
print(get_middle("gdfsfsffd"))