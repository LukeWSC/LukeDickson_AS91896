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
        if boss in range (1,7):
            boss_redo = input("you choose {} do you want to choose a different one? Y/N".format(boss))
        elif boss in ("Random"):
