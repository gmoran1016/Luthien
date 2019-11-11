import time

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
            time.sleep(1.5)
        elif enemyroll > yourroll:
            print("You have taken {} damage".format(damage))
            health -= damage
            time.sleep(1.5)
            if health < 1:
                selection = input("Your ship has taken critical damage and was destroyed\n would you like to play "
                                  "again?(y/n)")
                if selection == 'y':
                    Luthien.main()
                exit(0)
        else:
            print("You both are unable to damage each other")
    print("{} has been destroyed!!!!!!!!!!!!!".format(name))
    return health


def enemy(system, skill, health):
    enemyskill = 5 + system
    enemyhealth = 5 + system
    print("You have encountered an enemy pirate ship with skill {} and health {}".format(enemyskill, enemyhealth))
    input("Press Enter to continue")
    return combat(skill, health, enemyskill, enemyhealth, "Pirate")


def finalboss(skill, health, max_health, repairToolAmount):
    enemyskill = 12
    enemyhealth = 24
    print("Ah it is Eridu AAAAAAAAAHHHHHHHHHHHHHHH")
    print("Eridu's ship is strong and will not go down easy, he has a skill of {} and health of {}".format(enemyskill,
                                                                                                           enemyhealth))

    damage = 2
    while enemyhealth > 0:
        print("**********************")
        print("Your Ship Skill: {} Health: {} | {} Ship Skill: {} Health: {}".format(skill, health, "Eridu", enemyskill,
                                                                                     enemyhealth))

        if repairToolAmount > 0 and health < max_health:
            selection = input("Would you like to use one of your repair tools (you have {} with a health of {} "
                              "out of {}), y or n?".format(repairToolAmount, health, max_health))
            if selection == 'y':
                health += Luthien.d6() + Luthien.d6() - damage
                repairToolAmount -= 1
                if health > max_health:
                    health = max_health
        yourroll = Luthien.d6() + Luthien.d6() + skill
        enemyroll = Luthien.d6() + Luthien.d6() + enemyskill

        print("You rolled a skill of {} while Eridu rolled a skill of {}".format(yourroll, enemyroll))
        if yourroll > enemyroll:
            print("The enemy has taken {} damage".format(damage))
            enemyhealth -= damage
        elif enemyroll > yourroll:
            print("You have taken {} damage".format(damage))
            health -= damage
            if health < 1:
                selection = input("Your ship has taken critical damage and was destroyed\n would you like to play "
                                  "again?(y/n)")
                if selection == 'y':
                    Luthien.main()
                exit(0)
        else:
            print("You both are unable to damage each other")
