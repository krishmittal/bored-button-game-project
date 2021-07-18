import random
def a():
    import completeelyricsfinal123withhighscore
def b():
    import tictactoe
def c():
    import quiz_highscore
A=print('''welcome to the bored game
a random game would be played without your choosing enjoy''')
d='yes'    
while d=='yes':
    e=random.randint(0,3)
    if e==0:
        a()
        d=input('do u want to play again(yes,no):')
    elif e==1:
       print('WELCOME TO THE RANDOM QUIZ: ')
       c()
       d=input('do u want to play again(yes,no):')
    elif e==2:
       print('WELCOME TO TIC TAC TOE: ')
       t=input('do you have second player: ')
       if t=='yes':
           b()
       else:
           d=input('do u want to play again(yes,no):')
