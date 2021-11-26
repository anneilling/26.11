from module1 import*
while 1:
    print("A - Sisesta,\n E - Ekraanile,\n")
    valik=input()
    if valik.lower()=="A":
       inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=="E":
        andmed_ekranile(inimesed,palgad)
    elif valik.lower()=="K":
        inimesed,palgad=kustuta(inimesed,palgad)
    
    
