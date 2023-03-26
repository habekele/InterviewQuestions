# # for i, char in enumerate(list(range(100))):
# #     if char == 50:
# #         print(f"index of 50 is: {i}")

# # i = 0
# # while i < 50:
# #     print(i)
# #     i += 1
    
# # else:
# #     print('done all the work')

# # my_list = [1,2,3]
# # for item in my_list:
# #     continue
# #     print(item)

# # i = 0
# # while i < len(my_list):
# #     print(my_list[i])
# #     i+=1

# # while True:
# #     response = input('say something: ')
# #     if(response=='bye'):
# #         break


# # picture = [
# #     [0,0,0,1,0,0,0],
# #     [0,0,1,1,1,0,0],
# #     [0,1,1,1,1,1,0],
# #     [1,1,1,1,1,1,1],
# #     [0,0,0,1,0,0,0],
# #     [0,0,0,1,0,0,0],

# # ]
# # for image in picture:
# #     for pixel in image:
# #         if pixel:
# #             print('*',end='')
# #         else:
# #             print(' ',end='')
# #     print('')


# # some_list = ['a','b','c','b','d','m','n','n']

# # def find_dup(a):
# #     duplicate = []
# #     for item in some_list:
# #         if some_list.count(item) > 1 and item not in duplicate:
# #             duplicate.append(item)
# #     print (duplicate)

# # find_dup(some_list)

# # def say_hello(name='default', id=0):
# #     print(f'hello {name}, ID: {id}')

# # say_hello("Henok", 25)
# # say_hello("Tru", 26)
# # say_hello(id = 75, name='John')
# # say_hello()
# # say_hello('Tony')

# def sum(num1, num2):
#     def another_func(n1,n2):
#         return n1 + n2
#     return another_func(num1, num2)

# print(sum(12, 22))

def test(a):
    '''
    Info: This function tests and prints param a
    '''
    print(a)

help(test)
print(test.__doc__)