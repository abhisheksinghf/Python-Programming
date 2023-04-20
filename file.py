f = open('sample.txt','r')#by default the mode is r 
data = f.read(5)#reads first 5 chars 
print(data)
f.close()