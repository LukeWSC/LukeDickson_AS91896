#Set up
boss = 1
import random
start = ("n")
player = 1
p1_redo_class = 1
p1_redo_class = 1
p2_redo_class = 1
p2_redo_weapons = 0
p1_redo_weapons = 0
not_intro = ("n")
print("Describe game")
while start not in("y"):
    start = input("Are you ready Y/N ")
while not_intro in ("n","N","No","no"):


#Choosing class
    print ("Talk about what every stat does")
    if p1_redo_class in (1,"Y","y","Back","back","b","B"):
        p1_redo_class = 0
        p2_redo_weapons = 0
        p2_redo_class = 0
        p1_redo_weapons = 0
        print("Player one please allocate 25 levels or less in these 5 stats you can upgrade them later when you level up")
        
    #Health
        p1_hp =  int(input("""Health: """))
        p1_redo_class = 0
        if p1_hp not in range (0,25):
            print("""Please put in a usable input
                  """)
            p1_redo_class = 1
            continue


    #Mana
        p1_mana = int(input("""Mana: """))
        if p1_mana not in range (0,25):
            print ("""Please put in a usable input
                   """)
            p1_redo_class = 1
            continue

            
    #Arcane
        p1_arcane = int(input("""Arcane: """))
        if p1_arcane not in range (0,25):
            print ("""Please put in a usable input
                   """)
            p1_redo_class = 1
            continue


    #Strength
        p1_strength = int(input("""Strength: """))
        if p1_strength not in range (0,25):
            print ("""Please put in usable variables
                   """)
            p1_redo_class = 1
            continue


    #Dexerity
        p1_dex = int(input("""Dexerity: """))
        if p1_dex not in range (0,25):
            print ("""Please put in usable variables
                   """)
            p1_redo_class = 1


    #Calculate level and redo if to high
        p1_level = p1_hp + p1_mana + p1_arcane + p1_strength + p1_dex
        if p1_level >= 26:
            print("""Please keep your total number of points across your stats under 26
                  """)
            p1_redo_class = 1
        if p1_level <= 25:


#Player 1 choosing main weapon
            print(""" """)
            p1_redo_weapons = ("N")
            p1_redo_class = 0
    if p1_redo_weapons in ("N","n","Back","back","b","B"):
        p1_redo_class = 0
        p2_redo_weapons = 0
        p2_redo_class = 0
        p1_redo_weapons = 0
        p1_main = input("""Player one please enter the number of the weapon to choose your main weapon.
When you enter the names of the weapons it will tell you more and then you can choose to keep it or choose another.
Remeber you will get more weapons and spells later in the game.
    
    1 Great Axe
        
    2 Wizard Wand + three spells
        
    3 Katanna 
        
    4 Bloody dagger + three blood spells
        
    5 Sword
                                
    6 Holy symbol + three holy spells
        
    Back?
        
            What do you choose? """)
        if p1_main in ("1","One","one","Great Axe","great axe","axe","Axe"):
            p1_redo_weapons = input("""Great axe
    Strength added to hit :
        Strength / 4 (rounded to nearest whole number)
    
    Dexerity added to hit:
        none
    
    Random damage:
        30 to 60
                      
    Strength added to damage:
        Strength x 5
                                    
    Dexerity added to damage:
        None
    
    Player one:
    Your bonus to hit
        {}
                      
    Average damage
        {}
    
    Keep weapon? Y/N 
      """.format(round(p1_strength / 4), p1_strength * 5 + 45))
    

        if p1_main in ("3","Three","three","Katanna","katanna"):
            p1_redo_weapons = input("""Katanna
    Strength added to hit :
        None
    
    Dexerity added to hit:
        Dexerity / 3 (rounded to nearest whole number)
    
    Random damage:
        15 to 50
                      
    Strength added to damage:
        Strength x 2
    
    Dexerity added to damage:
        Strength x 2
    
    Player one:
    Your bonus to hit
        {}
                      
    Average damage
        {}
    
    Keep weapon? Y/N 
      """.format(round(p1_strength / 4), p1_strength * 5 + 45))
    #P1 incase invalid input
        if p1_redo_weapons not in ("Y","y","N","n","Back","back","b","B"):
            print("Please use only Y/N")
            p1_redo_weapons = ("n")

       #P1 keeping weapon going to P2
        if p1_redo_weapons in ("y","Y"):
            p2_redo_class = 1
    if p2_redo_class in (1,"n","N"):
        p1_redo_class = 0
        p2_redo_weapons = 0
        p2_redo_class = 0
        p1_redo_weapons = 0
        print("Player two please allocate 25 levels or less in these 5 stats you can upgrade them later when you level up")

        #Health
        p2_hp =  int(input("""Health: """))
        if p2_hp not in range (0,25):
            print("""Please put in a usable input
                        """)
            p2_redo_class = 1
            continue

        #Mana
        p2_mana = int(input("""Mana: """))
        if p2_mana not in range (0,25):
            print ("""Please put in a usable input
                   """)
            p2_redo_class = 1
            continue

        #Arcane
        p2_arcane = int(input("""Arcane: """))
        if p2_arcane not in range (0,25):
            print ("""Please put in a usable input
                   """)
            p2_redo_class = 1
            continue

        #Strength
        p2_strength = int(input("""Strength: """))
        if p2_strength not in range (0,25):
            print ("""Please put in usable variables
                   """)
            p2_redo_class = 1
            continue
        #Dexerity
        p2_dex = int(input("""Dexerity: """))
        if p2_dex not in range (0,25):
            print ("""Please put in usable variables
                   """)
            p2_redo_class = 1
            continue

        #Calculate level and redo if to high
        p2_level = p2_hp + p2_mana + p2_arcane + p2_strength + p2_dex
        if p2_level > 25:
            print("Please keep your total number of points across your stats under 26")
            p2_redo_class = 1
            print(""" """)
        if p2_level <= 25:
            p2_redo_weapons = ("N")
            print(""" """)
            

    #P2 choosing staring weapon
    if p2_redo_weapons in ("N","n","Back","back","b","B"):
        p1_redo_class = 0
        p2_redo_weapons = 0
        p2_redo_class = 0
        p1_redo_weapons = 0
        p2_main = input("""Player two please enter the number of the weapon to choose your main weapon.
When you enter the names of the weapons it will tell you more and then you can choose to keep it or choose another.
Remeber you will get more weapons and spells later in the game.
                                    
        1 Great Axe
        
        2 Wizard Wand + three wizard spells
        
        3 Katanna 
        
        4 Bloody dagger + three blood spells
        
        5 Sword
                                
        6 Holy symbol + three holy spells
        
        Back?
        
            What do you choose? """)
    
    #Great axe
        if p2_main in ("1","One","one","Great Axe","great axe","axe","Axe"):
            p2_redo_weapons = input("""Great axe    
    Strength added to hit :
        Strength / 4
    
    Dexerity added to hit:
        none
    
    Random damage:
        30 to 60
                      
    Strength added to damage:
        Strength x 5
    
    Player one:
    Your bonus to hit
        {}
                      
    Average damage
        {}
    
    Keep weapon? Y/N 
      """.format(round(p1_strength / 4), p1_strength * 5 + 45))
    
    #P2 incase invalid input
        if p2_redo_weapons not in ("Y","y","N","n"):
            print("Please use only Y/N")
            p2_redo_weapons = ("n")

        if p2_redo_weapons in ("Y","y"):
            p2_redo_weapons = input("Are you ready to begin?")
            if p2_redo_weapons in ("Y","y"):
                break
        

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

