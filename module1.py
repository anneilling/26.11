palgad=[1200,2500,750,395,1200]
inimesed=["A","B","C","D","E"]
def otsing_nimi_jargi(inimesed:list,palgad:list):
    """Tagastame järjend või tekst
    :rtype var: tulemus
    """
    nimi=input("Keda otsime?")
    for inimene in inimesed:
        if inimene==nimi:
            n=inimesed.count(nimi)
            print("Inimene on olemas, selline nimi kohtutakse ",n,"korda")
            b=0
            t=[]
            for i in range(n):
                k=inimesed.index(nimi,b)
                palk=palgad[k]
                b+=k+1
                t.append(nimi+str(palk))
            else:
                t=print("Nimekirjas puudub")
            return t

def lisamine(i, p): #i-inimeste list, p-palgade list
    kogus=int(input("Lisa kasutajad"))
    for j in range(kogus):
        nimi=input("Name: ")
        i.append(nimi)
        palk=int(input("Palk: "))
        p.append(palk)
        return i,p

def kutsutamine(i,p):
    try:
        name=input("Nimi: ")
        a=i.index(name)
        t= rue
    except:
        print("Nimi puudub")
        t=False
        if t:
            p.pop(a)
            i.pop(a)
            return i,p
