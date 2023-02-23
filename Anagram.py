#Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def anagram(a: str,b: str):
    
    return sorted(a)==sorted(b)
    

print(anagram('abc', 'cba'))
