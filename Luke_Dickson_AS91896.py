#Set up
boss = 1
import random
start = ("n")
player = 1
redo_class = 1
not_intro = ("n")
print("Describe game")
while start not in("y"):
    start = input("Are you ready Y/N ")
while not_intro in ("n","N","No","no"):


#Choosing class
    print ("Talk about what every stat does")
    redo_class = 1
    if redo_class in (1,"Y","y"):
        redo_class = 0
        print("Player one please allocate 25 levels or less in these 5 abiltes you can upgrade them later when you level up")
        p1_hp = input("Health") 
        p1_mana = input("Mana")
        p1_arcane = input("Arcane")
        p1_strength = input("Strength")
        p1_dex = input("Dexerity")
        p1_level = p1_hp + p1_mana + p1_arcane + p1_strength + p1_dex
        if p1_level >= 26:
            print("Please keep your total number of points across your stats under 26")
            redo_class = 1
        if p1_level <= 25:
            input("""Please choose your first of two starting weapons when you enter the names of the weapons it will tell you more and then you can choose to keep it or choose another remeber you will get more weapons later in the game
        1 Battle Axe
        
        2 """)
        else
             
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
