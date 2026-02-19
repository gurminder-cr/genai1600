# # Python - Data Structure Types List, tuple, Sets, Dictionary
# # List - []
# # tuple - ()
# # Sets - {}
# # Dictionary -{}

# # indexed, ordered, imutable(cannot change during run time), heterogenous 

# a=(12,True, 5.43, 'Hello',100)
# print(a)
# print(type(a))

# # i=(10,)
# # print(type(i))


# t=(12,10,15,199,43,88)
# print(t)
# print(t[:])
# print(t[:3])
# print(t[1:5])
# print(t[::-1])

# # t[1]=100 # 'tuple' object does not support item assignment

# t=list(t)
# # print(t)
# t[1]=100
# t=tuple(t)
# print("----------")
# print(t)



# sets 
# {}, heterogenous, unordered(index nahi hai), unique elements 

# s={10,'Hello','hi',100,23,9.98,23,14,10,98}
# print(s)

# # print(s)
# s.add(45) # This has no effect if the element is already present.
# s.add(100) # This has no effect if the element is already present.
# print(s)

# # s.update([12,13,14])
# # s.update([12,13,14])
# s.update({12,13,14,1,True})
# print(s)



# s.remove(45)
# # Remove an element from a set; it must be a member.
# # If the element is not a member, raise a KeyError.
# print(s)


# s.discard(1000)  #Remove an element from a set if it is a member.
# print(s)

# s.pop()
# s.pop()
# print(s)

# s.clear()
# print(s)


# l={}
# # l=set()
# # print(type(l))
# # l.update({10,23,4})
# # print(l)


# a={12,13,43,10}
# b={98,77,45,10}
# print(a.union(b))
# print(a.intersection(b))


# dictionary 
# key value pair  {}, key:value (koi bhi datatype ho skti hai)

d={'name':'Jasbir','rollno':123,'class':'btech','isownapet':True}
print(d)

# access 
print(d['name'])
# print(d['names'])

# print(d.get('names','Not present'))

d.update(hobbies='playing football')
d.update(rollno=100)

d['class']='Btech CSE'
d['marks']=88
print(d)



d.pop('marks')
print(d)

# print(d.keys())
# print(d.values())
# print(d.items())


# for i in d.items():
#     print(i)
for i,j in d.items():
    print(i,"==",j)
    

    