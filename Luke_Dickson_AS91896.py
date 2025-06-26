#Set up
boss = 1
import random
bosses = ["1","2","3","5","6","7"]
boss_redo = ("y")
start = ("n")
player = 1
in_intro = ("n")
print("Describe game")
while start not in("y"):
    start = input("Are you ready Y/N ")
while in_intro in ("n","N","No","no"):
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
    Massive increase in random damage RANGE
    Equipment: No base damage danger

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
1: Final boss
2: Player 1 class
3: Player 2 class
    """)
                            if redo_where == 1:
                                boss_redo = ("y")
                            if redo_where == 2:
                                player = 1
                                redo_class == 1
                            if redo_where == 3:
                                player = 2
                                redo_class == 1
                            else:
                                print("Please put in usable variables.")
                                in_intro = ("n")
                    else:
                        print("please put in usable variables")
                if redo_class not in ("y","Y"):
                    player = 2

#wrong input
            else:
                print("Please put in a usable variable")
                redo_class = 1

#Map
time = 16
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
I  3  [{}][{}][U][{}][{}]       R
R  4     [{}][{}][{}]     N    T
   5        [{}]      W   E  H
                       S
           WATER
""".format(time,c1,b2,c2,d2,a3,b3,c3,d3,e3,b4,c4,d4,c5))
player_location = ("c3")
playing = 1
while playing == 1:

#Damage
    if p1_main in ("Great axe"):
        p1_base = 30
        p1_main_bonus = p1_strength / 2
    p1_second_base_damage_main = p1_base + p1_strength * 5

    #C3
    if player_location == ("c3"):
        player_location = ("null")
        resting = input("Do you move or rest?")
        if resting in ("Rest","rest","Sleep","sleep","R","r","S","s"):
            p1_current_hp = p1_hp * 5
            p1_energy = p1_dex * 5 + 30
            p1_current_mana = p1_mana * 5
            time - 2
            player_location = ("c3")
        if resting in ("move","Move","M","m"):
            direction = input("Where do you go? N/E/S/W ")
            if direction in ("N","n","North","north"):
                player_location = ("c2")
            if direction in ("S","s","South","south"):
                player_location = ("c4")
            if direction in ("E","e","East","east"):
                player_location = ("d3")
            if direction in ("W","w","West","west"):
                player_location = ("b3")
            else:
                print("Please put in a usable variable.")
                player_location = ("c3")
        else:
                print("Please put in a usable variable.")
                player_location = ("c3")


    #C2
    if player_location == ("c2"):
        time - 1
        basic_fire_bosses = ["Fire Lizard","Flame Golem"]
        enemy = random.choice(basic_fire_bosses)
        if enemy in ("Fire Lizard"):
            enemy_hp = 200
            enemy_ac = 14
            enemy_energy = 50
            enemy_attacks = ["Spit flame", "Consume","Tail"]
        while enemy in ("Fire Lizard"):
            print("A Flame Lizard appears hp: {}  ac: {}  energy = {}".format(enemy_hp,enemy_ac,enemy_energy))
        
        #Player one action
            p1_action =input("""Player 1 what do you do? 
Attack?    Run?    Cast?    Inventory?    Skip?
""")
            if p1_action in ("Attack","Fight","attack","fight","f","F","A","a"):
                p1_to_hit = (random.randrange(1, 20))
                p1_to_hit + p1_main_bonus
                if p1_to_hit >= 14:
                    print("Hit!")
                    enemy_hp -= p1_base + random.randrange(1, 60)
                if p1_to_hit <= 14:
                    print("Miss")
