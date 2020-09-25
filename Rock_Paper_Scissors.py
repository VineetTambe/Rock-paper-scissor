import getpass
# import pygame 
import time 


gameover = False

quit = 1 
while quit :
    
    gameover = False
    while not gameover:
        print("Enter : 'R' for rock \n\t'P' for paper\n\t'S' for scissor\n")
        player1 = getpass.getpass(prompt='Enter player 1 input : ')
        player2 = getpass.getpass(prompt='Enter player 2 input : ')
        
        player1 = player1.lower()
        player2 = player2.lower()
        print('')
        
        if player1 == 'r':
            
            if player2 == 'r':
                print("Rock thrown by both players ... please try again!")
                time.sleep(2)
                continue
                time.sleep(2)
            
            elif player2=='p' :
                print("Player 2 wins !")
                gameover = True
                time.sleep(2)
                break
            
            elif player2=='s' :
                print("Player 1 wins!")
                gameover = True
                time.sleep(2)
                break
        
            else :
                print("Wrong input please try again!")
                time.sleep(2)
                continue
        
        elif player1=='p':
        
            if player2=='r':
                print("Player 1 wins!")
                gameover = True
                time.sleep(2)
                break
        
            elif player2=='p':
                print("Paper thrown by both players ... please try again!")
                time.sleep(2)
                continue
        
            elif player2=='s':
                print("Player 2 wins!")
                gameover = True
                time.sleep(2)
                break
        
            else:
                print("Wrong input please try again!")
                time.sleep(2)
                continue
        
        elif player1=='s':
        
            if player2=='r':
                print("Player 2 wins!")
                gameover = True
                time.sleep(2)
                break
        
            elif player2=='p':
                print("Player 1 wins!")
                gameover = True
                time.sleep(2)
                break
        
            elif player2=='s':
                print("Scissor thrown by both players ... please try again!")
                time.sleep(2)
                continue
        
            else:
                print("Wrong input please try again!")
                time.sleep(2)
    print('')
    quit = input('Enter 1 to continue 0 to quit :')