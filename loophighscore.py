import random
import mysql.connector
mydb = mysql.connector.connect(host='localhost',user = 'root',password='admin',database='bored_button')
new=input("are you a new user:(y or no) ")
if new=='y':
    def username():
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="bored_button")
        n=input("enter username: ")
        mycursor=mydb.cursor()
        mycursor.execute("insert into login(name) values('%s')"%(n,))
    def password():
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="admin",database="bored_button")
        p=int(input("enter password: "))
        mycursor=mydb.cursor()
        mycursor.execute("insert into login(password) values(%s)"%(p,))
    username()
    password()
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
see=input("do u want to see highscore: ")
if see=='y':
    cur=mydb.cursor()
    namehere=input('enter name: ')
    s='select * from login where name="%s"'
    cur.execute(s%namehere)
    myresult=cur.fetchall()
    for i in myresult:
        print(i)
    
    
