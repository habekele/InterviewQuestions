#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def anagram(a: str,b: str):
    arr = list(a)  #[a.b.c]              # ['h', 'e', 'l', 'l', '0']
    arr2 = list(b) 
    arr.sort()
    arr2.sort()
    
    if(arr != arr2):
        return False
    return True

print(anagram('abc', 'cba'))
