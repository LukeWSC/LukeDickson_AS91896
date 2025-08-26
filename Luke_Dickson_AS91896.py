#Set up
boss = 1
import random
start = ("n")
player = 1
not_intro = ("n")
p1_stats = ["0","0","0"]
p2_stats = ["0","0","0"]
p1_redo_weapons = 0

#GREAT AXES
def p1_great_axe(p1_redo_weapons):
    return p1_redo_weapons == input("""Great axe
    Dexerity added to hit
        Dexerity / 4 + 1
    
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
      """.format(round(p1_stats[1] / 4) + 1, p1_stats[1] * 5 + 45))
    
def p2_great_axe(p2_redo_weapons):
    return p2_redo_weapons == input("""Great axe
    Dexerity added to hit
        Dexerity / 4 + 1
    
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
      """.format(round(p2_stats[1] / 4) + 1, p2_stats[1] * 5 + 45))

#KATANNA
def p1_katanna(p1_redo_weapons):
    return p1_redo_weapons == input("""Katanna
    
    Dexerity added to hit:
        Dexerity / 3 (rounded to nearest whole number)
    
    Random damage:
        15 to 50
                      
    Strength added to damage:
        Strength x 2
    
    Dexerity added to damage:
        Dexerity x 2
    
    Player one:
    Your bonus to hit
        {}
                      
    Average damage
        {}
    
    Keep weapon? Y/N 
      """.format(round(p1_stats[2] / 3), p1_stats[2] * 2 + 30 + p1_stats[1] * 2))
    
def p2_katanna(p2_redo_weapons):
    return p2_redo_weapons == input("""Katanna
    
    Dexerity added to hit:
        Dexerity / 3 (rounded to nearest whole number)
    
    Random damage:
        15 to 50
                      
    Strength added to damage:
        Strength x 2
    
    Dexerity added to damage:
        Dexerity x 2
    
    Player one:
    Your bonus to hit
        {}
                      
    Average damage
        {}
    
    Keep weapon? Y/N 
      """.format(round(p2_stats[2] / 3), p2_stats[2] * 2 + 30 + p2_stats[1] * 2))

#SWORDS
def p1_sword(p1_redo_weapons):
    return p1_redo_weapons == input("""Sword
    Strength added to hit :
        None
    
    Dexerity added to hit:
        Dexerity / 3 (rounded to nearest whole number)
    
    Random damage:
        20 to 55
                      
    Strength added to damage:
        Strength x 3
    
    Dexerity added to damage:
        None
    
    Player one:
    Your bonus to hit
        {}
                      
    Average damage
        {}
    
    Keep weapon? Y/N 
      """.format(round(p1_stats[2] / 3), 40 + p1_stats[1] * 3))
    
def p2_sword(p2_redo_weapons):
    return p2_redo_weapons == input("""Sword
    Strength added to hit :
        None
    
    Dexerity added to hit:
        Dexerity / 3 (rounded to nearest whole number)
    
    Random damage:
        20 to 55
                      
    Strength added to damage:
        Strength x 3
    
    Dexerity added to damage:
        None
    
    Player one:
    Your bonus to hit
        {}
                      
    Average damage
        {}
    
    Keep weapon? Y/N 
      """.format(round(p2_stats[2] / 3), 40 + p2_stats[1] * 3))


#PLAYER TWO CHOOSING WEAPON
def p2_func_weapon():
    p2_main = input("""Player two please enter the number of the weapon to choose your main weapon.
When you enter the names of the weapons it will tell you more and then you can choose to keep it or choose another.
Remeber you will get more weapons and spells later in the game.
                                    
        1 Great Axe
        
        2 Katanna 
        
        3 Sword
        
        Back?
        
            What do you choose? """)
    
    #Weapons
    if p2_main in ("1","One","one","Great axe","great axe","axe","Axe"):
        p2_great_axe()

    if p2_main in ("2","Two","two","Katanna","katanna"):
        p2_katanna()

    if p2_main in ("3","Three","three","Sword","sword"):
        p2_sword()
            

    if p2_main in ("Back","back","b","B"):
        p2_func_class()
    #P2 incase invalid input
    if p2_redo_weapons not in ("Y","y","N","n","0"):
        print("Please use only Y/N")
        p2_func_weapon()

    if p2_redo_weapons in ("Y","y"):
        p2_redo_weapons = input("Are you ready to begin? Y/N ")


