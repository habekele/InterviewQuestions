# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print(f"index of 50 is: {i}")

# i = 0
# while i < 50:
#     print(i)
#     i += 1
    
# else:
#     print('done all the work')

# my_list = [1,2,3]
# for item in my_list:
#     continue
#     print(item)

# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i+=1

# while True:
#     response = input('say something: ')
#     if(response=='bye'):
#         break


# picture = [
#     [0,0,0,1,0,0,0],
#     [0,0,1,1,1,0,0],
#     [0,1,1,1,1,1,0],
#     [1,1,1,1,1,1,1],
#     [0,0,0,1,0,0,0],
#     [0,0,0,1,0,0,0],

# ]
# for image in picture:
#     for pixel in image:
#         if pixel:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print('')


some_list = ['a','b','c','b','d','m','n','n']

def find_dup(a):
    duplicate = []
    for item in some_list:
        if some_list.count(item) > 1 and item not in duplicate:
            duplicate.append(item)
    print (duplicate)

find_dup(some_list)