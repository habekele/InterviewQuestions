def topKFrequent( nums, k):
    res = dict()
    tot = []
    for x in nums:
        if x in res:
            res[x]=res[x] + 1
        else:
            res[x]=1
    
    for x in range(k):
        maxi = max(res,key=lambda x:res[x])
        tot.append(maxi)
        res[maxi] = 0

    
    return tot

def topKFrequentBucketSort(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for n in nums:
        count[n] = 1 + count.get(n,0)
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq)-1,0,-1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    


print(topKFrequent([1,1,1,2,2,3],2))
print(topKFrequentBucketSort([1,1,1,2,2,3], 2))