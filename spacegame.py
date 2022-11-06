# Space Warriors Game
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













