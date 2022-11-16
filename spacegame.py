# Space Warriors Game
import random
import time
class Spacecraft:
    def __init__(self, type, health):
        self.type = type
        self.health = health
        self.ship_destroyed = False

    def __repr__(self):
        return "This {type} spacecraft has {health} starting hit points ".format(type=self.type, health=self.health)

    def ship_gone(self):
        self.ship_destroyed = True
        if self.health != 0:
            self.health = 0
        print()
        print("Your spacecraft has been destroyed!")
        raise SystemExit

    def ship_gone_def(self):
        self.ship_destroyed = True
        if self.health != 0:
            self.health = 0
        print()
        print("The enemy spacecraft has been destroyed! YOU WON!!")
        raise SystemExit

    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.ship_gone()
        else:
            print("Your spacecraft now has [{health}] hit points remaining.".format(health=self.health))

    def lose_health_def(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.ship_gone_def()
        else:
            print("The enemy spacecraft now has [{health}] hit points remaining.".format(health=self.health))

    def attack(self, enemy_ship):
        while True:
            damage_fighter = random.randrange(2, 8)
            damage_defender = random.randrange(2, 6)
            if self.type == "fighter":
                #time.sleep(1)
                print('Your {type} spacecraft attacked the enemy ship for {damage} damage!'.format(type=self.type, damage=damage_fighter))
                #time.sleep(1)
                enemy_ship.lose_health_def(damage_fighter)
                #time.sleep(1)
                print('The enemy {enemy_ship} spacecraft attacked your ship for {damage2} damage!'.format(enemy_ship=enemy_ship.type, damage2=damage_defender))
                #time.sleep(1)
                self.lose_health(damage_defender)
                print()

            elif self.type == "defender":
                #time.sleep(1)
                print('Your {type} spacecraft attacked the enemy ship for {damage} damage!'.format(type=self.type, damage=damage_defender))
                #time.sleep(1)
                enemy_ship.lose_health_def(damage_defender)
                #time.sleep(1)
                print('The enemy {enemy_ship} spacecraft attacked your ship for {damage2} damage!'.format(enemy_ship=enemy_ship.type, damage2=damage_fighter))
                #time.sleep(1)
                self.lose_health(damage_fighter)
                print()


class Player:
    def __init__(self, type):
        self.type = type
        self.current_type = 0

    def attack_enemy_ship(self, enemy_ship):
        my_ship = self.type[self.current_type]
        their_ship = enemy_ship.type[enemy_ship.current_type]
        my_ship.attack(their_ship)

a = Spacecraft("fighter", 40)
b = Spacecraft("defender", 50)

print()
player_name = input('''Welcome to SPACE WARRIORS! Please enter your name and hit enter. ''')
print('''
Welcome ''' + player_name + '''! Space Warriors is a game that allows you to chose one of two spacecrafts and battle it out with 
the CPU! There are two classes: Fighter Class and a Defender Class. Each class is unique in it's own way.''')
print()
player_style = input('Please type in "Fighter" or "Defender" and press enter. ''').lower()
print()
if player_style == 'fighter':
    print('You have selected the fighter class which has 40 life and does 2 - 8 damage. Goodluck!')
    time.sleep(2)
elif player_style == 'defender':
    print('You have selected the defender class which has 50 life and does 2 - 6 damage. Goodluck!')
    time.sleep(2)
else:
    print('Wrong selection. Restart the game')
    raise SystemExit

player_selected = []
computer_selected = []

if player_style == 'fighter':
    player_selected.append(a)
    computer_selected.append(b)
else:
    player_selected.append(b)
    computer_selected.append(a)

live_player = Player(player_selected)
computer_player = Player(computer_selected)

print()
print("Let's get ready to fight! Both ships are launched!")
print()

live_player.attack_enemy_ship(computer_player)
