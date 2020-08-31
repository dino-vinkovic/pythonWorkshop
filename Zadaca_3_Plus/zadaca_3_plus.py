import random

print('*** Legend of Ino ***')

def printCharacterDetails(name, healthPoints, magicPoints):
    print('Name:', name, 'HP:', healthPoints, 'MP:', magicPoints, '\n')

# Calculate hit points for character according to his details
def calculatePoints(character):
    randomHP = random.randrange(0, int((character.healthPoints / 2)) + 1)
    randomMP = random.randrange(0, int((character.magicPoints / 2)) + 1)
    hitPoints = (randomHP + randomMP) * 2
    return hitPoints

# Ask player if he wants a health potion
def doctorCheckUp(player):
    wantMoreHP = input('Do you want a health potion? (y \ n) ')

    additionalHp = random.randrange(10, 50)
    if wantMoreHP.lower() == 'y':
        player.healthPoints += additionalHp
        print('You got additional HP.', additionalHp)
    else:
        pass

# Send details for two characters and calculate who wins
def fight(player, enemy):
    count = 1
    countDoctorCheckUp = 0

    print(enemy.name, 'has appeared!')
    while min(player.healthPoints, enemy.healthPoints) > 0:
        print('Round #' + str(count))

        playerHitPoints = calculatePoints(player)
        enemyHitPoints = calculatePoints(enemy)

        if playerHitPoints > enemyHitPoints:
            enemy.healthPoints -= playerHitPoints
            print(player.name + ' hit ' + enemy.name + ' with ' + str(playerHitPoints) + '. ' +
            enemy.name + ' hit ' + player.name + ' with ' + str(enemyHitPoints) + '. ' +
            player.name + ' wins the round.')
        else:
            player.healthPoints -= enemyHitPoints
            print(enemy.name + ' hit ' + player.name + ' with ' + str(enemyHitPoints) + '. ' +
            player.name + ' hit ' + enemy.name + ' with ' + str(playerHitPoints) + '. ' +
            enemy.name + ' wins the round.')

        printCharacterDetails(player.name, player.healthPoints, player.magicPoints)
        printCharacterDetails(enemy.name, enemy.healthPoints, enemy.magicPoints)
        count += 1

    if (player.healthPoints > 0) and (enemy.healthPoints <= 0):
        print(player.name + ' wins the fight against ' + enemy.name + '!\n')
        player.healthPoints += 70
        player.magicPoints += 30
    else:
        if (player.healthPoints <= 0) and (countDoctorCheckUp < 3):
            doctorCheckUp(player)
            countDoctorCheckUp += 1
            print(player.healthPoints)
        else:
            print('You lose.', enemy.name, 'wins the fight!\n')

class Character:
    def __init__(self, name, healthPoints=None, magicPoints=None):
        self.name = name
        self.healthPoints = healthPoints
        self.magicPoints = magicPoints

    def addType(self, healthPoints, magicPoints):
        self.healthPoints = healthPoints
        self.magicPoints = magicPoints

    def addWeapon(self, weapon):
        self.weapon = weapon

# Prompt user for character's name and check if they typed in a non-letter or space
selectCharacterName = input("What is your character's name: ")

while not selectCharacterName.isalpha() or selectCharacterName.isspace():
    selectCharacterName = input("What is your character's name: ")

# Create player's character with entered name
playersCharacter = Character(selectCharacterName)

# Prompt the user to select the character's type
selectCharacterType = input("""\nType in the number next to the type you want to choose:
    1 - Human
    2 - Troll
    3 - Wizard
    """)

# Check whether the user typed in one of the proposed values
while selectCharacterType.isalpha() or selectCharacterType.isspace() or \
        (int(selectCharacterType) <= 0) or (int(selectCharacterType) > 3):
    print("Please select 1, 2 or 3.")
    selectCharacterType = input("""\nType in the number next to the type you want to choose:
    1 - Human
    2 - Troll
    3 - Wizard
    """)

# If valid value is typed in, add the HP and MP to the character by selected type
if selectCharacterType == '1':
    playersCharacter.addType(100, 50)
elif selectCharacterType == '2':
    playersCharacter.addType(200, 0)
elif selectCharacterType == '3':
    playersCharacter.addType(50, 100)

# Prompt the user to select a weapon and add it to the character
selectWeapon = input("""Type in the number next to the weapon you want to choose:
    1 - Mancetov Crveni Spojler
    2 - Anin Nokat Istine
    3 - Vanjina Puska Pravde
    """)

weapons = ['Mancetov Crveni Spojler', 'Anin Nokat Istine', 'Vanjina Puska Pravde']

# Check whether the user typed in one of the proposed values
while selectWeapon.isalpha() or selectWeapon.isspace() or \
        (int(selectWeapon) <= 0) or (int(selectWeapon) > 3):
    print("Please select 1, 2 or 3.")
    selectWeapon = input("""Type in the number next to the weapon you want to choose:
    1 - Mancetov Crveni Spojler
    2 - Anin Nokat Istine
    3 - Vanjina Puska Pravde
    """)

if selectWeapon == '1':
    playersCharacter.addWeapon(weapons[0])
    playersCharacter.magicPoints += 30
    print('You have selected the following weapon:', weapons[0])
elif selectWeapon == '2':
    playersCharacter.addWeapon(weapons[1])
    playersCharacter.healthPoints += random.randrange(-20, 21)
    playersCharacter.magicPoints += random.randrange(10, 71)
    print('You have selected the following weapon:', weapons[1])
elif selectWeapon == '3':
    playersCharacter.addWeapon(weapons[2])
    playersCharacter.magicPoints += random.randrange(0, 101)
    print('You have selected the following weapon:', weapons[2])

#Print the details of the created character
printCharacterDetails(playersCharacter.name, playersCharacter.healthPoints, playersCharacter.magicPoints)

# Create enemies
naughtyNikolina = Character('Naughty Nikolina', 75, 75)
malevolentMilutin = Character('Malevolent Milutin', 100, 15)
lazyLana = Character('Lazy Lana', 120, 50)

enemies = [naughtyNikolina, malevolentMilutin, lazyLana]

# Fight with each enemy
countWin = 0
for enemy in enemies:
    fight(playersCharacter, enemy)

    if enemy.healthPoints <= 0:
        countWin += 1
    else:
        continue

# Player wins the game and saves Inoslav if he defeats all enemies
if countWin == 3:
    print(playersCharacter.name + ' survived and saved Inoslav.')
else:
    print('You have failed this quest!')