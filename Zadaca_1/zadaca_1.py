import datetime

print('\nZadatak 2:')

ime = "Dino"
prezime = "Vinkovic"

print(ime.upper(), prezime.upper())


print('\nZadatak 3:')

dan = 1
mjesec = 7
godina = 1990

print(str(dan) + "." + str(mjesec) + "." + str(godina) + ".")


print('\nZadatak 4:')
danasnjiDatum = datetime.datetime.now()

print(str(ime), str(prezime) + " ima " + str(danasnjiDatum.year - godina) + " godina.")


print('\nZadatak 5:')

if danasnjiDatum.month < mjesec:
    print(str(ime), str(prezime) + " ima " + str(danasnjiDatum.year - godina - 1) + " godina.")
else:
    print(str(ime), str(prezime) + " ima " + str(danasnjiDatum.year - godina) + " godina.")
