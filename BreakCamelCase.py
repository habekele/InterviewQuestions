def breakCamelCase(str):
    arr = list(str)
    arr2 = list()

    for count,value in enumerate(arr):
        if(value.isupper()):
            arr2.append(" ")
        arr2.append(value)
            
    return ''.join(arr2)

print(breakCamelCase("camelCase"))

def rot13(message):
    arr = list(message)
    for count,value in enumerate(arr):
        ordVal = ord(value)
        if((ordVal >= 65 and ordVal<=90) or(ordVal>=97 and ordVal<= 122) ):
            newVal = ord(value) + 13
            arr[count] = chr(newVal)
    
    return "".join(arr)

print(rot13("grfg#"))
        
