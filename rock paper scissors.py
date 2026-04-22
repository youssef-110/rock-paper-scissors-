import random
rock = 'r'
paper = 'p'
sicsor = 's'
list = ['r', 'p', 's']
y = random.choices(list)
while True:
 x = str(input())
 #tie
 if x == y:
    print(x)
    print(y)
    print('tie')
 
#lost      
 if y > x:
        print(x)
        print(y)
        print("you lost")
#won
 if y == [1] and x == paper:
        print(x)
        print(y)
        print("you won")
#won
 if y == [2] and x == sicsor:
        print(x)
        print(y)
        print("you won")
#lost
 if y == [1] and x == sicsor:
        print(x)
        print(y)
        print("you lost")
#lost
 if y == [3] and x == paper:
        print(x)
        print(y)
        print("you lost") 
#won
 if y == [3] and x == rock:
        print(x)
        print(y)
        print("you won") 

