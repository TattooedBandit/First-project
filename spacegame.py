# Space Warriors Game

import random
damage_list_fighter = [6, 7, 8, 9, 10]
fighter_damage = random.choice(damage_list_fighter)
damage_list_defender = [ 4, 5, 6, 7, 8]
defender_damage = random.choice(damage_list_defender)

class Spacecraft:
    def __init__(self, type, health):
        self.type = type
        self.health = health
        self.ship_destroyed = False
    def __repr__(self):                                             # When a ship type is printed, it's level, type, health and damage will be shown
        return "This {type} spacecraft has {health} starting hit points "/format(type=self.type, health=self.health)
    def ship_destroyed(self):                                       # Destroying a ship will flip its status to True
        self.ship_destroyed = True
        if self.health != 0:                                        # 'ship_destroyed' should only be called if health is set to 0
            self.health = 0                                         # if the ship has health left, it gets set to 0
        print("Your spacecraft has been destroyed!")
    def lose_health(self, amount):                                  # Deducts health from spacecraft and prints current health remaining
        self.health -= amount
        if self.health <= 0:                                        # Ensure health does not reach negative and destroys spacecraft
            self.health = 0
            self.ship_destroyed()
        else:
            print("Your spacecraft now has {health} hit points remaining".format(health=self.health))
    def attack(self, enemy_ship):
        if self.ship_destroyed:                                     # Checks to make sure ship is not already destroyed
            print('You cannot attack because your ship is destroyed.')
        if self.type == "Fighter":
            print('Your {type} spacecraft attacked an enemy ship for {damage} damage.'.format(type=self.type, damage=random.choice(damage_list_fighter)))
        if self.type == "Defender":
            print('Your {type} spacecraft attacked an enemy ship for {damage} damage.'.format(type=self.type, damage=random.choice(damage_list_defender)))
            enemy_ship.lose_health(self.damage)

class Player:
    def __init__(self, type, name):
        self.name = name
        self.type = type
        self.current_type = 0
    def __repr__(self):
        print('{name} you have selected the {type} spacecraft'.format(name=self.name, type=self.type))
    def attack_enemy_ship(self, enemy_ship):
        my_ship = self.type[self.current_type]
        their_ship = enemy_ship.type[enemy_ship.current_type]
        my_ship.attack(their_ship)

a = Spacecraft("Fighter", 40)
b = Spacecraft("Defender", 55)
print()
player_name = input('Welcome to Space Warriors! Please enter your name and hit enter. ')
player_style = input('''
Welcome ''' + player_name + '''! Space Warriors is a game that allows you to chose between two classes of spacecraft. 
The first selection is the fighter spacecraft. This ship does remarkable damage to it's enemies but is known to have a 
weaker defense system. The second selection is the defender spacecraft. This ship does  lesser damage that the fight 
ship but is known to have a strong defense system. Please choose which spacecraft you'd like to play by entering 
"Fighter" or "Defender" ''').lower()

while player_style != 'Fighter' and player_style != 'Defender':
    player_style = input('Whoops! It looks like you did not choose "Fighter" or "Defender". Try selecting again! ')

fighter_selected = []
defender_selected = []

if player_style == 'Fighter':
    fighter_selected.append(a)
else:
    defender_selected.append(b)

in_game_fighter = Player(fighter_selected, player_name)
in_game_defender = Player(defender_selected, player_name)

print(in_game_defender)
















