#!/usr/bin/env python3
#COSC1519 Introduction to Programming
#A2 Programming Project 
#Student name: Eamon Butler
#Student number: s3923505
#Practical group teacher: Gayan Wijesinghe
import sys, os
import random

def restart_or_exit(death):
    if death == 1:
        print("You have died...")
    elif death == 9: #restarts without asking if they chose the restart code from any input section (after the prologue)
        python = sys.executable
        os.execl(python, python, "\"{}\"".format(sys.argv[0])) #reopens the program (even works if file path has spaces in it)
    while (restart := input("Do you want to play again? (yes or no) ").lower()) not in ["yes", "no", "y", "n"]: #ask user if they want to restart or exit and any input 'not in' list gets passed to the error (case doesnt matter)
        print("Error: Accepted responses are 'yes', 'y', 'no' or 'n'")
    if restart == "yes" or restart == "y":
        python = sys.executable
        os.execl(python, python, "\"{}\"".format(sys.argv[0])) #reopens the program (even works if file path has spaces in it)
    else:
        print("exiting game") #if window/shell doesnt auto close, this will be seen to show the program is done
        sys.exit(0)

def prologue():
    print("You are an adventurer in a far off land, on the hunt for the legendary treasure of Dragonscorn. Your journey has been long and treacherous but you can feel your epic journey is nearly complete.")
    print("You approach the outskirts of a dark forest and see an old man sitting by a fire. You approach him to see if he has any knowledge of the ominous forest before you enter.")
    print("As you get closer the old man perks up and looks around rapidly. You see that he is blind")
    protagonist = str(input("The old man feverishly asks 'Who goes there??' "))
    print("'My name is " + protagonist + ", I mean you no harm. I am on a quest to find the ancient treasure of Dragonscorn and my journey has brought me to this forest. I have heard horrible things about it, have you ventured through before?'")
    print("'Ah the Forest of Hollowcall, I have not been inside its dark woods but I camp out here often for in the early morning animals such as rabbits and squirrels and sometimes even deer run out from inside the forest.'")
    print("'What they are running from, I do not know but they do make a delicious meal', he says with a chuckle. 'If you are going to try your luck in there, I can't let you go in without giving you something first, my conscience would not allow it!'")
    item = 0
    while item not in (1, 2, 3, 4): #loop if user inputs no. other than the avail options
        print("'I can offer you 3 things:'\n\t1. 'A hearty rabbit stew'\n\t2. 'A sword that an adventurer once gave me'\n\t3. 'Or a dagger I use to cut up the animals I catch, don't worry I have another at home!'\n\t4. Ignore his options, taking his life means you can have them all!\n")
        try:
            item = int(input("'Which one would you like?' (choose from 1 - 4)"));
            if item == 1:
                print("'Ah the rabbit stew, I was chasing that rabbit around the whole field before I finally caught it, it's even harder than it sounds when you're blind! Enjoy!'")
                print("+10 health (default sword 7 damage, 35 health, 2nd fight position)")
            elif item == 2:
                print("'Ah the sword of Vallemere. It once belonged to a noble knight who I helped in rescuing his Kings only daughter. They later went on to marry!'")
                print("+5 damage (12 damage, 25 health, 2nd fight position)")
            elif item == 3:
                print("'Oh you want my dagger? Good riddance! This dagger is the reason I'm blind. In a battle against a group of goblins, one jumped on my back and stabbed me in the eyes with a pair of daggers!")
                print("I used my vast knowledge of the mystic arts to escape and collapsed the entrance to the cave they live in and kept the daggers as a reminder not to steal chocolates from goblins again.'")
                print("Player always attacks first (7 damage, 25 health, 1st fight position)")
            elif item == 4:
                print("You take out your sword and lunge at him, aiming for his head but as you do he suddenly disappears.\n'Hmm, that wasn't a smart choice' he says from behind you. You turn around to see him floating over the fire.")
                print("As he raises his arms, the fire rises around him in a ring. He waves his arms in a circle and the fire ring spins faster and faster around him. You start to step back from the wizards awesome power.")
                print("You turn to run but as you do, the wizard points towards you and the fire shoots towards you, engulfing you in flames. It chars you to a crisp....\n")
                restart_or_exit(1)  #send to restart or exit function with code 1 to signal the death message
            else: # if number is outside of options
                print("\n'That item isn't on offer!'(Choose from the options)\n") 
        except Exception: # If enter anything thats not a number and allows the sys.exit to be raised
                print("\n'What did you say?'(Choose the NUMBER corresponding to the option)\n")
                
    print("\n'Be careful on your journey, the people from the village speak of an old legend that an evil beast controls the animals in those woods to protect his artifacts and bring any unwelcomed guest to him for him to consume.")
    print(f"If you believe the tales, the beasts artifact may be this treasure of Dragonscorn you are looking for.'\n'Farewell {protagonist}!'")
    print(f"End of prologue. {option_message} at any user input.\n\n\n")
    wheres_the_any_key = input("Press any key to continue.")
    if wheres_the_any_key == "0" or wheres_the_any_key == "9": #stats isn't set up until prologue function is finished
        print("That's not the any key.")
    
    return [protagonist, item] #returns the name and item choice as a list

