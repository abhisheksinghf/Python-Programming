import random

def gameWin(comp,you):
    if comp == 's':
        if you == 'w':
            return False
        elif
a = input("Computer Turn : Snake[s] Water[w] Gun[g] ? ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else :
    comp == 'g'
you = input("Player's Turn : Snake[s] Water[w] Gun[g] ? ")
gameWin(comp,you)