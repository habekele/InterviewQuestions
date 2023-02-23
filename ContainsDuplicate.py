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
print(containsDuplicate([2,14,18,22,22]))
    