#Set up
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
    #Choosing boss
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

#Choosing class
    if boss_redo not in ("y","Y","Yes","yes"):
        print ("""-------------
               """)
        print ("Talk about what every stat does")
        redo_class = 1
        if redo_class in (1,"Y","y"):
            redo_class = 0
            player_class = input("""Player {} choose starting class
            Mage
            Low hp 3
            High mana 10
            Good Arcane 6
            Low strength 3
            Low dex 3
            Equipment: Wand, Dagger, 3 spells

            Nimble
            Low hp 
            Low mana
            Low Arcane
            Very low strength
            High dex 
            Equipment: two dex weapons, wand

            Barbarian
            High hp 8
            Low mana 2 
            Low Arcane 2 
            High strength 9
            Low dex 4 
            Equipment: strength weapon

            Priest
            Mid health 6
            High mana 8
            Mid arcane 5
            Low strength 3
            Low dex  3
    
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
            #Mage
            if player_class in ("Mage","1","mage","one","One"):
                if player == 1:
                    p1_hp = 3
                    p1_mana = 10
                    p1_arcane = 9
                    p1_strength = 3
                    p1_dex = 3
                    p1_main = ("Wizard Wand")
                    p1_offhand = ("Dagger")
                    p1_spells = ["fireball","shield",""]
                print ("""Mage
    Low hp 3
    High mana 10
    Good Arcane 6
    Low strength 3
    Low dex 3
    Equipment: Wand, Dagger, 3 spells""")
                redo_class = input("Do you want to choose a different class? Y/N")
                redo_class = 1
                if redo_class not in ("y","Y"):
                    player = 2

            elif class1 in (""):
                ("repeat above to another class")