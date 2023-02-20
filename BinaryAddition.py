def add_binary(a,b):
    sum = a+b
    sum = bin(sum)
    sum = sum[2::]
    return sum

    # sum = a+b
    # firstBin = ''
    # arr = []
    # while(sum!=1):
    #     if(sum%2!=0):
    #         #arr.append(1)
    #         sum = sum - 1
    #         firstBin = '1'+firstBin

    #     else:
    #         #arr.append(0)
    #         firstBin = '0'+firstBin
    #     sum = sum/2

    # if(sum ==1):
    #     #arr.append(1)
    #     firstBin = '1'+firstBin
    # #arr = arr[::-1]
    # #return ("".join(str(e) for e in arr))

    # return firstBin

print(add_binary(15, 2))