#PLAYER TWO CHOOSING STATS
def p2_func_class():
    contin = input("Continue to player two? Y/N ")
    if contin in ("n","N"):
        print(" ")
        print("---PLAYER ONE---")
        contin = 0
        p1_func_weapon()

    
    if contin not in ("Y","y","N","n"):
        print("Please only use Y or N thank you")
        print(" ")
        contin = 0
        p2_func_class()

    
    if contin in ("y","Y"):
        print(" ")
        contin = 0
        print("---PLAYER TWO---")
        print ("""Health is the ammount of damage your character can take before being knocked out.
           
Strength is how good you are with strength weapons and is mainly based on damage.
           
Dexerity is how good you are with dexerity weapons and how likely you are to get hit by an enemy and it mainly changes how likely you are to hit.
               """)

        print("Player two please allocate 15 levels or less in these 3 stats")
        print(" ")

        #Health
        p2_hp =  int(input("""Health: """))
        if p2_hp not in range (0,16):
            print("""Please put in a usable input
                        """)
            p2_func_class()
            

        #Strength
        p2_strength = int(input("""Strength: """))
        if p2_strength not in range (0,16):
            print ("""Please put in usable variables
                   """)
            p2_func_class()

        #Dexerity
        p2_dex = int(input("""Dexerity: """))
        if p2_dex not in range (0,16):
            print ("""Please put in usable variables
                   """)
            p2_func_class()

        #Calculate level and redo if to high
        p2_level = p2_hp + p2_strength + p2_dex
        if p2_level > 16:
            print("Please keep your total number of points across your stats under 26")
            p2_func_class()
            print(""" """)
        if p2_level <= 15:
            def p2_func_class():
                print(""" """)

#PLAYER ONE CHOOSING WEAPON
def p1_func_weapon():
    print(" ")
    p1_main = input("""Player one please enter the number of the weapon to choose your main weapon.
When you enter the names of the weapons it will tell you more and then you can choose to keep it or choose another.
Remeber you will get more weapons and spells later in the game.
    
    1 Great Axe
        
    2 Katanna 
         
    3 Sword
        
    Back?
        
            What do you choose? """)
    
    if p1_main in ("1","One","one","Great axe","great axe","axe","Axe"):
        p1_great_axe()

    if p1_main in ("2","Two","two","Katanna","katanna"):
        p1_katanna()
    
    if p1_main in ("3","Three","three","Sword","sword"):
        p1_sword()


    #P1 back to score
    if p1_main in ("Back","back","b","B"):
        p1_func_class()

    #P1 incase invalid input
    elif p1_redo_weapons in ("N","n"):
        print("Returning to weapon's page")
        p1_func_weapon()

    else:
        print("Wrong input")
        p1_func_weapon()

       #P1 keeping weapon going to P2
    if p1_redo_weapons in ("y","Y"):
        p2_func_class()

#PLAYER ONE CHOOSING STATS
def p1_func_class():
    print("---PLAYER ONE---")
    print ("""Health is the ammount of damage your character can take before being knocked out.
           
Strength is how good you are with strength weapons and is mainly based on damage.
           
Dexerity is how good you are with dexerity weapons and how likely you are to get hit by an enemy and it mainly changes how likely you are to hit.
               """)

    print("Player one please allocate 15 levels or less in these 3 stats")
        
    #Health
    p1_hp =  int(input("""Health: """))
    if p1_hp not in range (0,16):
        print ("""Please put numbers between 0-15
                   """)
        p1_func_class()
    else:
        print ("""Please put in usable variables
                   """)
        p1_func_class()


    #Strength
    p1_strength = int(input("""Strength: """))
    if p1_strength not in range (0,16):
        print ("""Please put numbers between 0-15
                   """)
        p1_func_class()
    else:
        print ("""Please put in usable variables
                   """)
        p1_func_class()


    #Dexerity
    p1_dex = int(input("""Dexerity: """))
    if p1_dex not in range (0,16):
        print ("""Please put numbers between 0-15
                   """)
        p1_func_class()
    else:
        print ("""Please put in usable variables
                   """)
        p1_func_class()


    #Calculate level and redo if to high
    p1_level = p1_hp + p1_strength + p1_dex
    if p1_level >= 16:
        print("""Please keep your total number of points across your stats under 26
                  """)
        if p1_level <= 15:
            print(""" """)
            p1_func_weapon()

    #P2 choosing staring weapon

        
