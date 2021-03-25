import random
def a():
    import completeelyricsfinal
def b():
    import tictactoe
def c():
    import quizzz
A=print('''welcome to the bored game
a random game would be played without your choosing enjoy''')
d='yes'    
while d=='yes':   
   c=random.randint(0,3)
   if c==0:
       a()
       d=input('do u want to play again(yes,no):')
   elif c==1:
       print('WELCOME TO THE RANDOM QUIZ: ')
       b()
       d=input('do u want to play again(yes,no):')
   elif c==2:
       print('WELCOME TO TIC TAC TOE: ')
       e=input('do you have second player: ')
       if e=='yes':
           c()
           d=input('do u want to play again(yes,no):')
       else:
           d=input('do u want to play again(yes,no):')
