# Question 4: Permission Checker
# A user has user_permissions = {"read", "write"}. The admin requirements for a folder are admin_reqs = {"read", "write", "execute"}.
# •	Task: Use a method to check if the user has all the permissions required for admin access (Is the user's set a subset of the requirements?).
# •	Task: Find the specific permissions the user is missing 

user_permissions = {"read", "write"}
admin_reqs = {"read", "write", "execute"}

print(admin_reqs.difference(user_permissions))

print(user_permissions.issubset(admin_reqs))



logs = {
    "404": [10, 12, 15, 20],
    "500": [12, 20, 22, 25],
    "403": [10, 20, 30]
}


# s= {i for i in logs['500'] if i not in logs['404']}
s= {i for i in logs['404'] if i in logs['403'] and i in logs["500"]}
print(s)