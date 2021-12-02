
from module1 import *
from keyboard import *
palgad=loe_failist_listisse("palgad.txt")
inimesed=loe_failist_listisse("inimesed.txt")
while 1:
    print("*"*100,"\nKeskmine - 1\nMaksimaalne -2\nOtsing -3\nLisa - 4")
    print("Vali ")

    if read_key()=="1":
        kesk=keskmine(inimesed,palgad)
        print("Keskmine palk on ",summa)

    elif read_key()=="2":
        suurim,kellel=suurim(inimesed,palgad)
        print("Maksimaalne palk=> ", suurim, " Kellel=> ",kellel)
   
    elif read_key()=="3":
        vastus=otsing_nimi_jargi(inimesed, palgad)
        print(vastus)

    elif read_key()=="4":
        palgad,inimesed=lisa(palgad,inimesed)
        print(palgad,inimesed)

    
