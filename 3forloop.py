# for loop - 
# python for loop - range() - start, stop, step 

# for i in range(1,10):  # 1-10 (stop-1)
#     print("python")
# for i in range(0,10):  # 1-10 (stop-1)
#     print(i)
    
# for i in range(10):  # by default starting point - 0 
#     print(i)
    
# for i in range(2,15,3):  # step by default 1 
#     print(i)
    
    
for i in range(10,1,-1):  # reverse  stop-1 = 1-(-1)= 2
    print(i)
    
    
# for i in range(0,30):
#     if i%3==0:
#         print(i)
        
   
# multiplication table 

# number= int(input("Enter number "))
# upto= int(input("Upto "))

# for i in range(0,upto+1):
#     print(number,"*",i,"=",number*i) 


# Nested for loop
# *
# **
# ***
# ****
# *****
 
# for i in range(1,6):
#     for j in range(0,i):
#         print("*",end="")
#     print()


# strings - " ", ''

# name=input("Enter your name ")
name="Gurminder\n"
print(len(name))

# for i in range(0,len(name)):print(name)
print(name*len(name))



# variables swap 
a=10
b=20
# c=a 
# a=b 
# b=c 
a,b=b,a
print(a,b)