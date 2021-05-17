woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche", "Melone", "Marille", "Pfirsich"]
#print(len(woerterbuch_deutsch))
woerterbuch_english = ["apple", "pear", "cherry", "melon", "apricot", "peach"]
#print(woerterbuch_english)
#print(woerterbuch_english[2])
#print(woerterbuch_deutsch[0])
#deutsch = input("Gesuchte Frucht eingeben:")
#wort = woerterbuch_deutsch.index(deutsch)
#if deutsch == wort:
    #print("Ja")




    
auswahl = input("Befehl? [E]ingabe, [L]öschen, [A]bfrage:")

if auswahl == "E" or auswahl == "e" :
    sprache = input("Ins [D]eutsche oder [E]nglische übersetzen?")

    if sprache == 'D' or sprache == 'd':
            wort1 = input("Zu einfügendes Wort:")
            woerterbuch_deutsch.append(wort1)
            print(wort1, "wurde eingefügt!")
            print(woerterbuch_deutsch)
        
    
    elif sprache == "e" or sprache == "E":
            wort2 = input("Zu einfügendes Wort:")
            woerterbuch_english.append(wort2)
            print(wort2, "wurde eingefügt!")
            print(woerterbuch_english)
        
elif auswahl == "l" or auswahl == "L":
    löschen = input("Aus dem [D]eutschen oder [E]nglischen löschen?")
    if löschen == "d" or löschen == "D":
        lwortd = input("Zu löschendes Wort:")
        woerterbuch_deutsch.remove(lwortd)
        print(lwortd, "wurde gelöscht!")
        print("Die neue Liste lautet:", woerterbuch_deutsch)
    elif löschen == "e" or löschen == "E":
        lworte = input("Zu löschendes Wort:")
        woerterbuch_english.remove(lworte)
        print(lworte, "wurde gelöscht!")
        print("Die neue Liste lautet:", woerterbuch_english)

else:
    max = len(woerterbuch_deutsch)
    emax = len(woerterbuch_english)
    
    eingabe = input("Frucht eingeben:")

    index = 0

    while index < max:
        if woerterbuch_deutsch[index].upper() == eingabe.upper():
            print(woerterbuch_english[index], "(EN)")
            break
        
        if woerterbuch_english[index].upper() == eingabe.upper():
            print(woerterbuch_deutsch[index], "(DE)")
            break
        index += 1
    
    if index == max:
        print("Keine Frucht gefunden!")

































