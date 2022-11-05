# Space Warriors Game
print()
print('Welcome to Space Warriors.')
print()
player_name = input('What is your name? ')
player_style = input('''
Welcome ''' + player_name + '''! Space Warriors is a game that allows you to chose between a fighter spacecraft 
or a defender spacecraft. Each spacecraft has it's own strengths and weaknesses. Please type in 
"Fighter" or "Defender" ''')
print()
if player_style == 'Fighter':
    print('''You have selected the fighter style spacecraft. This spacecraft does remarkable damage 
    to it\'s enemies but is known to have a weaker defense system.''')
else:
    print('''You have selected the defender style spacecraft. This spacecraft is known to have a strong
defense system  but is know to do lesser damage to it\'s enemies.''')






