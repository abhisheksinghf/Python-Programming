n = int(input("Enter a number : "))
flag = 0
for i in range(2,n):
    if n%i==0:
        flag = 1
        break
if flag==0:
    print("Prime ")
else:
    print("Non-Prime")