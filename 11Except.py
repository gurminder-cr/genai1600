# Exception Handling 
# Errors - syntax error and second is logical error 

i=int(input("Enter i "))
j=int(input("Enter j "))

# print(i/j)
l=[23,14,56]
try:
    print(i/j)
    print(l[4])
except Exception as e:
    print("Error is-",e)
# except ZeroDivisionError as e:
#     print("Error")
# except IndexError as i:
#     print(i)
finally:
    print("Always Executed")

print("Important Line")