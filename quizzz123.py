import random
high = 0
a=("what is the devil's number ?")
b=("Who is the youngest self-made 10^90?")
c=("who was mrolympia this year?")
d=("the fastest car in the world?")
e=("who won the latest chamoionship: ")
f=("who won the lattest cricket world cup")
g=("first youtube channel to get over 100 million subscribers")
h=("who is the owner of amazon? : ")
i=("this artist with over a billion dollars made by selling shoes ")
j=("this man is often called fastest man alive")
l1=[a,b,c,d,e,f,g,h,i,j]
print("welcome to the bored quiz")
z=int(input("how many times do you want to play?(1-10): "))
for x in range(z):
    print("enter number ")
    y=random.choice(l1)
    if y==a:
        high = high+1
        print(a)
        w=int(input('1-666, 2-999, 3-696, 4-969 : '))
        if w==1:
            print("correct")
           
        else:
            print("wrong")
            print("correct answer : 666")
        l1.remove(y)    

    if y==b:
        print(b)
        s=int(input("1-kylie jenner,2- jay-z 3-kim kardashian 4- travis scot : "))
        if s==1:
            high = high+1
            print("correct")
            l1.remove(y)
            
        else:
            print("wrong")
    if y==c:
        print(c)
        p=int(input('1-brandon curry 2-big ramy 3-arnold schwarenegger 4-john cena : '))
        if p==2:
            high = high+1
            print("correct")
            l1.remove(y)
           
        else:
            print("wrong")
    if y==d:
        print(d)
        m=int(input("1-maruti-800 , 2-bugatti, 3-koenigsegg, 4-ssc : "))
        if m==4:
            high = high+1
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==e:
        print(e)
        n=int(input("1-houston rockets , 2-new york yankees, 3-la lakers , 4-celtics : "))
        if n==3:
            high = high+1
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==f:
        print(f)
        k=int(input("1-new zealand ,2-india ,3-australia, 4-england: "))
        if k==4:
            high = high+1
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==g:
        print(g)
        l=int(input("1-pewdiepie , 2-mr.beast , 3-T-series , 4-ajay nagger"))
        if l==3:
            high = high+1
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==h:
        print(h)
        o=int(input("1-bill gates, 2-jeff bezos, 3-jack ma, 4-ambani"))
        if o==2:
            high = high+1
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==i:
        print(i)
        A=int(input('1-kanye west , 2-travis scot , 3-dr.dre , 4-drake : '))
        if A==1:
            high = high+1
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==j:
        print(j)
        B=int(input('1-milkha singh , 2-usain bolt, 3-tobi brown, 4-Vikas Gowda. : '))
        if B==2:
            high = high+1
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
print("thank you for playing")            
