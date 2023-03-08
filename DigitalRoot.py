def digital_root(n):
    arr = list(str(n))
    if len(arr) == 1:
        return int(arr[0])
    while(len(arr)>1):
        sum = 0
        for count,value in enumerate(arr):
            sum = sum + int(value)
        arr = list(str(sum))
    return sum

def recursive_digital_root(n):
    if n <=9:
        return n
    sum = 0
    for x in str(n):
        sum = sum + int(x)
    
    return recursive_digital_root(sum)
print(digital_root(9))
print(recursive_digital_root(1019))