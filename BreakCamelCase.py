def breakCamelCase(str):
    arr = list(str)
    arr2 = list()

    for count,value in enumerate(arr):
        if(value.isupper()):
            arr2.append(" ")
        arr2.append(value)
            
    return ''.join(arr2)

print(breakCamelCase("camelCase"))