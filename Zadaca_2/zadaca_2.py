print('Zadatak 1:')

consonants = 'yzf xrl prltty gzzd xt thms'
newSentence = consonants.replace('x', 'a').replace('l', 'e').replace('m', 'i').replace('z', 'o').replace('f', 'u')

print('Replaced:', newSentence)

print('\nZadatak 2:')

vanjaSays = 'Inoslav je danas slistio cijeli avokado.'
hiddenMessage = vanjaSays[1] + vanjaSays[5] + vanjaSays[8] + vanjaSays[10] + vanjaSays[15] + vanjaSays[19]

print('Hidden message:', hiddenMessage)

print('\nZadatak 3: Without "SPACE"')

recenica = 'StvarnoSPACEsuSPACEgrozneSPACEoveSPACEMacbookSPACEProSPACEtipkovnice.'
novaRecenica = recenica.replace('SPACE', '\n')

print(novaRecenica)


print('\nZadatak 4:')

cute = 'jasamigormancesvirambubnjeveivolimte'

print('Cute message:', cute[-7:])


print('\nZadatak 5:')

sms1 = 'Ajde kupi Cokolino, gladan sam!'
sms2 = 'Nalazimo se sutra u 7 kod Lane. Stizes?!?'
sms3 = 'Pao sam s romobila. Please zovi hitnu.'

print('Average:', (len(sms1) + len(sms2) + len(sms3)) / 3)


print('\nZadatak 6:')

nevenSays = '>w<<>o[[[[[w{}{i::a&*!%m@@@re(a&%$l;:;l__—y?*aLKJm*a**z!e$$dSDaMBMMt%t*?=h222iQWEs%$ASD&p&o%i123n!—t'

nevensMessage = ''
for letter in nevenSays:
    if letter.islower():
        nevensMessage += letter

print('Coherent message:', nevensMessage)


print('\nZadatak 7:')

inoslavsMessage = 'ptof xn yn rnhf mfpjwnhf'
anotherMessage = 'forj rjsn snoj rn itgwt, efxuft xfr sf aqfp'

decipheredMessage = ''

for letter in anotherMessage:

    if ord(letter) >= 97:
        if (ord(letter) - 5) < 97:
            character = (ord(letter) - 5) + 26
        else:
            character = ord(letter) - 5
    else:
        character = ord(letter)

    decipheredMessage += chr(character)

print('Deciphered message:', decipheredMessage)
