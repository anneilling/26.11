  #funktsioonide loomine
from random import *
def loe_failist_listisse(file:str)->list:
    """Loeme tekst failist ja salvesta järjendisse
    :rtype: list:
    """
    file=open(file,"r")
    list_=[]
    for stroka in file:
        list_.append(stroka.strip())
    file.close()
    return list_

def otsing_nimi_jargi(inimesed:list,palk:list):
   """otsime inimest nimi järgi
   :rtype: str:
   """
   nimi=input("Keda otsime?")

   for inimene in inimesed:

       if inimene.upper()==nimi.upper():

           n=inimesed.count(nimi)
           print("Leitud",n, "korda")
           b=0
           t=[]
           for i in range(n):
               k=inimesed.index(nimi,b)
               palk=palk[k]
               b+=k+1
               t.append(nimi+str(palk))
               print(nimi, palk)
       else:
           t="Ei ole nimi kirjas"
           return t


def lisa(palk:list,inimesed:list): #i-inimeste list, p-palgade list
    #lisa inimesi ja palga
    #:rtype:str,str:
    a=input("Sissesta nimi ")
    inimesed.append(a)
    b=int(input("Sisesta palk "))
    palk.append(b)
    return palk,inimesed

def kutsutamine(i:list,p:list):
    """infode kustutamine
    :rtype:str,str:
    """
    try:
        name=input("Nimi: ")
        a=i.index(name)
        t=True
    except:
        print("Nimi puudub")
        t=False
        if t:
            p.pop(a)
            i.pop(a)
            return i,p

def suurem(i:list,p:list):
    """ otsime suurim palk
    :rtype: str,str:
    """
    p1=[]
    for e in p:
        p1.append(int(e))
    suurim=max(p1)
    b=p1.index(suurim)
    kellel=i[b]
    return suurim , kellel

def keskmine(i:list,p:list):
    """Keskmise palka leidmine. Kui ta on loetelus, siis näiame kes saab seda kätte
    :rtype var:
    """
    summa=0
    for palk in p:
        summa+=palk
    kesk=summa/len(p)
    print(kesk)
    vahe=0
    if 0<=p.index(kesk)<len(p)-1:
        kesk=i[p.index(kesk)]
        return kesk
    else:
        kesk="Puudub"
        return kesk


