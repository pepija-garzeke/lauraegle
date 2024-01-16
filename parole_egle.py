lietotajs="kaposts" #mainīgais lietotajs apzīmē lietotājvārdu
parole="purvs"
lminejums=input("Ievadi savu lietotājvārdu: ") #mainīgais lminejums ir lietotājvārda minējums
if lminejums=="iziet":
    print("Programmas beigas!")+exit()
pminejums=input("Ievadi savu paroli: ") #pminejums ir paroles minējums
if pminejums=="iziet":
    print("Programmas beigas!")+exit()
meginajumi=1 #šis mainīgais izmantots, lai pārbaudītu cik reizes ir mēģināts
        
while  meginajumi<6:
    if lminejums=="iziet" or pminejums=="iziet":
        print("Programmas beigas!")
        break
    if lminejums==lietotajs and pminejums==parole:
        print("Pieslēgšanās veiksmīga!")
        pirmais=int(input("Ievadi pirmo veselo skaitli: "))
        otrais=int(input("Ievadi otro veselo skaitli: "))
        kopa = range(pirmais, otrais+1) #mainīōgais kopa norāda, ka tur ir iekļauti visi skaitļi no pirmā līdz otrajam
        summa = sum(kopa) #mainīgais summa ir visu iekļauto skaitļu summa
        print(f"Secīgi pieaugošo skaitļu summa no pirmā līdz otrajam ievadītajam skaitlim ir: {summa}") 
        break
    if meginajumi==5:
        print("Atļauts mēģināt pieslēgties 5 reizes!")
        break
    else:
        print("Mēģini vēlreiz!")
        print(f"Atlikušie mēģinājumi: {5-meginajumi}")    
        lminejums=input("Ievadi savu lietotājvārdu: ")
        pminejums=input("Ievadi savu paroli: ")
        meginajumi+=1 #pēc katra mēģinājuma izmantoto mēģinājumu skaits palielinās par 1
    
    



