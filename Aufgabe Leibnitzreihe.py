# Leibitzreihe zur Annäherung der Zahl Pi

name = input("Benutzername:")
print("Hallo Benutzer", name)


i = int(input("Anzahl an Interationen:"))
zahlInt = 0
# ist die aktuelle Laufvariable

piAnnäherung = 0

while zahlInt < i:
    piAnnäherung += (-1)**zahlInt/(2*zahlInt+1)
    # Leibnitzreihe wird berechnet
    print("Der Zwischenwert lautet:", piAnnäherung)
    zahlInt += 1
    
piAnnäherung *= 4 # mit 4 multiplizieren um Leibnitzreihe zu Erfüllen
print("Annäherung an Pi:", piAnnäherung)

