import random

Actions = ('Create Another Charachter', 'Roll Dice')
Dice = ('D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100')

class Player:
    Health = 0
    Strength = 0
    Constitution = 0
    def Start(Health):
        Player.Health = int(input("What is your Health? : "))
    def __init__(self, Health):
        self.Health = Player.Health

def ListActions(Actions):
    print('Actions to Choose From')
    for i in range(len(Actions)):
        print(i+1,'.', Actions[i])
    ActNum = int(input("What number from the list do you choose? : "))
    if ActNum is 2:
        ListDice(Dice)

def ListDice(Dice):
    print('Dice to Choose From')
    for i in range(len(Dice)):
        print(i+1,'.', Dice[i])
    DieNum = int(input('What die do you choose? : '))
    if DieNum is 1:
        print(random.randint(1, 4))
    elif DieNum is 2:
        print(random.randint(1, 6))
    elif DieNum is 3:
        print(random.randint(1, 8))
    elif DieNum is 4:
        print(random.randint(1, 10))
    elif DieNum is 5:
        print(random.randint(1, 12))
    elif DieNum is 6:
        print(random.randint(1, 20))
    elif DieNum is 7:
        print(random.randint(1, 100))

Player.Start(Player.Health)
player = Player(Player.Health)

while(True):
    ListActions(Actions)

