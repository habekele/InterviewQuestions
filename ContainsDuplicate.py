#Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

def containsDuplicate(a):
    a.sort()
    next = 0
    length = len(a)-1
    for count,value in enumerate(a):
        if(next < length):
            next = count+1
            if(value == a[next]):
                return True
        
    return False

def containsDuplicateHashMap(a):

    hashMap = dict()
    for count,value in enumerate(a):
        if value in hashMap:
            return True
        hashMap[value] = count

    return False


print(containsDuplicateHashMap([2,14,18,22,22]))
    