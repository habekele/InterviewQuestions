def twosum(a,target):
   
    complementMap = dict()
 
    for count, value in enumerate(a): # i is index v is ap
        complement = target - value
        if complement in complementMap:
            return [complementMap[complement] ,count]
        complementMap[value] = count
    return


    

arr = [2,1,5,3]
print(twosum(arr,7))

