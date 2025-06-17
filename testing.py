boss = 1
boss_redo = ("y")
start = ("n")
in_intro = 1
print("Describe game")
while start not in("y"):
    start = input("are you ready Y/N")
while in_intro == 1:
    if boss_redo in ("y"):
        boss_redo = ("n")
        boss = 1
        boss = int(input("""Choose final boss
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
        if boss >= 1:
            boss_redo = input("you choose 1 do you want to choose another? Y/N")
        
test = 1
time = 10
print(test)
print("""    A  B  C  D  E    Time {}
 1    [{}][{}][{}]                    
 2 [{}][{}][{}][{}][{}]
 3 [{}][{}][O][{}][{}]
 4 [{}][{}][{}][{}][{}]
 5    [{}][{}][{}]    N
                 W   E
                   S
""".format(time,a1,b1,c1,d1,e1,a2,b2,c2,d2,e2,a3,b3,c3,d3,e3,a4,b4,c4,d4,e4,a5,b5,c5,d5,e5))

