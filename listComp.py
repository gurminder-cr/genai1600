# a=[12,45,33,21]
# b=[33,32,10,11]
# print(a)
# print(b)

# for i in zip(a,b):
#     print(i)
# for i,j in zip(a,b):
#     print(i,j)
# for i,j in zip(a,b):
#     print(i+j)


# l=[]
# # print(type(l))
# for i in range(0,33):
#     if i%4==0:
#         l.append(i)
# print(l)




# for loop input
# l=[]
# for i in range(1,6):
#     j=input(f"Enter value of location {i} ")
#     l.append(j)
# print(l)


# list comprehension 
l= [i for i in range(0,33)]
# l= [i for i in range(0,33) if i%4==0]
li= [i if i%4==0 else i**2 for i in l]
print(li)

j=[input(f"Enter {i} ") for i in range(0,10)]
print(j)
