def topKFrequent( nums, k):
    res = dict()
    tot = []
    for x in nums:
        if x in res:
            res[x]=res[x] + 1
        else:
            res[x]=1
        if res[x] >= k:
            tot.append(x)
    
    return set(tot)

print(topKFrequent([1,2,3,3,4,5,5],2))