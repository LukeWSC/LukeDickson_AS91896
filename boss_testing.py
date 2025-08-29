
boss = 1
import random
start = ("n")
player = 1
not_intro = ("n")
p1_stats = [0,15,0]
p2_stats = [5,5,5]
p1_main = ("1")
p2_main = ("3")
p1_level = 0
p2_level = 0
test = ("n")
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
1 Attack?    2 Run?
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

                
    if p1_action in ("Run","run","2","Two","two","R","r"):
        player_location = ("c3")
        enemy_hp = 0
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
1 Attack?    2 Run?
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
                
    if p2_action in ("Run","run","2","Two","two","R","r"):
        p2_to_hit = 0
        player_location = ("c3")
        enemy_hp = 0
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
                print(" ")
                p1_status = 1
                if p2_status == 1:
                    print("Oh no! You were defeated by the giant lizard better luck next time!")
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
                print(" ")
                p2_status = 1
                if p1_status == 1:
                    print("Oh no! You were defeated by the giant lizard better luck next time!")
                    player_location = ("c3")
                    time -= 1
                    enemy_hp = 0
                    p2_current_hp = 1
                    p1_current_hp = 1
                    continue

            if enemy_hp <= 0:
                print("You defeated the giant lizard amazing job!")
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
                            print("The giant lizard leaps forward mouth wide but player one dodge's out of the way! Well done!")

                    if p1_display_damage < p2_display_damage:
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
