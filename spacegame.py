# Space Warriors Game

import random
damage_list_fighter = [6, 7, 8, 9, 10, 11, 12]
damage_list_defender = [3, 4, 5, 6, 7, 8, 9]

class Spacecraft:
    def __init__(self, type, health):
        self.type = type
        self.health = health
        self.damage_fighter = random.choice(damage_list_fighter)
        self.damage_defender = random.choice(damage_list_defender)
        self.ship_destroyed = False
    def __repr__(self):
        return "This {type} spacecraft has {health} starting hit points ".format(type=self.type, health=self.health)
    def ship_destroyed(self):
        self.ship_destroyed = True
        if self.health != 0:
            self.health = 0
        print("Your spacecraft has been destroyed!")
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.ship_destroyed()
        else:
            print("Your spacecraft now has {health} hit points remaining.".format(health=self.health))
    def lose_health2(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.ship_destroyed()
        else:
            print("Your enemy spacecraft now has {health} hit points remaining".format(health=self.health))
    def attack(self, enemy_ship):
        if self.type == "fighter" and enemy_ship.type == 'defender':
            print('Your {type} spacecraft attacked the enemy ship for {damage} damage and the enemy {enemy_ship} spacecraft attacked your ship for {damage2} damage.'.format(type=self.type,
                                                                                                                                                           damage=self.damage_fighter,
                                                                                                                                                           enemy_ship=enemy_ship.type,
                                                                                                                                                           damage2=self.damage_defender))
            self.lose_health(self.damage_defender)
            enemy_ship.lose_health2(self.damage_fighter)

        #else:
         #   self.type == 'defender' and enemy_ship.type =='fighter'
          #  print(
           #     'Your {type} spacecraft attacked the enemy ship for {damage} damage and the {enemy_ship} attacked your ship for {damage2} damage.'.format(type=self.type,
            #                                                                                                                                               damage=self.damage_defender,
             #                                                                                                                                              enemy_ship=enemy_ship.type,
              #                                                                                                                                             damage2=self.damage_fighter))
           # self.lose_health(self.damage_defender)
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
player_name = input('Welcome to Space Warriors! Please enter your name and hit enter. ')
player_style = input('''
Welcome ''' + player_name + '''! Space Warriors is a game that allows you to chose between two classes of spacecraft. If you select a 
fighter spacecraft when you will fight again a defender spacecraft. If you choose a defender space craft
then you will fight a fighter spacecraft. Please select "Fighter" or "Defender" and press enter. ''').lower()

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
