def stats(stat_call, update_health): #stat_call for if user asked for stat readout. adjust_health is for removing or adding health to character. is_hurt defines if the health is base_health or health
    #setting base stats
    health = 25
    attack = 7   #base attack stats
    fight_order = 2 #base position stats 
    #adjusting player choice stat
    if player_choices[1] == 1:   #if user chose stew
        health = 35.0
    elif player_choices[1] == 2: #if user chose sword
        attack = 12
    elif player_choices[1] == 3: #if user chose dagger
        fight_order = 1
    #defining item choice
    if player_choices[1] == 1:
        item_choice = "Rabbit Stew"
    if player_choices[1] == 2:
        item_choice = "Sword of Vallemere"
    if player_choices[1] == 3:
        item_choice = "Blind Wizard's Dagger"
    
    if update_health != 99:
        health = update_health
    
    if stat_call == 1:
        print("Name: "+ player_choices[0])
        print("Item: "+ item_choice)
        print("Health: "+ str(health))
        print("Attack Damage: "+ str(attack))
        print("Attack Position: "+ str(fight_order))
    return [item_choice, health, attack, fight_order]

def attack_calc(attacker, enemy_attack, blocking): # calculation to determine how much damage is inflicted on target
    if attacker == "player":
        if blocking == True:
            attack_power = player_stats[2] / 2
            crit_chance = 0
            fail_chance = 1
        else:
            attack_power = player_stats[2]
            crit_chance = 1
            fail_chance = 0
        multiplier = 1
    else:
        if blocking == True:
            attack_power = enemy_attack / 2
        else:
            attack_power = enemy_attack
        crit_chance = 0
        fail_chance = 1
        multiplier = 0.5
    attack_chance = [(attack_power - (attack_power * fail_chance)), (attack_power - (2.5 * multiplier)), (attack_power - (2 * multiplier)),(attack_power), (attack_power + (2 * multiplier)), (attack_power + (3.5 * multiplier)), (attack_power + (10*crit_chance))]
    attack_damage = random.choices(attack_chance, weights=(10, 10, 15, 35, 15, 15, 10))
    return attack_damage

