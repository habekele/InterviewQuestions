#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
from collections import defaultdict

def GroupAnagram(strList):
    res = defaultdict(list)
    for s in strList: # for each word in the Array
        count = [0] * 26 #a....z

        for c in s:# for each letter in the word
            count[ord(c) - ord('a')]+=1
        
        res[tuple(count)].append(s)

    return res.values()

print(GroupAnagram(['cat','ape','hat','ate','tea','eat','tac']))