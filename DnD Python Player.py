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
        print("")
        Player.Strength = int(input("What is your Strength? : "))
        if Player.Strength >= 21:
            while Player.Strength >= 21:
                print("")
                print("That number is greater than 20.  Retype your number.")
                print("")
                Player.Strength = int(input("What is your Strength? : "))
        print("")
        Player.Dexterity = int(input("What is your Dexterity? : "))
        if Player.Dexterity >= 21:
            while Player.Dexterity >= 21:
                print("")
                print("That number is greater than 20.  Retype your number.")
                print("")
                Player.Dexterity = int(input("What is your Dexterity? : "))
        print("")
        Player.Constitution = int(input("What is your Constitution? : "))
        if Player.Constitution >= 21:
            while Player.Constitution >= 21:
                print("")
                print("That number is greater than 20.  Retype your number.")
                print("")
                Player.Constitution = int(input("What is your Constitution? : "))
        print("")
        Player.Intelligence = int(input("What is your Intelligence? : "))
        if Player.Intelligence >= 21:
            while Player.Intelligence >= 21:
                print("")
                print("That number is greater than 20.  Retype your number.")
                print("")
                Player.Intelligence = int(input("What is your Intelligence? : "))
        print("")
        Player.Wisdom = int(input("What is your Widom? : "))
        if Player.Wisdom >= 21:
            while Player.Wisdom >= 21:
                print("")
                print("That number is greater than 20.  Retype your number.")
                print("")
                Player.Wisdom = int(input("What is your Wisdom? : "))
        print("")
        Player.Charisma = int(input("What is your Charisma? : "))
        if Player.Charisma >= 21:
            while Player.Charisma >= 21:
                print("")
                print("That number is greater than 20.  Retype your number.")
                print("")
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
    def __init__(self, Health, Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma, SM, DM, CoM, IM, WM, ChM):
        self.Health = Player.Health
        self.Strength = Player.Strength
        self.Dexterity = Player.Dexterity
        self.Constitution = Player.Constitution
        self.Intelligence = Player.Intelligence
        self.Wisdom = Player.Wisdom
        self.Charisma = Player.Charisma
        self.SM = Player.SM
        self.DM = Player.DM
        self.CoM = Player.CoM
        self.IM = Player.IM
        self.WM = Player.WM 
        self.ChM = Player.ChM

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

Player.Start(Player.Health, Player.Strength, Player.Dexterity, Player.Constitution, Player.Intelligence, Player.Wisdom, Player.Charisma, Player.SM, Player.DM, Player.CoM, Player.IM, Player.WM, Player.ChM)
player = Player(Player.Health, Player.Strength, Player.Dexterity, Player.Constitution, Player.Intelligence, Player.Wisdom, Player.Charisma, Player.SM, Player.DM, Player.CoM, Player.IM, Player.WM, Player.ChM)

while(True):
    ListActions(Actions)

