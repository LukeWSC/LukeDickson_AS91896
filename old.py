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
        player_class = input("""Player {} choose starting class
1 Mage

2 Barbarian

3 Priest
    Mid health 6
    High mana 8
    Mid arcane 5
    Low strength 3
    Low dex  3
    
4 Warrior
    All stats are mid 5 each

5 Bloody
    High hp 9
    Very low mana 1
    High arcane 6
    Low strength 4
    Slightly high dex 5
    Equipment: bleedable weapon, wand, blood spells

6 Prodigy
    Mid health 5
    Very low mana 2
    Extremely high arcane 12
    Low strength 3
    Low dex 3

7 Fated
    Randomly spread 25 levels
    Equipment: Chaos dagger

8 Random

    Who do you choose?: """.format(player))
        print(""" """)
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
            print("""Mage
    Low hp 3
    High mana 10
    Good Arcane 6
    Low strength 3
    Low dex 3
    Equipment: Wand, Dagger, 3 spells""")
            if player == 2:
                p2_hp = 3
                p2_mana = 10
                p2_arcane = 9
                p2_strength = 3
                p2_dex = 3
                p2_main = ("Wizard Wand")
                p2_offhand = ("Dagger")
                p2_spells = ["fireball","shield",""]
            redo_class = input("Do you want to choose a different class? Y/N ")
            if player == 2:
                if redo_class in ("n","N","No","no"):
                    break
                if redo_class not in ("y","Y"):
                    player = 2

#Barbarian
            elif player_class in ("Barbarian","barbarian","2","Two","two"):
                if player == 1:
                    p1_hp = 8
                    p1_mana = 2
                    p1_arcane = 2
                    p1_strength = 9
                    p1_dex = 4
                    p1_main = ("Great axe")
                print ("""Barbarian
    High hp 8
    Low mana 2 
    Low Arcane 2 
    High strength 9
    Low dex 4 
    Equipment: strength weapon""")
                if player == 2:
                    p2_hp = 8
                    p2_mana = 2
                    p2_arcane = 2
                    p2_strength = 9
                    p2_dex = 4
                    p2_main = ("Great axe")
                redo_class = input("Do you want to choose a different class? Y/N ")
                if player == 2:
                    if redo_class in ("n","N","No","no"):
                        in_intro = input("Are you ready to begin? Y/N")
                        if in_intro in ("y","Y","Yes","yes"):
                            break
                        if in_intro in ("n","N","No","no"):
                            redo_where = input("""What do you want to redo?
1: Player 1 class
2: Player 2 class
    """)
                            if redo_where == 1:
                                player = 1
                                redo_class == 1
                            if redo_where == 2:
                                player = 2
                                redo_class == 1
                            else:
                                print("Please put in usable variables.")
                                in_intro = ("n")