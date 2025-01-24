from random import random

diceOption = list(range(1,7))

#wepons list
wepons = ["fist","knife","club"]
print("avalible wepond", ", ".join(wepons))

def getCombatStrenght(promt):
    {
        while true:
            value = int(input(promt))
        if I <= value: <= 6;
            return value
        else:
            print("invalid input: please enter a number between 1 and 6");
    }

 combatStrenght() = getCombatStrenght("please enter a number between 1 and 6 for player");
 mcombatStrenght() =getCombatStrenght("please enter a number between 1 and 6 for monster");

 for j in range(1,21,2):
    heroRoll = random.choice(diceOption)
    monsterRoll = random.choice(diceOption)

    heroWepon = wepons[heroRoll -1]
    monsterWepon = wepons[monsterRoll -1]

    heroTotal = combatStrenght + heroRoll
    monsterTotal = combatStrenght + monsterRoll

    if heroTotal > monsterTotal:
        print("hero won!");
    elif monsterTotal > heroTotal:
        print("monster won!");
    else
        print(" it's a tie!");

