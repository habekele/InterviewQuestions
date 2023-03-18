def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    # your code here
    result = []
    for x in range(a,b+1):
        sum = 0
        string = str(x)
        for count,value in enumerate(string):
            new = pow(int(value),count+1)
            sum=sum+new
        if sum == x:
            result.append(sum)
    return result

print(sum_dig_pow(1, 89))