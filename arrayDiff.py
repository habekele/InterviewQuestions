def array_diff(a, b):
    for x in b:
        while(x in a)== True:
            a.remove(x)
    return a
    
diff1 = array_diff([1,2,2,3,3,4,5,4,3,2,1,5,4,6,7,0], [2,3,4])
print(diff1)