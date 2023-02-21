def count(str):
    d = {}
    for key in str:
        if(key not in d):
            d[key] = 1
        else:
            d[key] += 1
    return d

sent = 'abcaaacsdf'

print(count(sent))