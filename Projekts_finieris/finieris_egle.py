import math
print("Labdien, sāksim darbu!")
skaits=int(input("Cik podesti jāizgatavo?  "))
koks=input("Kāda koka saplāksnis vajadzīgs? ")
cena=float(input("Cik maksā 1 kvadrātmetrs saplākšņa? (eiro)  "))
garums=float(input("Kāds būs podesta garums? (lūdzu, atbildi ievadi metros)  "))
platums=float(input("Kāds būs podesta platums? (lūdzu, atbildi ievadi metros)  "))
augstums=float(input("Kāds būs podesta augstums? (lūdzu, atbildi ievadi metros)  "))
listesgarums=round((platums+garums+augstums)*4,2)#līstes garums ir atkarīgs no podesta izmēra
sturis=8#katram podestam vajag 8 stūra savienojumus
finieris=round(2*(garums*platums)+2*(platums*augstums)+2*(garums*augstums),2)#finiera daudzums kvadrātmetros

#ar šo funkciju programma konsolē parādīs nepieciešamo materiālu skaitu
def materialuAprekins(tips,skaits):
    return tips*skaits

print("Nepieciešamie materiāli:\n",materialuAprekins(finieris,skaits)," kvadrātmetri finiera\n",materialuAprekins(listesgarums,skaits)," metri līstes\n",materialuAprekins(sturis,skaits)," stūra savienojumi")

#ar šo funkciju programma aprēķina izmaksas norādītajam materiālu tipam
def izmaksas(tips,cena,skaits):
    return round(tips*cena*skaits,2)

kopejasizmaksas=round((2*(garums*platums)+2*(platums*augstums)+2*(garums*augstums))*cena+(listesgarums/2.6*3.8)+(sturis*skaits*0.3),2)
    
print(f"Jūs izgatavosiet podestu no: {koks}")
print("šeit ir jūsu izmaksas: \nFinieris: ",izmaksas(finieris,cena,skaits)," eiro\nLīstes: ",round(izmaksas(listesgarums/2.6,3.8,skaits)/2.62,2), " eiro\nStūra savienojumu:",izmaksas(sturis,0.3,skaits)," eiro")
print("Kopējās izmaksas: ",kopejasizmaksas," eiro")
pvn=input("Vai tu vēlies redzēt izmaksas ar pvn? (j/n)  ")
if pvn=="j":
    print("Izmaksas ar pvn: ",round(kopejasizmaksas*1.21,2), " eiro")

print("Paldies par darbu, atā :)")

    