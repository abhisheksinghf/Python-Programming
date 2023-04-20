s1 = int(input("Enter Marks of Subject 1 : "))
s2 = int(input("Enter Marks of Subject 2 : "))
s3 = int(input("Enter Marks of Subject 3 : "))

if(s1 < 33 or s2 < 33 or s3 < 33):
    print("Fail")
elif(s1+s2+s3)/3 < 40:
    print("You are Fail coz marks less than 33% ")
else:
    print("Pass")