#P1 stats
p1_max_health = p1_hp * 5 + 30
p1_current_hp = p1_max_health
p1_max_mana = p1_mana * 5
p1_current_mana = p1_max_mana

#P2 stats
p2_max_health = p2_hp * 5 + 30
p2_current_hp = p2_max_health
p2_max_mana = p2_mana * 5
p2_current_mana = p2_max_mana


playing = 1
while playing == 1:

#Damage
    if p1_main in ("Great axe"):
        p1_to_hit = round(p1_strength / 4)
        p1_base_damage = p1_strength * 5 

    if p2_main in ("Great axe"):
        p2_to_hit = round(p2_strength / 4)
        p2_base_damage = p2_strength * 5 
    

    #C3
    if player_location == ("c3"):
        print("Player one is on {} health out of {}, they have {} mana left and are level {}".format(p1_current_hp, p1_max_health,p1_current_mana,p1_max_mana,p1_level))
        print("Player two is on {} health out of {}, they have {} mana left and are level {}".format(p2_current_hp, p2_max_health,p2_current_mana,p2_max_mana,p1_level))
        player_location = ("null")
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
        resting = input("Do you move or rest?")
        if resting in ("Rest","rest","Sleep","sleep","R","r","S","s"):
            p1_current_hp = p1_max_health
            p1_current_mana = p1_max_mana
            p2_current_hp = p2_max_health
            p2_current_mana = p2_max_mana
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
        basic_fire_bosses = ["Fire Lizard"]
        enemy = random.choice(basic_fire_bosses)
        if enemy in ("Fire Lizard"):
            enemy_hp = 200
            enemy_ac = 14
            enemy_energy = 50
            enemy_attacks = ["Spit flame", "Consume","Tail"]
            print ("A Flame Lizard appears!")
        while enemy in ("Fire Lizard"):
            print("Flame Lizard hp: {}  ac: {}  energy = {}".format(enemy_hp,enemy_ac,enemy_energy))
        
        #Player one action
            p1_action =input("""Player 1 what do you do? 
1 Attack?    2 Run?    3 Cast?    4 Skip?
""")
            if p1_action in ("1","one","One","Attack","Fight","attack","fight","f","F","A","a"):
                p1_to_hit += (random.randrange(1, 20))
                if p1_to_hit >= 14:
                    print("Hit!")
                    if p1_main in ("Great axe"):
                        p1_display_damage = p1_base_damage + (random.randrange(30, 60))
                        enemy_hp -= p1_display_damage
                        print("Player one you did {} damage so the boss is now on {}".format(p1_display_damage,enemy_hp))
                if p1_to_hit <= 14:
                    print("Miss")

        #Player two action
            p2_action =input("""Player 2 what do you do? 
1 Attack?    2 Run?    3 Cast?    4 Skip?
""")
            if p2_action in ("1","one","One","Attack","Fight","attack","fight","f","F","A","a"):
                p2_to_hit += (random.randrange(1, 20))
                if p2_to_hit >= 14:
                    print("Hit!")
                    if p2_main in ("Great axe"):
                        p2_display_damage = p2_base_damage + (random.randrange(30, 60))
                        enemy_hp -= p2_display_damage
                        print("Player one you did {} damage so the boss is now on {}".format(p2_display_damage,enemy_hp))
                if p2_to_hit <= 14:
                    print("Miss")

        #Enemies turn
            random.choice(enemy_attacks)


    #Final boss
