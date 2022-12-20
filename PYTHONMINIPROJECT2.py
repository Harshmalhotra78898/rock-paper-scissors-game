import random
import getpass
numberofrounds=int(input("NUMBER OF ROUNDS "))
choiceofplay=int(input("TYPE '1' FOR SINGLEPLAYER AND TYPE '2' FOR MULTIPLAYER"))
if choiceofplay==1:
    yourscore=0
    compscore=0
    for i in range(1,numberofrounds+1):
        computerchoice=random.randint(1,3)
        if computerchoice==1:
            comp="ROCK"
        elif computerchoice==2:
            comp="PAPER"
        else:
            comp="SCISSOR"
        you=input("ENTER YOUR CHOICE :- ROCK , PAPER OR SCISSOR ; 'CHOICES ARE CASE SENSITIVE , USE CAPITAL LETTERS ONLY'  ")
        if comp==you:
         print('TIE')
        elif comp=='ROCK':
            if you=='PAPER':
                print('YOU WIN')
                yourscore+=1
            elif you=='SCISSOR':
                print('YOU LOSE')
                compscore+=1
        elif comp=='PAPER':
            if you=='ROCK':
                print('YOU LOSE')
                compscore+=1
            elif you=='SCISSOR':
                print('YOU WIN')
                yourscore+=1
        elif comp=='SCISSOR':
            if you=='PAPER':
                print('YOU LOSE')
                compscore+=1
            elif you=='ROCK':
                print('YOU WIN')
                yourscore+=1
    if yourscore==compscore:
        print("YOUR SCORE =",yourscore)
        print("COMPUTER SCORE =",compscore)
        print(" RESULT :- TIE")
    elif yourscore<compscore:
        print("YOUR SCORE =",yourscore)
        print("COMPUTER SCORE =",compscore)
        print(" RESULT :- YOU LOSE")
    else:
        print("YOUR SCORE =",yourscore)
        print("COMPUTER SCORE =",compscore)
        print(" RESULT :- YOU WIN")

elif choiceofplay==2:
    player1=getpass.getpass("PLAYER 1 ENTER YOUR CHOICE :- ROCK , PAPER OR SCISSOR ; 'CHOICES ARE CASE SENSITIVE , USE CAPITAL LETTERS ONLY'  ")
    player2=input("PLAYER 2 ENTER YOUR CHOICE :- ROCK , PAPER OR SCISSOR ; 'CHOICES ARE CASE SENSITIVE , USE CAPITAL LETTERS ONLY'  ")
    player1score=0
    player2score=0
    for i in range(1,numberofrounds+1):
        if player1==player2:
         print('TIE')
        elif player1=='ROCK':
            if player2=='PAPER':
                print('PLAYER 2 WIN')
                player2score+=1
            elif player2=='SCISSOR':
                print('PLAYER 1 WIN')
                player1score+=1
        elif player1=='PAPER':
            if player2=='ROCK':
                print('PLAYER 1 WIN')
                player1score+=1
            elif player2=='SCISSOR':
                print('PLAYER 2 WIN')
                player2score+=1
        elif player1=='SCISSOR':
            if player2=='PAPER':
                print('PLAYER 1 WIN')
                player1score+=1
            elif player2=='ROCK':
                print('PLAYER 2 WIN')
                player2score+=1
    if player1score==player2score:
        print("PLAYER 1 SCORE =",player1score)
        print("PLAYER 2 SCORE =",player2score)
        print(" RESULT :- TIE")
    elif player1score<player2score:
        print("PLAYER 1 SCORE =",player1score)
        print("PLAYER 2 SCORE =",player2score)
        print(" RESULT :- PLAYER 2 WIN")
    else:
        print("PLAYER 1 SCORE =",player1score)
        print("PLAYER 2 SCORE =",player2score)
        print(" RESULT :- PLAYER 1 WIN")
