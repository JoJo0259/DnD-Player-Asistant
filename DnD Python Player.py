import random

Actions = ('Create Another Charachter', 'Roll Dice')
Dice = ('D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100')

class Player:
    Health = 0
    Strength = 0
    Dexterity = 0
    Constitution = 0
    Intelligence = 0
    Wisdom = 0
    Charisma = 0
    SM = 0
    DM = 0
    CoM = 0
    IM = 0
    WM = 0
    ChM = 0
    def Start(Health, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, SM, DM, CoM, IM, WM, ChM):
        Player.Health = int(input("What is your Health? : "))
        Player.Strength = int(input("What is your Strength? : "))
        Player.Dexterity = int(input("What is your Dexterity? : "))
        Player.Constitution = int(input("What is your Constitution? : "))
        Player.Intelligence = int(input("What is your Intelligence? : "))
        Player.Wisdom = int(input("What is your Widom? : "))
        Player.Charisma = int(input("What is your Charisma? : "))
        Player.SM = Player.Strength - 10
        Player.SM = Player.SM / 2
        Player.DM = Player.Dexterity - 10
        Player.DM = Player.DM / 2
        Player.CoM = Player.Constitution - 10
        Player.CoM = Player.CoM / 2
        Player.WM = Player.Wisdom - 10
        Player.WM = Player.WM / 2
        Player.IM = Player.Intelligence - 10
        Player.IM = Player.IM / 2
        Player.ChM = Player.Charisma - 10
        Player.ChM = Player.ChM / 2
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

