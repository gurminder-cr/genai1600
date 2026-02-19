# list -  [], heterogenous data structure, indexed, ordered,, mutable(can change during run time)

# l=[23,44,33,10,22,15]
# l=[12,'hello','hi',90,9.90,True,100]
# print(l)
# print(type(l))    

# # slicing 
# print(l[:])
# print(l[:4])
# print(l[:6])
# print(l[1:6])
# print(l[1:10])
# print(l[::1])
# print(l[::2])
# print(l[::-1])
# print(l[::-2])
# print("-------------------")
# print("-------------------")
# print(l[6:1:-2])  # stop-1, -1 == 1-(-1) = 2
# print("-------------------")

# # methods and functions 

i=[34,11,100,56,43,22,10]
# print(i)
# # i.pop() by default last 
# # i.pop(4)
# # print(i)

# # i.remove(11)
# # print(i)


# # i.append([19,20])
# # i.append(19)
# i.extend([15,19,20])
# # i.extend(1000) raises error 
# print(i)

# print("Sorted list")

# i.sort()  #raises error if list if string is present in list
# print(i)

# i.insert(3,29)
# print(i)


# list comprehension 


print("slicing -----------")
print("-----------")
print("-----------")
print(i)
print(i[:])
print(i[:5])
print(i[1:])
print(i[1:6])
print(i[::1])
print(i[::-1])
print(i[1:6:-1])
print(i[6:1:-1]) # stop=1 ,  stop-(step) 1-(-1)= 2