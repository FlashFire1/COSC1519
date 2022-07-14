'''
Created on 19 Sept 2021

@author: Eamon
'''

def stats(adjust_health, is_hurt): #stat_call for if user asked for stat readout. adjust_health is for removing or adding health to character. is_hurt defines if the health is base_health or health
    #setting base stats
    base_health = 25.0  #base health stats
    base_attack = 7   #base attack stats
    base_position = 2 #base position stats 
    #adjusting health
    if is_hurt == True: #this is needed to identify if any health changes have happened
        health = health - adjust_health
    else:
        health = base_health
    return [health, base_attack, base_position]

calling = stats()
print(calling[0])
stats(10, True)
print(calling[0])

input('enter')
