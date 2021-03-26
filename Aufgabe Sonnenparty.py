# einfaches `=´ Zeichen: Zuweisung
strWetter = input("Wochenendwetter - `sonnig´ oder `regnerisch´?")
# doppeltes `=´Zeichen: Vergleichsoperator

#if statement
if strWetter == "sonnig":
    print("Gartenparty!")

#oder
elif strWetter == "regnerisch":
    print("Kellerparty")

elif strWetter == "bewölkt":
    print("Bitte abstimmen")

#sonst
else:
    print("Bitte sonnig oder regnerisch eingeben!")
    
    
    