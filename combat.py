import Luthien

def combat(skill, health, enemyskill, enemyhealth, name):
    damage = 2
    while enemyhealth > 0:
        print("**********************")
        print("Your Ship Skill: {} Health: {} | {} Ship Skill: {} Health: {}".format(skill, health, name, enemyskill,
                                                                                enemyhealth))
        yourroll = Luthien.d6() + Luthien.d6() + skill
        enemyroll = Luthien.d6() + Luthien.d6() + enemyskill

        print("You rolled a skill of {} while they rolled a skill of {}".format(yourroll, enemyroll))
        if yourroll > enemyroll:
            print("The enemy has taken {} damage".format(damage))
            enemyhealth -= damage
        elif enemyroll > yourroll:
            print("You have taken {} damage".format(damage))
            health -= damage
            if health < 1:
                print("Your ship has taken critical damage and was destroyed")
                exit(0)
        else:
            print("You both are unable to damage each other")
    print("{} has been destroyed!!!!!!!!!!!!!".format(name))
    return health

def enemy(system, skill, health):
    enemyskill = 5 + system
    enemyhealth = 5 + system
    print("You have encountered an enemy pirate ship with skill {} and health {}".format(enemyskill, enemyhealth))
    return combat(skill, health, enemyskill, enemyhealth, "Pirate")