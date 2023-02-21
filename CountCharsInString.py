def counter(str):
    d = {}
    if str == '':
        return d

    array = []
    for x in str:
        array.append(x)
    
    for key in array:
        if(d.get(key)==None):
            d[key] = 1
            print(d.get(key))
        else:
            count = d.get(key)+1
            d[key] = count
    return d

sent = 'abca'

print(counter(sent))