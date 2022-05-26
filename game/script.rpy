init python:
    from __future__ import print_function
    from __future__ import absolute_import
    from __future__ import division
    from __future__ import unicode_literals
    from builtins import round
    from builtins import range
    from builtins import int
    from builtins import input
    from future import standard_library
    standard_library.install_aliases()
    import math
    import future
    import charactersEnemy
    import charactersPlayer
    import random
    import time

    

python:

    playerList = []
    enemy = {}
    charactersSelected = 0
    charactersInMenu = 0

define Unknown = Character("???")
define e = Character("")
define nUtsuho = Character("Utsuho")
define nOrin = Character("Orin")
define nGruntA = Character("Grunt A")
define nGruntB = Character("Grunt B")
define nGruntC = Character("Grunt C")



label start:

    Unknown "Where would you like to begin this story?"

    menu:

        "Remains of Blazing Hell":
            jump Utsuho1

        "Kourindou":
            return

        "Moriya Shrine":
            return

label Utsuho1:

    e "Remains of Blazing Hell"
    nUtsuho "Orin?"
    nOrin "Yeah?"
    nUtsuho "Do you think Satori-sama will make eggs for dinner tonight?"
    nOrin "Do you ever want to eat anything else?"
    nUtsuho "..."
    nUtsuho "No?"
    nOrin "..."
    nOrin "She'll probably have some ready for you."
    nUtsuho "Yay!"
    nOrin "Hmm? What was that?"
    nGruntA "Go Rattata!"
    nGruntB "Here comes Zubat!"
    nGruntC "Don’t forget Muk!"
    nGruntA "Hahaha! As you can see you’re surrounded!"
    nGruntB "So give us all your Pokemon!"
    nGruntC "Or else!"
    nUtsuho "What’s a Pokemon?"
    nOrin "I have no idea."
    nGruntA "What? You don’t know what Pokemon are?"
    nGruntB "Um... then what do we do?"
    nGruntC "Uh... demand cash?"
    nGruntA "That works! Give us all your money!"
    nUtsuho "No! You can’t have my money!"
    nOrin "Okuu, you don’t have any money..."
    nUtsuho "Oh yeah..."
    nGruntA "Ugh! Enough talking! Let’s fight!"

    python:
        playerList = charactersPlayer.utsuho1
        enemy = charactersEnemy.rocket1
    
    jump battleStart

    return