def fighting(enemy_name, number_of_enemy, min_health, max_health): #Function for repetitive battle
    current_player_health = float(player_stats[1])
    enemy = []
    endgame_move = ""
    if enemy_name == "Rabbit":
        enemy_attack_type = 5
    elif enemy_name == "Centaur":
        enemy_attack_type = 8
    else:
        enemy_attack_type = 15
        endgame_move = "\n\t4. Grab Sword of Dragonscorn"
    for enemy_index in range (0, number_of_enemy):
        enemy.append(random.randint(min_health, max_health))
    enemy = [float(enemy_index) for enemy_index in enemy]
    while len(enemy) > 0:
        current_enemy_health = enemy[len(enemy)-1]
        while current_enemy_health > 0:
            if len(enemy) > 1:
                enemy_num = len(enemy)
                enemy_remain = str(enemy_num) + " " + enemy_name + "s remain."
            else:
                enemy_remain = "1 " + enemy_name + " remain."
            print(f"{enemy_remain} Current opponent is at {current_enemy_health} health")
            while (player_move := input(f"What do you want to do?\n\t1. Attack\n\t2. Block\n\t3. Dodge{endgame_move}\n({option_message})\n").lower()) not in ["1", "attack", "2", "block", "3", "dodge", "4", "dragonscorn","9","0"]: 
                print("Error: Accepted responses are '1', 'attack', '2', 'block', '3' or 'dodge'. \n")
            if player_move == "1" or player_move == "attack":
                enemy_attack = attack_calc(enemy_name, enemy_attack_type, False)
                player_attack = attack_calc("player", 0, False)
                if player_stats[3] == 2:
                    print(f"\n{enemy_name} attacks!\n{player_choices[0]} took {enemy_attack} damage.")
                    print(f"\n{player_choices[0]} attacks!\n{enemy_name} took {player_attack} damage.\n")
                else:
                    print(f"\n{player_choices[0]} attacks!\n{enemy_name} took {player_attack} damage.")
                    print(f"\n{enemy_name} attacks!\n{player_choices[0]} took {enemy_attack} damage.\n")
                
                current_player_health = current_player_health - enemy_attack[0]
                current_enemy_health = current_enemy_health - player_attack[0]
            elif player_move == "2" or player_move == "block": # When blocking fight order doesn't matter
                enemy_attack = attack_calc(enemy_name, enemy_attack_type, True)
                player_attack = attack_calc("player", 0, True)
                print(f"\n{enemy_name} attacks!\n{player_choices[0]} blocks the bulk of the damage. {player_choices[0]} took {enemy_attack} damage.")
                print(f"\n{player_choices[0]} parries!\n{enemy_name} took {player_attack} damage.\n")
                
                current_player_health = current_player_health - enemy_attack[0]
                current_enemy_health = current_enemy_health - player_attack[0]
            elif player_move == "3" or player_move == "dodge":
                print(f"\n{enemy_name} attacks!\n{player_choices[0]} dodges the attack! {player_choices[0]} takes no damage.")
            elif player_move == "4" or player_move == "dragonscorn":
                if enemy_name == "Dragon":
                    player_attack = 100
                    print("\nYou run across the room, barely missing the dragons firebreath and pick up the shining Sword of Dragonscorn")
                    print(f"\n{player_choices[0]} attacks!\n{enemy_name} took {player_attack} damage.\n")
                    current_enemy_health = current_enemy_health - player_attack
                else:
                    print("Error: Accepted responses are '1', 'attack', '2', 'block', '3' or 'dodge'. \n")
            elif player_move == "9":
                while (confirm := input("Are you sure you want to restart or exit?").lower()) not in ["yes", "no", "y", "n"]: #confirm user wanted to restart_or_exit as they might get mixed up with stats 
                    print("Error: Accepted responses are 'yes', 'y', 'no' or 'n'")
                if confirm == "yes" or confirm == "y":
                    restart_or_exit(9)
                else:
                    pass
            elif player_move == "0":
                stats(1, current_player_health)
            if current_player_health <= 0.0: #player dies, sends to restart function
                restart_or_exit(1)
        print(f"\n{player_choices[0]} has defeated the {enemy_name}!\n")
        del enemy[-1] #removes the last enemy in list

def chapter_one(): #chance encounter
    print("You wave goodbye to the old man as you enter the Forest of Hollowcall. As you enter you notice your surroundings getting darker and darker the further you step into the forest.")
    print("The tall forest trees are dense and you cannot see the sky through them but still you feel the darkness is not natural. You sense this may be caused by the evil beast that the old man mentioned.")
    print("As you continue deeper into the forest, you see shadows moving behind the trees in front of you.")
    shadowey_response = -1
    while shadowey_response != 2: #loops until correct (option 2) is chosen
        shadowey_response = int(input("What do you do?\n\t1. Draw your weapon and run towards the shadow swinging it around in all directions.\n\t2. Slowly walk towards the shadow with your hand on your weapon.\n\t3. run away\n"))
        if shadowey_response == 1: #dumb answer loops repetitively
            print("You run towards the trees where you saw the shadow swinging your weapon and yelling. When you reach the tree there's nothing there and now you feel stupid. You see the shadow up ahead again.")
        elif shadowey_response == 2: #correct answer, passes to continue story
            pass
        elif shadowey_response == 3: #even dumber answer that ends the game
            print("You turn around and run out of the forest as fast as you can. The townspeople call you a chicken for the rest of your life.\nThe End")
            restart_or_exit(0)
        elif shadowey_response == 9: # send to restart function
            restart_or_exit(9)
        elif shadowey_response == 0: #stats command
            stats(1, 99)
        else:
            print("Thats not one of the options, choose either 1, 2 or 3")
    print("You cautiously walk towards the trees where you saw the shadows, your hand on your weapon just in case it is an enemy. When you get near, you hear rustling of foliage on the ground and call out.")
    print("'If you're behind that tree, do not be afraid, I am but a wandering adventurer and mean you no harm.' As you finish your sentence you hear hoofs on the ground and a centaur reveals itself from behind the tree.")
    print("'Hello adventurer, I am glad to see someone who has their own thoughts! Lots of creatures that live in these woods have lost their minds to a dark power emanating from deep within the forest'")
    print("'Even my brother has lost himself to the darkness, its horrible. Please adventurer, if you see him, smack some sense into him!'\n")
    print("'If I come across your brother I will try', you respond. 'If not, I shall defeat the beast controlling the innocent and free them all. Farewell'\n\n")
    input("\nPress enter to continue\n\n") #chapter end pause
    
