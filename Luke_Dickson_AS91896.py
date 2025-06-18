boss = 1
import random
bosses = ["1","2","3","5","6","7"]
boss_redo = ("y")
start = ("n")
player = 1
in_intro = 1
print("Describe game")
while start not in("y"):
    start = input("Are you ready Y/N ")
while in_intro == 1:
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


        print ("Talk about what every stat does")
        redo_class = 1
    if redo_class in (1,"Y","y"):
        redo_class = 0
        class1 = input("""Player {} choose starting class
        Mage
            Very low hp
            High mana
            Good Arcane
            Low strength
            Low dex
            Equipment: Wand, Dagger, 3 random spells

        Nimble
            Low hp
            Low mana
            Low Arcane
            Very low strength
            High dex
            Equipment: two dex weapons, wand

        Barbarian
            High hp
            Low mana
            Low Arcane
            High strength
            Low dex
            Equipment: strength weapon

        Priest
            Mid health 
            High mana 
            Mid arcane
            Low strength
            Low dex 
    
        Warrior
            All stats are mid 5 each

        Bloody
            High hp 9
            Very low mana 1
            High arcane 6
            Low strength 4
            Slightly high dex 5
            Equipment: two bleedable weapons, wand, blood spells

        Fated
            Randomly spread 25 levels
            Massive increase in random damage RANGE
            Equipment: No base damage danger

        Prodigy
            Mid health 5
            Very low mana 2
            Extremely high arcane 12
            Low strength 3
            Low dex 3

        Who do you choose?: 
        """.format(player))
        if class1 in ("Mage","1"):
            mana = 1
            print ("all this data")
            redo_class = input("Do you want to choose a different class? Y/N")
            redo_class = 1
            if redo_class not in ("y","Y"):
                print ("huh")

        elif class1 in (""):
            ("repeat above to another class")