label battleStart:

    python:
        code = "XXXX"
        # Character Lists
        
        player = {}

        # Character Slots and Turn Order
        turnList = []
        slotList = []
        slot = {}
        # Character Actions to take next
        action = {}
        target = {}
        # extra attacks
        targetEx = {}

        # Displays enemies at the start and removes enemy[0]

        """
        # displays enemies for selection. Only alive ones
        def displayEnemies ():
            for x in range(1, len(enemy)+1):
                if enemy[x].isAlive == True:
                    print(f" {x}. {enemy[x].name}")

        # Returns a list of alive characters, player or enemy
        def listAliveCharacters (dict):
            aliveList = []
            for x in range(1, len(dict)+1):
                if dict[x].isAlive == True:
                    aliveList.append(dict[x])
            return aliveList

        # Returns a list of useable skills
        def listActiveSkills (user):
            activeSkills = []
            for x in range(0, len(user.skillList)):
                if user.skillList[x].cooldown == 0:
                    activeSkills.append(x)
            return activeSkills

        # lowers skill cooldowns by 1
        def lowerSkillCooldown (user):
            for x in user.skillList:
                if x.cooldown != 0:
                    x.cooldown -= 1



        # Displays player's slots
        def displayPlayers ():
            for x in range(1, len(player)+1):
                print(f" {x}. {player[x].name}")

        # Displays skills for a particular character
        def listSkills (user):
            print(f"--{user.name}-- [{user.hp}/{user.maxHp}] HP")
            for x in range(len(user.skillList)):
                if user.skillList[x].cooldown == 0:
                    print(f" {x}. {user.skillList[x].name}")
                else:
                    if user.skillList[x].cooldown == 1:
                        turns = "turn"
                    else:
                        turns = "turns"
                    print(f" X. {user.skillList[x].name} [Cooldown: {user.skillList[x].cooldown} {turns}]")

        # Use a skill.
        def useSkill(user, skill, target):
            if target in player.values():
                party = player
            if target in enemy.values():
                party = enemy
            if user.skillList[skill].type in [0,2,4,6]:
                party = listAliveCharacters(party)
            if user.skillList[skill].type in [0,1,2]:
                if target.hp == 0:
                    if target in player.values():
                        try:
                            target = random.choice(listAliveCharacters(player))
                        except:
                            pass
                    if target in enemy.values():
                        try: 
                            target = random.choice(listAliveCharacters(enemy))
                        except:
                            pass
            if target != []:
                user.skillList[skill].skill(user,target,party)

        # use Basic Attack
        def useBasicAttack (user, target):
            if target in player.values():
                party = player
            if target in enemy.values():
                party = enemy
            party = listAliveCharacters(party)
            if target.hp == 0:
                    if target in player.values():
                        try:
                            target = random.choice(listAliveCharacters(player))
                        except:
                            pass
                    if target in enemy.values():
                        try: 
                            target = random.choice(listAliveCharacters(enemy))
                        except:
                            pass
            user.skillList[0].skill(user,target,party)

        # choose actions loop
        def chooseActions ():
            for x in range(1, len(player)+1):
                if player[x].isAlive == True:
                    listSkills (player[x])
                    action[x] = int(input("Choose a skill: "))
                    if player[x].skillList[action[x]].type in [1,2,3]:
                        if player[x].skillList[action[x]].type == 2:
                            displayEnemies ()
                            target[x] = enemy[int(input(f"Choose a target for {player[x].skillList[action[x]].name}: "))]
                        if player[x].skillList[action[x]].type in [1,3]:
                            displayPlayers ()
                            target[x] = player[int(input(f"Choose a target for {player[x].skillList[action[x]].name}: "))]
                        displayEnemies ()
                        targetEx[x] = enemy[int(input(f"Choose a target for {player[x].skillList[0].name}: "))]
                    if player[x].skillList[action[x]].type in [0]:
                        displayEnemies ()
                        target[x] = enemy[int(input(f"Choose a target for {player[x].skillList[action[x]].name}: "))]
                        targetEx[x] = 0
                    if player[x].skillList[action[x]].type in [4,6]:
                        target[x] = random.choice(listAliveCharacters(enemy))
                        targetEx[x] = 0
                    if player[x].skillList[action[x]].type in [5,7]:
                        target[x] = random.choice(listAliveCharacters(player))
                        targetEx[x] = 0
                else:
                    action[x] = 0
                    target[x] = random.choice(listAliveCharacters(enemy))
                    targetEx[x] = 0

        # chooses enemy actions and targets
        def enemyActions ():
            players = len(player)
            for x in range(1, len(enemy)+1):
                action[x+players] = random.choice(listActiveSkills(enemy[x]))
                if enemy[x].skillList[action[x+players]].type in [1,5]:
                    target[x+players] = random.choice(listAliveCharacters(enemy))
                if enemy[x].skillList[action[x+players]].type in [3,7]:
                    target[x+players] = random.choice(list(enemy.values()))
                if enemy[x].skillList[action[x+players]].type in [0,2,4,6]:
                    target[x+players] = random.choice(listAliveCharacters(player))
                targetEx[x+players] = 0

        # Helps turnOrder sort or something
        def turnKey(self):
            return self.turnNumber

        # redefines turnList, slotList and slot
        def turnOrder ():
            turnList.clear ()
            slotList.clear ()
            # add all characters to turnList    
            for x in range(1, len(player)+1):
                turnList.insert(x, player[x])
            for x in range(1, len(enemy)+1):
                turnList.insert(x+int(len(player)), enemy[x])
            # slot part
            for x in range(1, len(turnList)+1):
                slot[x] = turnList[x-1]
            slotList.extend(turnList)
            # sort turnList
            for x in turnList:
                x.turnNumber = x.spd + random.randint(0, 5)
            turnList.sort(key = turnKey, reverse = True)

        # a round of combat
        def round ():
            for x in range(0, len(turnList)):
                y = slotList.index(turnList[x])+1
                slot[y].statUpdate ()
                target[y].statUpdate ()
                if slot[y].isAlive == True:
                    if slot[y].skillList[action[y]].cooldown == 0:
                        time.sleep(0.2)
                        useSkill(slot[y], action[y], target[y])
                        slot[y].statUpdate ()
                        target[y].statUpdate ()
                        if targetEx[y] != 0:
                            time.sleep(0.2)
                            useBasicAttack (slot[y], targetEx[y])
                            slot[y].statUpdate ()
                            targetEx[y].statUpdate ()
                aPlayers = 0
                aEnemies = 0
                for x in range(1, len(enemy)+1):
                    if enemy[x].isAlive == True:
                        aEnemies += 1
                for x in range(1, len(player)+1):
                    if player[x].isAlive == True:
                        aPlayers += 1        
                if aPlayers == 0:
                    break
                if aEnemies == 0:
                    break

            for x in range(1, len(slot)+1):
                slot[x].rotateStatChanges ()
                lowerSkillCooldown (slot[x])

    """






    $ result = 0
    $ battleOver = False
    $ playerWon = False
    $ enemyWon = False
    jump encounter
    python: 
        """
        $ characterSelect ()
        while battleOver == False:
            $ chooseActions ()
            $ turnOrder ()
            $ enemyActions ()
            $ round ()
            $ alivePlayers = 0
            $ aliveEnemies = 0
            python:
                for x in range(1, len(enemy)+1):
                    if enemy[x].isAlive == True:
                        aliveEnemies += 1
                for x in range(1, len(player)+1):
                    if player[x].isAlive == True:
                        alivePlayers += 1        
                if alivePlayers == 0:
                    battleOver = True
                    enemyWon = True
                if aliveEnemies == 0:
                    battleOver = True
                    playerWon = True
        python:
            for x in range(1, len(enemy)+1):
                enemy[x].reset()
            for x in range(1, len(player)+1):
                player[x].reset()
        if playerWon == True:
            $result = "next"
            $input(f"You Won!")
        if enemyWon == True:
            $input("You Lost...")
            $print("1. Try again")
            $print("2. Skip Battle")
            $print("3. Main Menu")
            $result = int(input("Choose a number: "))
            if result == 1:
                $result = "repeat"
            if result == 2:
                $result = "next"
            if result == 3:
                $result = "menu"
        return
        """

label encounter:

    python:
        enemy[0] = "Enemies"
        encounterList = ""
        for x in range(1, len(enemy)-1):
            encounterList += "%s, " % (enemy[x].name)
        encounterList += "and %s!" % (enemy[int(len(enemy)-1)].name)
        del enemy[0]

    e "Encountered [encounterList]"

    jump characterSelect

label characterSelect:

    e "Select a Team."

    while charactersSelected != 4 or len(playerList)-1:

        $ charactersSelected += 1

        menu:

            while charactersInMenu != len(playerList)-1:

                $ charactersInMenu += 1

                "[playerList[charactersInMenu].name]":
                    player[charactersSelected] = playerList[charactersInMenu]

























