#Set up
boss = 1
import random
start = ("n")
player = 1
p1_stats = ["0","0","0"]
p2_stats = ["0","0","0"]
good_comments = ["good job!","well done"]
bad_comments = ["better luck next time","good try"]
p1_redo_weapons = ("null")
p2_redo_weapons = ("null")
p1_main = ("NULL")
p2_main = ("NULL")
p1_level = 0
p2_level = 0

# P L A Y E R   T W O



    #PLAYER TWO CHOOSING WEAPON
def p2_func_weapon():
    print(" ")
    global p2_main
    p2_main = input("""Player two please enter the number of the weapon to choose your main weapon.
When you enter the names of the weapons it will tell you more and then you can choose to keep it or choose another.
Remember you will get more weapons and spells later in the game.
    
    1 Great Axe
        
    2 Katanna 
         
    3 Sword
        
    Back?
        
            What do you choose? """)
    
    if p2_main in ("1","One","one","Great axe","great axe","axe","Axe"):
        p2_redo_weapons = input("""Great axe
    Dexerity added to hit
        Dexerity / 4 + 1
    
    Random damage:
        30 to 60
                      
    Strength added to damage:
        Strength x 5
                                    
    Dexerity added to damage:
        None
    
    Player two:
    Your bonus to hit
        {}
                      
    Average damage
        {}
    
    Keep weapon? Y/N 
      """.format(round(p2_stats[1] / 4) + 1, p2_stats[1] * 5 + 45))

    if p2_main in ("2","Two","two","Katanna","katanna"):
        p2_redo_weapons = input("""Katanna
    
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
    
    if p2_main in ("3","Three","three","Sword","sword"):
        p2_redo_weapons = input("""Sword
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


    #P2 back to score

    if p2_main in ("Back","back","b","B"):
        p2_func_class()

    #P2 incase invalid input

    if p2_main not in ("1","2","3"):
        p2_func_weapon()

    #P2 keeping weapon going to game
    if p2_redo_weapons in ("y","Y"):
        print("Going into game")
        print(" ")
        return
    
    elif p2_redo_weapons in ("N","n"):
        print("Returning to weapon's page")
        p2_func_weapon()


        
    elif p2_redo_weapons not in ("y","Y"):
        print(p2_redo_weapons)
        print("Wrong input")
        p2_func_weapon()


    #PLAYER TWO CHOOSING STATS
def p2_func_class():
    if p2_redo_weapons not in ("y","Y"):
        contin = input("Continue with player two? Y/N ")
        if contin in ("n","N"):
            print(" ")
            print("---PLAYER ONE---")
            contin = 0
            p2_func_weapon()


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
            if p2_redo_weapons not in ("y","Y"):
                p2_stats[0] = str(input("""Health: """))

                if p2_stats[0].isdigit():
                    p2_stats[0] = int(p2_stats[0])

                    if p2_stats[0] in range(0,16):
                        pass

                    else:
                        print("Please put in a number from 0 to 15")
                        print(" ")
                        p2_func_class()
            
                else:
                    print ("""Please put in usable numbers
                   """)
                    p2_func_class()
            

            #Strength
            if p2_redo_weapons not in ("y","Y"):
                p2_stats[1] = str(input("""Strength: """))

                if p2_stats[1].isdigit():
                    p2_stats[1] = int(p2_stats[1])

                    if p2_stats[1] in range(0,16):
                        pass

                    else:
                        print("Please put in a number from 0 to 15")
                        print(" ")
                        p2_func_class()

                else:
                    print ("""Please put in usable numbers
                           """)
                    p2_func_class()

                #Dexerity
            if p2_redo_weapons not in ("y","Y"):    
                p2_stats[2] = str(input("""Dexerity: """))

                if p2_stats[2].isdigit():
                    p2_stats[2] = int(p2_stats[2])

                    if p2_stats[2] in range(0,16):
                        pass

                    else:
                        print("Please put in a number from 0 to 15")
                        print(" ")
                        p2_func_class()


                else:
                    print ("""Please put in usable numbers
                       """)
                    p2_func_class()

            else:
                return

            #Calculate level and redo if to high
            global p2_level
            p2_level = p2_stats[0] + p2_stats[1] + p2_stats[2]
            if p2_level >= 16:
                print("Please keep your total number of points across your stats under 16")
                print(""" """)
                p2_func_class()
            if p2_level <= 15:
                print(""" """)
                print("Player two is level: {}".format(p2_level))
                p2_func_weapon()




# P L A Y E R   O N E



    #PLAYER ONE CHOOSING WEAPON
def p1_func_weapon():
    print(" ")
    global p1_main
    p1_main = input("""Player one please enter the number of the weapon to choose your main weapon.
When you enter the names of the weapons it will tell you more and then you can choose to keep it or choose another.
Remember you will get more weapons and spells later in the game.
    
    1 Great Axe
        
    2 Katanna 
         
    3 Sword
        
    Back?
        
            What do you choose? """)
    
    if p1_main in ("1","One","one","Great axe","great axe","axe","Axe"):
        p1_redo_weapons = input("""Great axe
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

    if p1_main in ("2","Two","two","Katanna","katanna"):
        p1_redo_weapons = input("""Katanna
    
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
    
    if p1_main in ("3","Three","three","Sword","sword"):
        p1_redo_weapons = input("""Sword
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


    #P1 back to score

    if p1_main in ("Back","back","b","B"):
        p1_func_class()

    #P1 incase invalid input

    if p1_main not in ("1","2","3"):
        p1_func_weapon()

    elif p1_redo_weapons in ("N","n"):
        print("Returning to weapon's page")
        p1_func_weapon()

    #P1 keeping weapon going to P2
    if p1_redo_weapons in ("y","Y"):
        p2_func_class()
        
    elif p1_redo_weapons not in ("y","Y"):
        print(p1_redo_weapons)
        print("Wrong input")
        p1_func_weapon()


    #PLAYER ONE CHOOSING STATS
def p1_func_class():
    print("---PLAYER ONE---")
    print ("""Health is the ammount of damage your character can take before being knocked out.
Strength is how good you are with strength weapons and is mainly based on damage.
Dexerity is how good you are with dexerity weapons and how likely you are to get hit by an enemy and it mainly changes how likely you are to hit.
               """)

    print("Player one please allocate 15 levels or less in these 3 stats")
    print(" ")
        
    #Health
    if p2_redo_weapons not in ("y","Y"):
        p1_stats[0] = str(input("""Health: """))

        if p1_stats[0].isdigit():
            p1_stats[0] = int(p1_stats[0])

            if p1_stats[0] in range(0,16):
                pass

            else:
                print("Please put in a number from 0 to 15")
                print(" ")
                p1_func_class()
            

        else:
            print ("""Please put in usable numbers
                   """)
            p1_func_class()


    #Strength
    if p2_redo_weapons not in ("y","Y"):
        p1_stats[1] = str(input("""Strength: """))

        if p1_stats[1].isdigit():
            p1_stats[1] = int(p1_stats[1])

            if p1_stats[1] in range(0,16):
                pass

            else:
                print("Please put in a number from 0 to 15")
                print(" ")
                p1_func_class()

        else:
            print ("""Please put in usable variables
                   """)
            p1_func_class()


    #Dexerity
    if p2_redo_weapons not in ("y","Y"):
        p1_stats[2] = str(input("""Dexerity: """))
        
        if p1_stats[2].isdigit():
            p1_stats[2] = int(p1_stats[2])

            if p1_stats[2] in range(0,16):
                pass

            else:
                print("Please put in a number from 0 to 15")
                print(" ")
                p1_func_class()

        else:
            print ("""Please put in usable variables
                    """)
            p1_stats[2] = 0
            p1_func_class()
    
    else:
        return


    #Calculate level and redo if to high
    global p1_level
    p1_level = p1_stats[0] + p1_stats[1] + p1_stats[2]
    print (p1_level)
    if p1_level >= 16:
        print("""Please keep your total number of points across your stats under 16
                  """)
        print(" ")
        p1_func_class()
    if p1_level <= 15:
        print(""" """)
        print("Player one is level: {}".format(p1_level))
        p1_func_weapon()

    #P2 choosing staring weapon

def redo_start():
    start = input("Are you ready Y/N ")
    if start in ("y","Y","Yes","yes"):
        print(""" """)
        p1_func_class()
    else:
        print(""" """)
        redo_start()
        
print("""Welcome to my game. This game is a text based fighting game which you choose you starting skills and weapon.
This game currently only has one boss and two tiles but there might be more weapons, more tiles, more bosses, more skills and a magic system coming soon!
This game needs and saves no personal data so you don't have to worry what so ever about your safety.
This game is also unfinshed but more will probabley be coming soon!
      """)
while start not in("y"):
    start = input("Are you ready Y/N ")
    if start in ("y","Y","Yes","yes"):
        print(""" """)
        p1_func_class()
    else:
        redo_start()


boss = 1
import random
start = ("n")
player = 1
p1_level = 0
p2_level = 0
playing = 0
p1_to_hit = 0
p2_to_hit = 0
p1_base_damage = 0
p1_status = 0
p2_status = 0
enemy_hp = 0


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
player_location = ("c3")

#P1 stats
p1_stats[0] = int(p1_stats[0])
p1_stats[1] = int(p1_stats[1])
p1_stats[2] = int(p1_stats[2])
p1_max_health = p1_stats[0] * 5 + 30
p1_current_hp = p1_max_health
p1_ac = round(p1_stats[2] / 2.5) + 11

#P2 stats
p2_stats[0] = int(p2_stats[0])
p2_stats[1] = int(p2_stats[1])
p2_stats[2] = int(p2_stats[2])
p2_max_health = p2_stats[0] * 5 + 30
p2_current_hp = p2_max_health
p2_ac = round(p2_stats[2] / 2.5) + 11

def p1_func_action():
    global p1_to_hit
    global p1_display_damage
    global player_location
    global enemy_hp
    p1_to_hit = 0
    p1_action = input("""Player 1 what do you do? 
1 Attack?
""")
    if p1_action in ("1","one","One","Attack","Fight","attack","fight","f","F","A","a"):
        if p1_main in ("1","One","one","Great axe","great axe","axe","Axe"):
            p1_to_hit = round(p2_stats[1] / 4)
            p1_base_damage = p1_stats[1] * 5 
            p1_display_damage = p1_base_damage + (random.randrange(30, 60))
            p1_to_hit += (random.randrange(1, 20))
            return

        if p1_main in ("2","Two","two","Katanna","katanna"):
            p1_to_hit = round(p2_stats[2] / 3)
            p1_base_damage = p1_stats[2] * 2 + p1_stats[1] * 2
            p1_display_damage = p1_base_damage + (random.randrange(15, 50))
            p1_to_hit += (random.randrange(1, 20))
            return

        if p1_main in ("3","Three","three","Sword","sword"):
            p1_to_hit = round(p2_stats[2] / 3)
            p1_base_damage = p1_stats[1] * 3
            p1_display_damage = p1_base_damage + (random.randrange(20, 55))
            p1_to_hit += (random.randrange(1, 20))
            return

    else:
        p1_func_action()
            


def p2_func_action():
    global p2_to_hit
    global p2_display_damage
    global player_location
    global enemy_hp
    p2_to_hit = 0
    player_location = ("c2")
    p2_action =input("""Player 2 what do you do? 
1 Attack?
""")
    if p2_action in ("1","one","One","Attack","Fight","attack","fight","f","F","A","a"):
        if p2_main in ("1","One","one","Great axe","great axe","axe","Axe"):
            p2_to_hit = round(p2_stats[1] / 4)
            p2_base_damage = p2_stats[1] * 5 
            p2_display_damage = p2_base_damage + (random.randrange(30, 60))
            p2_to_hit += (random.randrange(1, 20))
            return

        if p2_main in ("2","Two","two","Katanna","katanna"):
            p2_to_hit = round(p2_stats[2] / 3)
            p2_base_damage = p2_stats[2] * 2 + p2_stats[1] * 2
            p2_display_damage = p2_base_damage + (random.randrange(15, 50))
            p2_to_hit += (random.randrange(1, 20))
            return

        if p2_main in ("3","Three","three","Sword","sword"):
            p2_to_hit = round(p2_stats[2] / 3)
            p2_base_damage = p2_stats[1] * 3
            p2_display_damage = p2_base_damage + (random.randrange(20, 55))
            p2_to_hit += (random.randrange(1, 20))
            return
    

    else:
        p2_func_action()


playing = 1
while playing == 1:

#Damage player one
    if time <= 0:
        print("You ran out of time thank you for playing more coming soon!")
        while time <= 0:
            pass
    

    #C3
    if player_location == ("c3"):
        print("Player one is on {} health out of {}".format(p1_current_hp, p1_max_health))
        print("Player two is on {} health out of {}".format(p2_current_hp, p2_max_health))
        player_location = ("null")
        print("""
                        Time {}
       A  B  C  D  E    
   1        [{}]             
   2     [{}][{}][{}]          
   3  [{}][{}][U][{}][{}]       
   4     [{}][{}][{}]     N    
   5        [{}]      W   E  
                       S
           
""".format(time,c1,b2,c2,d2,a3,b3,c3,d3,e3,b4,c4,d4,c5))
        resting = input("Do you move or rest? ")
        if resting in ("Rest","rest","Sleep","sleep","R","r","S","s"):
            p1_current_hp = p1_max_health
            p2_current_hp = p2_max_health
            p1_status = 0
            p2_status = 0
            p1_ac = round(p1_stats[2] / 2.5)
            p2_ac = round(p2_stats[2] / 2.5)
            time -= 2
            player_location = ("c3")
        if resting in ("move","Move","M","m"):
            direction = input(str("""Where do you go? N/E/S/W 
"""))
            if direction in ("N","n","North","north","E","e","East","east","S","s","South","south","W","w","West","west",):
                player_location = ("c2")

            else:
                print("Please put in a usable variable.")
                player_location = ("c3")
        
        else:
            player_location = ("c3")
            continue


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
                p1_func_action()
                if p1_to_hit >= 14:
                    print("{} Hit!".format(p1_to_hit))
                    enemy_hp -= p1_display_damage
                    print("Player one you did {} damage so the boss is now on {}".format(p1_display_damage,enemy_hp))
                if p1_to_hit <= 0:
                    pass
                if p1_to_hit < 14:
                    print("{} Miss".format(p1_to_hit))

            if p1_current_hp <= 0:
                print("Player one is knocked out!")
                p1_display_damage = 0
                p2_display_damage = 100
                print(" ")
                p1_status = 1
                if p2_status == 1:
                    print("Oh no! You were defeated by the giant lizard {}" .format(random.choice(bad_comments)))
                    player_location = ("c3")
                    time -= 1
                    enemy_hp = 0
                    p1_current_hp = 1
                    p2_current_hp = 1
                    continue

        #Player two action
            if p2_current_hp > 0:
                print(" ")
                print("---PLAYER TWO---")
                p2_func_action()
                if p2_to_hit >= 14:
                    print("{} Hit!".format(p2_to_hit))
                    enemy_hp -= p2_display_damage
                    print("Player two you did {} damage so the boss is now on {}".format(p2_display_damage,enemy_hp))
                if p2_to_hit <= 0:
                    pass
                if p2_to_hit < 14:
                    print("{} Miss".format(p2_to_hit))

            if p2_current_hp <= 0:
                print("Player two is knocked out!")
                p2_display_damage = 0
                p1_display_damage = 100
                print(" ")
                p2_status = 1
                if p1_status == 1:
                    print("Oh no! You were defeated by the giant lizard {}!".format(random.choice(bad_comments)))
                    player_location = ("c3")
                    time -= 1
                    enemy_hp = 0
                    p2_current_hp = 1
                    p1_current_hp = 1
                    continue

            if enemy_hp <= 0:
                print("You defeated the giant lizard {}".format(random.choice(good_comments)))
                print("Thank you for playing more maybe coming soon!")
                while enemy_hp <= 0:
                    pass
                
                

        #Enemies turn
            if enemy_hp > 0:
                print(" ")
                print("---GIANT LIZARD---")
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
                            print("The giant lizard leaps forward mouth wide but player one dodge's out of the way! {}".format(random.choice(good_comments)))

                    else:
                        enemy_to_hit = (random.randrange(1, 20)) + enemy_bonus
                        if enemy_to_hit >= p2_ac:
                            enemy_damage = (random.randrange(70, 100))
                            p1_current_hp -= enemy_damage
                            print("The giant lizard leaps forward mouth wide open devourering player one! Dealing {} damage and leaving player one on {} health".format(enemy_damage,p1_current_hp))
                        if enemy_to_hit < p1_ac:
                            print("The giant lizard leaps forward mouth wide but player two dodge's out of the way! {}".format(random.choice(good_comments)))
                

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

                    else:
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
