def count_bits(n):
    bit = bin(n)[2::]
    total = 0
    for x in str(bit):
        total+=int(x)
    return total
    

print(count_bits(1234))