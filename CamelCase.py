def CamelCase(text: str):

    a = list(text)
    for count,value in enumerate(a):
        if value == '-' or value == '_':
            a[count+1] = a[count+1].capitalize()
            a.pop(count)


    return ''.join(a)

print(CamelCase('tes_dsf-dfs'))