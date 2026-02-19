# i="    hello class     "
# print(i)
# print(i.strip()) # strip - remove extra spaces both sides 
# print(i.lstrip()) # strip - remove extra spaces left side
# print(i.rstrip()) # strip - remove extra spaces right side

# slicing 
n="Gurminder Singh"
print(n)
print(n[:])  #start stop step [] - subscriptable operator 
print(n[:5])  #start stop step [] - subscriptable operator 
print(n[1:8])  #start stop step [] - subscriptable operator 
print(n[0:11])  #start stop step [] - subscriptable operator 
print(n[::]) # step
print(n[:6:2]) # step
print(n[::-1]) # step
print(n[10:1:-1]) # step

print("========================")

for i in "jasbir":
    print(i+"-",end="")
    
print("---------------------")

print(n)
print(n.endswith("h"))
print(n.startswith("g"))

if n.startswith("G"):
    print("dfhvdsk")
    
