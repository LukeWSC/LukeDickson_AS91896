test = 1
time = 6
print(test)
c1 = ("B")
b2 = 1
c2 = 1
d2 = 1
a3 = ("B")
b3 = 1
c3 = 1
d3 = 1
e3 = ("B")
b4 = 1
c4 = 1
d4 = 1
c5 = ("B")
print("""
           FIRE         Time {}
       A  B  C  D  E    
   1        [{}]             E
A  2     [{}][{}][{}]          A
I  3  [{}][{}][{}][{}][{}]       R
R  4     [{}][{}][{}]     N    T
   5        [{}]      W   E  H
                       S
           WATER
""".format(time,c1,b2,c2,d2,a3,b3,c3,d3,e3,b4,c4,d4,c5))

lock = 1
while lock == 1:
    lock = 1
#Choosing boss
bosses = ["1","2","3","5","6","7"]
boss_redo = ("y")
if boss_redo in ("y","Y","Yes","yes"):
    boss_redo = ("n")
    boss = 1
    boss = str(input("""Choose final boss
    1
    2
    3
    4
    5
    6
    7
    Random
    """))
    print(boss)
    if boss in ("1","2","3","5","6","7","One","Two","Three","Four","Five","Six","Seven"):
        boss_redo = input("You choose {} do you want to choose a different one? Y/N ".format(boss))
    elif boss in ("Random","random"):
        bosses = random.choice(bosses)
        boss_redo = input("You got at random {} do you want to choose another? Y/N ".format(bosses))
    else:
        print("Please put in a usable number.")
        boss_redo = ("y")
    if boss_redo not in ("y","Y","Yes","yes"):
        print ("""-------------
               """)
        p1_redo_weapons = 1

        #Back?
        p1_redo_weapons = input("Enter \"back\" to go back to player's weapon.")