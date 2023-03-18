def find_it(seq):

    hasMap = dict()
    for x in seq:
        if x in hasMap:
            hasMap[x]+=1
        else:
            hasMap[x]=1
    for x in hasMap:
        if (hasMap[x]%2)!= 0:
            return x
    return None

print(find_it([1,1,2,2,3,3,4,4,4,4,4]))
