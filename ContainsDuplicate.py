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
def containsDuplicateAgian(a):
    for x in a:
        if a.count(x) > 1:
            return True
    return False

print(containsDuplicateHashMap([2,14,18,22,22]))
print(containsDuplicateAgian([2,14,18,21,22]))