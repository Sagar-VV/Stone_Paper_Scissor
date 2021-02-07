import random
while True:
    weapon = [ 'stone', 'paper' , 'scissor']

    for order,data in enumerate(weapon):
        print(order,data)
        
    user_choice = int(input('Choose your weapon : '))
    w = weapon[user_choice]
    print(w)

    opponent_choice = random.choice(weapon)

    print(opponent_choice)

    if w == opponent_choice :
        print('tie')

    elif w == 'stone' and opponent_choice == 'scissor' :
        print('you win')

    elif w == 'paper' and opponent_choice == 'stone':
        print('you win')

    elif w == 'scissor' and opponent_choice == 'paper':
        print('you win')

    else:

        print('you lose')    

# Save the record of winning
# Better output (improve interface)
# Add tab at use your weapon line
# compare the interger in another program


