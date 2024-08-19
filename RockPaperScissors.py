#!/usr/bin/env python
# coding: utf-8

# # Rock Paper Scissors 

# In[1]:


import random

def tas_kagit_makas_IBRAHIM_ARDIC():
    """
    Play a game "Rock Paper Scissors" against the computer.

    User inputs:
    'r' stands for Rock
    'p' stands for Paper
    's' stands for Scissors

    Rules:
    - Rock beats Scissors
    - Paper beats Rock
    - Scissors beats Paper

    The first to win two rounds wins the game (Best of three). After each game, you can choose to play again.
    
    """
    rockPaperScissors = ['r', 'p', 's']
    
    # Mapping r, p, s
    mapping = {
        'r': 'rock',
        'p': 'paper',
        's': 'scissors'
    }

    # r beats s, p beats r, s beats p.
    dictionary = { 
        'r': {'s'},
        'p': {'r'},
        's': {'p'}
    }
    welcomeMsg = "Welcome to the Rock Paper Scissors Game"
    print(welcomeMsg, f'\nr= rock \np= paper \ns= scissors')

    compPoint = 0
    userPoint = 0
    gameCount = 1

    while(True):
        isComputerPlaying = random.randint(0,1) # 0 False, 1 True

        while(compPoint<2 and userPoint <2): 
            print(f"Round {gameCount}")
            print('-'*len(welcomeMsg))
            
            computerChoice = rockPaperScissors[random.randint(0,2)]
            userChoice = input("Please enter your choice (r,p,s): ")
            userChoice = userChoice.lower()


            
            if userChoice == computerChoice: # If draw
                print(f"Draw! Computer also chose {mapping[computerChoice]}\nPlease select again: ")
                print('-'*len(welcomeMsg))
                continue


            if userChoice == 'r': # If user choices Rock
                if computerChoice in dictionary['r']:
                    print(f"Congrats you won! Computer chose {mapping[computerChoice]}")
                    userPoint+=1
                else:
                    print(f'Computer won! Computer chose {mapping[computerChoice]}')
                    compPoint +=1

            elif userChoice == 'p': # If user choices Paper
                if computerChoice in dictionary['p']:
                    print(f"Congrats you won! Computer chose {mapping[computerChoice]}")
                    userPoint+=1

                else:
                    print(f'Computer won! Computer chose {mapping[computerChoice]}')
                    compPoint +=1

            elif userChoice == 's': # ıf user choices Scissors
                if computerChoice in dictionary['s']:
                    print(f"Congrats you won! Computer chose {mapping[computerChoice]}")
                    userPoint+=1

                else:
                    print(f'Computer won! Computer chose {mapping[computerChoice]}')
                    compPoint +=1

            else: # If user entered something different than 'r', 'p', 's'
                print("Invalid choice, please enter \n'r' for Rock\n'p' for  Paper\n's' for Scissors")
                continue
                
            gameCount +=1

            print(f"Your Score: {userPoint}\nComputer's Score: {compPoint} ")

            if userPoint ==2: # If user wins
                print("Congrats you won the game. Thanks for playing!")
                
            if compPoint ==2: # If computer wins
                print("Computer won the game. Thanks for playing!")

            print('-'*len(welcomeMsg))

        isUserPlaying = input("Do you want to play one more game?(y,n): ")



        if isUserPlaying == 'y' or isUserPlaying == 'n': # Valid input
            if isUserPlaying == 'y' and isComputerPlaying: # If both user and computer wants to replay
                compPoint =0
                userPoint =0
                gameCount =1

            elif isUserPlaying == 'n': # If user doesn't want to replay
                print("Thanks for playing!")
                break
            
            if not isComputerPlaying: # If user wants to replay but computer does not.
                print("Computer wanna vibe rn. GoodBye")
                break

        else: # Invalid input
            print("Invalid Choice")


# In[2]:


tas_kagit_makas_IBRAHIM_ARDIC()


# In[ ]:




