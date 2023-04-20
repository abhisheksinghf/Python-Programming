message = "Good Morning"
name = "Abhisheksingh"
# print(message+ name)
# c =message+ name
# print(c)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
# print(name[14]) throws error
#name[2] = 'B' #does not work in python
print(name[0:4])#this is called string slicing 
print(name[:5])#this is valid it works same as name[0:5]
print(name[0:])#prints the whole string same as [0:13]
c = name[-4:-1]#this is same as name[1:4]
print(c)
#skipping value 
d = name[1:4:2]#skips after 2 letters
print(d)
d = name[0::2]
print(d)
