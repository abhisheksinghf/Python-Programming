# a = {12,3,45,6,7,8}
# print(a)
# print(type(a))
# b = {12,3,1,12}#avoides repetation
# print(b)
a = {}#this is not set
print(type(a))
b = set()#this is an empty set
print(type(b))
b.add(4)
b.add(10)
b.add(10)
# b.add([2,2,5,3,1])#cannot add list throws an error
b.add((3,3,5,1))#we can add tuple
print(b)
print(len(b))
b.remove(4)
print(b.pop())#removes random number 
print(b)