print("""Welcome to my game. This game is a text based fighting game which you choose you starting skills and weapon.
This game currently only has one boss and two tiles but there might be more weapons, more tiles, more bosses, more skills and a magic system coming soon!
This game needs and saves no personal data so you don't have to worry what so ever about your safety.
This game is also unfinshed but more will probabley be coming soon!
      """)
while start not in("y"):
    start = input("Are you ready Y/N ")
    p1_func_class()
    print(""" """)
#Map
players_down = 0
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
player_location = ("c3")

#P1 stats
p1_max_health = p1_hp * 5 + 30
p1_current_hp = p1_max_health
p1_ac = round(p1_dex / 2.5) + 11

#P2 stats
p2_max_health = p2_hp * 5 + 30
p2_current_hp = p2_max_health
p2_ac = round(p1_dex / 2.5) + 11


playing = 1
while playing == 1:

#Damage player one
    if time <= 0:
        print("You ran out of time thank you for playing more coming soon!")
        break

    if p1_main in ("1","One","one","Great axe","great axe","axe","Axe"):
        p1_to_hit = round(p1_strength / 4)
        p1_base_damage = p1_strength * 5 

    if p1_main in ("2","Two","two","Katanna","katanna"):
        p1_to_hit = round(p2_dex / 3)
        p1_base_damage = p2_dex * 2 + p2_strength * 2

    if p1_main in ("3","Three","three","Sword","sword"):
        p1_to_hit = round(p1_dex / 3)
        p1_base_damage = p1_strength * 3

#Damage player two
    if p2_main in ("1","One","one","Great axe","great axe","axe","Axe"):
        p2_to_hit = round(p2_strength / 4)
        p2_base_damage = p2_strength * 5 
    
    if p2_main in ("2","Two","two","Katanna","katanna"):
       p2_to_hit = round(p2_dex / 3)
       p2_base_damage = p2_dex * 2 + p2_strength * 2

    if p2_main in ("3","Three","three","Sword","sword"):
        p2_to_hit = round(p1_dex / 3)
        p2_base_damage = p1_strength * 3
    

    #C3
