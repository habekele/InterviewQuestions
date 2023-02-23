def twosum(a,target):
   
    complementMap = dict()
 
    for count, value in enumerate(a): # i is index v is ap
        complement = target - value
        if complement in complementMap:
            return [complementMap[complement] ,count]
        complementMap[value] = count
    return


    

arr = [2,7,11,15]
print(twosum(arr,9))

