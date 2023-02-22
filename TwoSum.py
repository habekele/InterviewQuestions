def twosum(a,target):
   
   
#brute force
    # for i in range(len(a)):
    #     for j in range(i+1, len(a)):
    #         sum = a[i] + a[j]
    #         if(sum==target):
    #             return [ i,j]
    complementMap = dict()
 
    for i in range(len(a)):
        complement = target - a[i]
        if a[i] in complementMap:
            return [complementMap[complement],i]
        else:
            complementMap[complement] = i


    

array = [3,2,3,4]
print(twosum(array,6))

