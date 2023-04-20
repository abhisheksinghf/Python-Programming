n = int(input("Enter a number : \n"))
f = 1
sum=0
for i in range(1,n+1):
    f = f * i
    sum = sum + i
print(f)
print(sum)