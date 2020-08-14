import random
import sys

print('Zadatak 1:')

inp = input('Say something:')

if len(inp) < 20:
    if 'joj' in inp or 'hm' in inp:
        print('You are lying.')
    else:
        print('Less than 20. You are lying.')
elif 20 <= len(inp) <= 40:
    print('Ok, you are telling the truth.')
elif len(inp) > 40:
    print('More than 40. You are lying.')


numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

suma = 0
for num in numbers:
    if num % 2 != 0:
        suma += num

print('\nZadatak 2:')
print('Sum:', suma)


print('\nZadatak 3:')

jobs = ["The tester", "The cajka", "The fireman", "The surgeon", "The programmer"]
adverbs = ["somewhat", "slightly", "extremely"]
adjectives = ["happy", "crazy", "anxious", "insane", "sexy"]
hairColors = ["blond", "purple", "pink", "red"]

for i in range(0, 5):
    print('Character ' + str(i + 1) + ': ' + random.choice(jobs) + ' is ' + random.choice(adverbs),
          random.choice(adjectives) + ' and has ' + random.choice(hairColors) + ' hair.')


print('\nZadatak 4:')

pozvani = ["Otto", "Neven", "Mario", "Lana", "Ana", "Tihana", "Ino", "Nikolina"]

newList = []
for i in pozvani:
    i = i.lower()
    rev = i[::-1]
    if i != rev:
        newList.append(i)

    newList.sort()

print('Final list:', newList)


print('\nZadatak 5:')

cijene = []

for i in range(3):
    cijenaPopravkaRemena = input("Upisi cijenu popravka zupcastog remena za " + str(i + 1) + ". automehanicara: ")
    cijenaPopravkaBranika = input("Upisi cijenu popravka branika za " + str(i + 1) + ". automehanicara: ")
    popust = input("Upisi popust za " + str(i + 1) + ". automehanicara: ")

    try:
        cijenaPopravkaRemena = int(cijenaPopravkaRemena)
        cijenaPopravkaBranika = int(cijenaPopravkaBranika)
        popust = int(popust)

        if (not type(cijenaPopravkaRemena) is int) or (not type(cijenaPopravkaBranika) is int) or (not type(popust) is int):
            raise ValueError('Cijene moraju biti pozitivni cijeli brojevi.')
        elif (cijenaPopravkaRemena < 0) or (cijenaPopravkaBranika < 0) or (popust < 0):
            raise Exception('Cijene moraju biti pozitivni cijeli brojevi.')
        else:
            cijene.append([int(cijenaPopravkaRemena), int(cijenaPopravkaBranika), int(popust)])

    except ValueError as er:
        print(er)
        sys.exit('Exiting because of an error...')
    except Exception as ex:
        print(ex)
        sys.exit('Exiting because of an excetion...')


renatoCijena = (cijene[0][0] + cijene[0][1]) - ((cijene[0][2] / 100) * (cijene[0][0] + cijene[0][1]))
marinaCijena = (cijene[1][0] + cijene[1][1]) - ((cijene[1][2] / 100) * (cijene[1][0] + cijene[1][1]))
lukaCijena = (cijene[2][0] + cijene[2][1]) - ((cijene[2][2] / 100) * (cijene[2][0] + cijene[2][1]))

if renatoCijena < marinaCijena and renatoCijena < lukaCijena:
    print('Renato ima najpovoljniju ponudu od ' + str(renatoCijena))
elif marinaCijena < renatoCijena and marinaCijena < lukaCijena:
    print('Marina ima najpovoljniju ponudu od ' + str(marinaCijena))
elif renatoCijena == lukaCijena == marinaCijena:
    print('Ista cijena kod svih automehanicara.')
else:
    print('Luka ima najpovoljniju ponudu od ' + str(lukaCijena))
