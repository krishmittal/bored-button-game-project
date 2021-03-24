import random
a=("What do you want from me? Why don't you ____ from me?")
b=("Workin' on the ______ like usual Way off in the deep end like usual")
c=("You like my hair? Gee, thanks, just ______ it I see it, I like it, I want it, I got it (yeah)")
d=("Wash us in the ____ (ooh) Drop this for the thugs (ah)")
e=("Ay, I remember syrup sandwiches and ______ allowances")
f=("Man I'm the mocho like ______ The choppa go Oscar for Grammy")
g=("This is ______ Don't catch you slippin' now")
h=("I'm tryna put you in the worst ____, ah P1 cleaner than your church shoes, ah")
i=("I got the ______ in the back ______ tack is attached")
j=("You're changing, I can't stand it My _____ can't take this damage")
l1=[a,b,c,d,e,f,g,h,i,j]
print("welcome to complete the lyrics")
z=int(input("how many times do you want to play?(1-10): "))
for x in range(z):
    print("complete the lyric")
    print("enter number ")
    y=random.choice(l1)
    if y==a:
        print(a)
        w=int(input('1-run, 2-hide, 3-play, 4-stand : '))
        if w==1:
            print("correct")
            l1.remove(y)
            
        else:
            print("wrong")
    if y==b:
        print(b)
        s=int(input("1-weekend,2-sunday3-monday4-saturday : "))
        if s==1:
            print("correct")
            l1.remove(y)
            
        else:
            print("wrong")
    if y==c:
        print(c)
        p=int(input('1-dye2-bought3-byed4-washed : '))
        if p==2:
            print("correct")
            l1.remove(y)
           
        else:
            print("wrong")
    if y==d:
        print(d)
        m=int(input("1-rain , 2-water, 3-wine, 4-blood : "))
        if m==4:
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==e:
        print(e)
        n=int(input("1-shoes , 2-clothes, 3-crime , 4-phone : "))
        if n==3:
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==f:
        print(f)
        k=int(input("1-randy,2-mandy,3-sassy, 4-happy: "))
        if k==1:
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==g:
        print(g)
        l=int(input("1-india , 2-brazil , 3-america , 4-china"))
        if l==3:
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==h:
        print(h)
        o=int(input("1-emotion, 2-mood, 3-time, 4-place"))
        if o==2:
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==i:
        print(i)
        A=int(input('1-horses , 2-money , 3-cars , 4-bikes : '))
        if A==1:
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
    if y==j:
        print(j)
        B=int(input('1-lungs , 2-heart, 3-blood, 4-flesh : '))
        if B==2:
            print("correct")
            l1.remove(y)
        else:
            print("wrong")
print("thank you for playing")            