def chapter_two(): #fighting multiple small enemies
    print("You travel in the direction the centaur gave you, thinking about how you would break such a curse without knowing the cause if you do find his brother.")
    print("While in deep thought you don't seem to notice the soft pattering that's coming closer to you until its almost too late.")
    print("3 giant rabbits pop out from behind some nearby shrubbery. They look crazed, with their eyes white as stone. You draw your weapon in preparation for attack.\n")
    fighting("Rabbit", 3, 5.0, 12.0)
    print("All rabbits have been defeated! The darkness of the forest makes it difficult know what time it is but you have been travelling for some time now so you decide now is a good time to rest, ")
    print("especially since you now have these rabbits to cook up!\nHealth fully restored!")
    stats(1, 99)
    input("\nPress enter to continue\n\n") #chapter end pause

def chapter_three(): #fighting one big enemy
    print("As you head deeper into the forest you, you feel a strange pull in one direction. You follow it and as you get closer you start to hear soft whispers in a language you don't understand, but it sounds almost like a chant")
    print("You walk in the direction of the feeling and as you do, you realise that the whispers aren't out loud but in your head. The closer you get to the feeling, the louder the chanting becomes and the more aggressive it sounds")
    print("Your years of training in all sorts of magic resistance has done you well as you can tell that it is the only reason the chanting isn't infecting you like it has the other creatures of the forest.")
    print("As you draw near a mountain, you see a massive cave in the side of it. The chanting, almost at a shout now, sounds like it is coming from in the cave.")
    print("You approach the cave and notice that a creature is standing in front of it. The creature is a centaur that looks much like the one you saw earlier, this must be his brother!")
    print("Suddenly the centaur turns around and looks directly at you, its eyes much like the rabbits were. The centaur lets out a deafening scream as it sprints towards you.")
    fighting("Centaur", 1, 20, 30)
    print("The centaur collapses to the ground. You approach cautiously, concerned that you may have killed the kind centaurs brother!")
    print("As you approach the centaur lifts its head with a groan and you jump backwards, ready to fight if it attacks again.")
    print("He looks at you and you see a much kinder face, his eyes no longer all white. 'You are one hell of a fighter, human', he says as he stands up.")
    print("'Your brother sent me and told me to beat some sense into you.' you respond. The centaur lets out a howling laugh. 'Of course he did! He always thinks a beating is the answer, this time he was right!'")
    print("'Thankyou for freeing me human, I am forever in your debt. You can have this health potion. Is there anything I can do to help you?'\nHealth fully restored!")
    stats(1, 99)
    input("\nPress enter to continue\n\n") #chapter end pause

def chapter_end(): #fighting the boss and winning the prize
    print("'I am looking for the Treasure of Dragonscorn and heard rumours that the beast that was controlling the creatures of this forest is protecting some kind of relic.'")
    print("'I was hoping the two legendary items were one in the same.'")
    print("'Ah an ancient artifact you say? I'm not sure if its the treasure you are looking for but the beast has a very powerful looking sword within its cave'")
    print("'That sounds exactly like the treasure I am searching for!, Thankyou for your help.'")
    print("'Be warned, the beast is a very dangerous being!' The centaur then trots off towards the way you came.\n\n")
    print("You enter the large cave, its walls dark, the only light coming from deep inside.")
    print("You walk towards the light, drawing your sword just in case the beast sneaks up on you. The light gets brights and brighter until you get to the heart of the cave.")
    print("In the center of the opening you see a large creature, as black as obsidian and scaly. You realise that the beast is a dragon!")
    print("Across the room, on a pile of gold you see a shining crimson blade of a sword. At the same time the Dragon turns and sees you standing in its cave")
    print("The dragon flies up into the air, readying to attack you...")
    fighting("Dragon", 1, 50, 80)
    print("You pull the blade out of the giant creature, its blade seems to shine an even brighter shade of crimson with dragon blood on it")
    print("You feel the dark chanting disappear within your mind but it is replaced with a soothing, warm humm.")
    print("The sword has accepted you as its owner and will only be its strongest if wielded by you")
    print("\n\n\t\tThe End\n\n\n")
    

option_message = "For restart select '9' and for current stats select '0'"
player_choices = prologue()
player_stats = stats(0, 99) #used to point to certain stats
chapter_one()
chapter_two()
chapter_three()
chapter_end()

restart_or_exit(0) #send to restart or exit function with code 0 to not signal the death message
