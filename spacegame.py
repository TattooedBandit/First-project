# Space Warriors Game
import random
damage_list_fighter = [6, 7, 8, 9, 10]
damage_list_defender = [ 4, 5, 6, 7, 8]
class Spacecraft:
    def __init__(self, type, damage, health):
        self.type = type
        self.damage = damage
        self.health = health
        self.ship_destroyed = False
    def __repr__(self):                                             # When a ship type is printed, it's level, type, health and damage will be shown
        return "This {type} spacecraft has {health} hit points remaining and does approximately {damage} damage when attacking"/format(
            spacecraft=self.type, health=self.health, damage=self.damage)
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
        if (self.type == enemy_ship.type):
            print('Your {type} spacecraft attacked an enemy ships for {damage} damage.'.format(type=self.type, damage=self.damage))
            enemy_ship.lose_health(self.damage)

class Player:
    def __init__(self, spacecraft, type, name):
        self.spacecraft = spacecraft
        self.name = name
        self.type = type
    def __repr__(self):
        print('{name} you have selected the {spacecraft} spacecraft'.format(name=self.name, spacecraft=self.spacecraft))
    def attack_enemy_ship(self, enemy_ship):
        my_ship = self.spacecraft[self.type]
        their_ship = self.enemy_ship[self.type]
        my_ship.attack(their_ship)









    print()
    player_name = input('Welcome to Space Warriors! Please enter your name. ')
    player_style = input('''
    Welcome ''' + player_name + '''! Space Warriors is a game that allows you to chose between two classes of spacecraft. 
    The first selection is the fighter spacecraft. This ship does remarkable damage to it's enemies but is known to have a 
    weaker defense system. The second selection is the defender spacecraft. This ship does  lesser damage that the fight 
    ship but is known to have a strong defense system. Please choose which spacecraft you'd like to play by entering 
    "Fighter" or "Defender" ''').lower()
    print()
    while player_style != 'fighter' and player_style != 'defender':
        payer_style = input('Whoops, it looks like you did not chose "Fighter" or "Defender". Please try again ')
    if player_style == 'fighter':
        input('''You have selected the fighter spacecraft. As a fighter your damage output is between a range of 6 to 10 
    damage and your hit points begin at 40.''')
    else:
        input('''You have selected the defender spacecraft. As a defender your damage output is between a range of 3 and 7
    damage and your hit points begin at 50.''')