def c3():
    print("Player one is on {} health out of {} and are level {}".format(p1_current_hp, p1_max_health,p1_level))
    print("Player two is on {} health out of {} and are level {}".format(p2_current_hp, p2_max_health,p1_level))
    player_location = ("null")
    print("""
                        
       A  B  C  D  E    
   1        [{}]             
   2     [{}][{}][{}]          
   3  [{}][{}][U][{}][{}]       
   4     [{}][{}][{}]     N    
   5        [{}]      W   E  
                       S
           
""".format(c1,b2,c2,d2,a3,b3,c3,d3,e3,b4,c4,d4,c5))
    resting = input("Do you move or rest? ")
    if resting in ("Rest","rest","Sleep","sleep","R","r","S","s"):
        players_down = 0
        p1_current_hp = p1_max_health
        p2_current_hp = p2_max_health
        p1_ac = round(p1_dex / 2.5)
        p2_ac = round(p2_dex / 2.5)
        time -= 2
        c3()
    if resting in ("move","Move","M","m"):
        direction = input("Where do you go? N/E/S/W ")
        if direction in ("N","n","North","north"):
            c2()

        if direction in ("S","s","South","south"):
            c2()
            
        if direction in ("E","e","East","east"):
            c2()
        
        if direction in ("W","w","West","west"):
            c2()
                
        else:
            print("Please put in a usable variable.")
            c3()


    #C2
    if player_location == ("c2"):
        time - 1
        basic_fire_bosses = ["Fire Lizard"]
        enemy = random.choice(basic_fire_bosses)
        if enemy in ("Fire Lizard"):
            enemy_hp = 200
            enemy_ac = 14
            enemy_energy = 75
            ready_to_eat = 0
            p1_display_damage = 0
            p2_display_damage = 0
            enemy_attacks = ["Claw","Consume","Tail","Tail"]
            print ("A Giant Lizard appears!")
        while enemy_hp > 0:
            print("Giant Lizard hp: {}  ac: {}  energy = {}".format(enemy_hp,enemy_ac,enemy_energy + 25))
            enemy_energy + 25
            enemy_bonus = 6
        #Player one action
            if p1_current_hp > 0:
                print(" ")
                print("---PLAYER ONE---")
                p1_action =input("""Player 1 what do you do? 
1 Attack?    2 Run?
""")
                if p1_action in ("1","one","One","Attack","Fight","attack","fight","f","F","A","a"):
                    p1_to_hit += (random.randrange(1, 20))
                    if p1_to_hit >= 14:
                        print("Hit!")
                        if p1_main in ("1","One","one","Great Axe","great axe","axe","Axe"):
                            p1_display_damage = p1_base_damage + (random.randrange(30, 60))
                            enemy_hp -= p1_display_damage
                            print("Player one you did {} damage so the boss is now on {}".format(p1_display_damage,enemy_hp))

                        if p1_main in ("2","Two","two","Katanna","katanna"):
                            p1_display_damage = p1_base_damage + (random.randrange(15, 50))
                            enemy_hp -= p1_display_damage
                            print("Player one you did {} damage so the boss is now on {}".format(p1_display_damage,enemy_hp))

                        if p1_main in ("3","Three","three","Sword","sword"):
                            p1_display_damage = p1_base_damage + (random.randrange(20, 55))
                            enemy_hp -= p1_display_damage
                            print("Player one you did {} damage so the boss is now on {}".format(p1_display_damage,enemy_hp))

                    if p1_to_hit <= 14:
                        print("Miss")
                
                if p1_action in ("Run","run","2","Two","two","R","r"):
                    player_location = ("c3")
                    enemy_hp = 0
                    continue
            
            if p1_current_hp <= 0:
                print("Player one is knocked out!")
                players_down += 1

        #Player two action
            if p1_current_hp > 0:
                print(" ")
                print("---PLAYER TWO---")
                p2_action =input("""Player 2 what do you do? 
1 Attack?    2 Run?
""")
                if p2_action in ("1","one","One","Attack","Fight","attack","fight","f","F","A","a"):
                    p2_to_hit += (random.randrange(1, 20))
                    if p2_to_hit >= 14:
                        print("Hit!")
                        if p2_main in ("1","One","one","Great Axe","great axe","axe","Axe"):
                            p2_display_damage = p2_base_damage + (random.randrange(30, 60))
                            enemy_hp -= p2_display_damage
                            print("Player two you did {} damage so the boss is now on {}".format(p2_display_damage,enemy_hp))
                            print(" ")

                        if p2_main in ("2","Two","two","Katanna","katanna"):
                            p2_display_damage = p2_base_damage + (random.randrange(15, 50))
                            enemy_hp -= p2_display_damage
                            print("Player two you did {} damage so the boss is now on {}".format(p2_display_damage,enemy_hp))
                            print(" ")

                        if p2_main in ("3","Three","three","Sword","sword"):
                            p2_display_damage = p2_base_damage + (random.randrange(20, 55))
                            enemy_hp -= p2_display_damage
                            print("Player one you did {} damage so the boss is now on {}".format(p2_display_damage,enemy_hp))

                        if p1_action in ("Run","run","2","Two","two","R","r"):
                            player_location = ("c3")
                            enemy_hp = 0
                            continue

                    if p2_to_hit <= 14:
                        print("Miss")
                        print(" ")

            if p2_current_hp <= 0:
                print("Player one is knocked out!")
                print(" ")
                players_down += 1

            if enemy_hp <= 0:
                print("You defeated the giant lizard amazing job!")
                print("Thank you for playing more coming soon!")
                enemy_hp = 0
                player_location = ("c3")
                break
            
            if players_down >= 2:
                print("Oh no! You were defeated by the giant lizard better luck next time!")
                player_location = ("c3")
                time -= 1
                enemy_hp = 0
                players_down = 0
                p1_current_hp = 1
                p2_current_hp = 1
                continue
                
                

        #Enemies turn
            if enemy_hp > 0:
                if ready_to_eat == 1 and enemy_energy >= 75: 
                    enemy_energy -= 60
                    ready_to_eat = 0
                    if p1_display_damage >= p2_display_damage:
                        enemy_to_hit = (random.randrange(1, 20)) + enemy_bonus
                        if enemy_to_hit >= p1_ac:
                            enemy_damage = (random.randrange(70, 100))
                            p1_current_hp -= enemy_damage
                            print("The giant lizard leaps forward mouth wide open devourering player one! Dealing {} damage and leaving player one on {} health".format(enemy_damage,p1_current_hp))
                        if enemy_to_hit < p1_ac:
                            print("The giant lizard leaps forward mouth wide but player one dodge's out of the way! Well done!")

                    if p1_display_damage <= p2_display_damage:
                        enemy_to_hit = (random.randrange(1, 20)) + enemy_bonus
                        if enemy_to_hit >= p2_ac:
                            enemy_damage = (random.randrange(70, 100))
                            p1_current_hp -= enemy_damage
                            print("The giant lizard leaps forward mouth wide open devourering player one! Dealing {} damage and leaving player one on {} health".format(enemy_damage,p1_current_hp))
                        if enemy_to_hit < p1_ac:
                            print("The giant lizard leaps forward mouth wide but player two dodge's out of the way! Good job!")
                

                if ready_to_eat == 0:
                    enemy_action = random.choice(enemy_attacks)
                if ready_to_eat == 1:
                    enemy_action = ("null")
                if enemy_action in ("Tail") and enemy_energy >= 35:
                    enemy_to_hit = (random.randrange(1, 20))
                    if enemy_to_hit >= p1_ac:
                        enemy_damage = (random.randrange(15, 20))
                        p1_current_hp -= enemy_damage
                        print("The giant lizard swipes it's tail hiting player one for {} leaving player one on {} health".format(enemy_damage,p1_current_hp))
                    if enemy_to_hit < p1_ac:
                        print("The giant lizard swipes it's tail but player one dodges. Nice job!")
                    enemy_to_hit = (random.randrange(1, 20))
                    if enemy_to_hit >= p2_ac:
                        enemy_damage = (random.randrange(15, 30))
                        p2_current_hp -= enemy_damage
                        print("The giant lizard's tail hits player two for {} leaving player two on {} health".format(enemy_damage,p2_current_hp))
                    if enemy_to_hit < p2_ac:
                        print("The giant lizard's tail but player two dodges. Great job!")
            
                if enemy_action in ("Consume") and enemy_energy >= 65:
                    print("You see the giant lizard open it's jaws wide as if it's about to pounce")
                    ready_to_eat = 1
                    continue

                if enemy_action in ("Claw","Consume","Tail") and enemy_energy >= 20:
                    enemy_energy -= 15
                    if p1_display_damage >= p2_display_damage:
                        enemy_to_hit = (random.randrange(1, 20)) + enemy_bonus
                        if enemy_to_hit >= p1_ac:
                            print("The giant lizard goes in for a swipe with it's claws at player one and hits!")
                            enemy_damage = (random.randrange(15, 30))
                            p1_current_hp -= enemy_damage
                            print("Player one took {} damage and is on {} health".format(enemy_damage, p1_current_hp))
                        if enemy_to_hit < p1_ac:
                            print("The giant lizard goes in for a swipe with it's claws at player one but misses.")

                    if p1_display_damage < p2_display_damage:
                        enemy_to_hit = (random.randrange(1, 20)) + enemy_bonus
                        if enemy_to_hit >= p2_ac:
                            print("The giant lizard goes in for a swipe with it's claws at player two and hits!")
                            enemy_damage = (random.randrange(15, 30))
                            p2_current_hp -= enemy_damage
                            print("Player two took {} damage and is on {} health".format(enemy_damage, p2_current_hp))
                        if enemy_to_hit < p2_ac:
                            print("The giant lizard goes in for a swipe with it's claws at player two but misses.")

            else:
                print("The Lizard is to exhausted to do anything")
                enemy_energy + 30
