def isPalidrome(n):
    n= n.lower()
    
    for i in n:
        if(i.isalpha() == False and i.isdigit()==False):
            n=n.replace(i, "")
    x=0
    for i in n[::-1]:
        if i != n[x]:
            return False
        x+=1
    return True
    
print(isPalidrome("sfsASD  asa  d  SAD"))
print(isPalidrome("r , ace   c  ar"))