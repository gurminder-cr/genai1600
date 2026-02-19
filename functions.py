# functions - user defined functions, pre-defined
# pre defined - input(), sum(), print() 
# to make functions use keyword - def 

# def func1():
#     print("Hello this is a function")
    
# func1()

# function with arguments/parameters
# def func2(a,b):  # parameters
#     # print(a,b)
#     print(a+b)
    
# # func2(10,12)

# i=int(input("Enter i "))
# j=int(input("Enter j "))
# func2(i,j)

# function with return 

# def myfunc(a,b):
#     # print(a+b)
#     return a+b
    
# print(myfunc(11,12))



# function with default paramter 

# def myfunc1(a,b=20):
#     print(a*b)
    
# myfunc1(10,12)

# function with keyword argument 

# def keyFunc(a,b,c):
#     print(a,b,c)
    
# keyFunc(c=10,b=20,a=30)


# def oddEven(a):
#     if a%2==0:
#         return "Even"
#     else:
#         return "Odd"
    
# number= int(input("Enter number "))
# # ans= oddEven(number)
# # print(ans)
# print(oddEven(number))


# arbitrary arguments-  *args
# def numberSum(*a):
#     print(a)
#     sum=0 
#     for i in a:
#         sum+=i
#     print(sum)
    
# numberSum(12,13)
# numberSum(12,13,14)
# numberSum(12,13,14,15)
# numberSum(12,13,14,15,19,)
# numberSum(12,13,14,15,19,20)
    
    
# keyword arbitrary - **kwargs 

def keywordArb(**a):
    print(a)

keywordArb(a=10,b=20)
keywordArb(a=10,b=20,c=30)
keywordArb(a=10,b=20,c=30,d=23)
keywordArb(a=10,b=20,c=30,d=23,e=45)


def listNum(a):
    print(a)
    
listNum([12,13,45,67,88])