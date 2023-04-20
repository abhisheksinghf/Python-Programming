def gretest(a,b,c):
    if(a>b and a>c):
        print("A is Gretest")
    elif(b>c):
        print("B is Gretest")
    else:
        print("C is Gretest")
a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : "))
gretest(a,b,c)
