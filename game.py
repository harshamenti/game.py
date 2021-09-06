import random
def win(comp,you):
    if you=='s':
        if comp =='s':
            return 'draw'
        elif comp =='g':
            return 'you lose'
        elif comp =='w':
            return 'you lose'
    elif you=='w':
        if comp =='s':
            return 'you lose'
        elif comp =='g':
            return 'you won'
        elif comp =='w':
            return 'draw'
    elif you=='g':
        if comp =='s':
            return 'you won'
        elif comp =='g':
            return 'draw'
        elif comp =='w':
            return 'you lose'
    else:
        return 'you have chosen the alphabet that is out of above 3'



you = input('Your turn ')
randm = random.randint(1, 3)

if randm ==1:
    comp ="s"
elif randm ==2:
    comp ="g"
elif randm == 3:
    comp = "w" 

print(f'you have chosen "{you}" comp has choosen "{comp}" ')
W=win(comp,you)
print(W)
get.cwd