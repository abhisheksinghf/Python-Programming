# a = input("Enter your name : ")
# print("Good Morning "+a)
letter = '''Dear name 
        You are selected 
        date'''
name = input("Enter your name : ")
date = input("Enter date : ")
letter = letter.replace("name",name)
letter = letter.replace("date",date)
print(letter)