def error(): #funkcija, lai nav katru reizi jāraksta print
    print("Ievadi pareizus datus")+exit()
def izmaksas(x): #funkcija, kas izmaksas centos pārvēršs uz eiro
    summa=x/100
    return summa
muzika=input("Vai tu gribēsi klausīties mūziku? (j/n):")
if muzika=="n":
    print("Šoferis tevi nevedīs, jo viņam ļoti patīk mūzika")+exit()#programma apstājās, jo šoferītis ved tikai cilvēkus, kam patīk klausīties mūziku

pasazieri=int(input("Ievadi pasažieru skaitu:"))
if pasazieri>4:
    print("Pārāk daudz cilvēku")+exit()#ja pasažieru skaits ir lielāks par 4, programma apstājās, jo taksi nav vietas vairāk cilvēkiem

pulkstenis=int(input("Cik pulkstens? (laiku ievadi veselās stundās, piemēram, 15:14 = 15): "))
if pulkstenis<0 or pulkstenis>23:
    error()
cels=int(input("Cik tālu tu brauksi? (km):"))
if cels<0:
    error()
elif pulkstenis>=6 and pulkstenis<22:
    brauciens=cels*57#lai nav grūtības ar float un int, tad sākumā programma visu sarēķina 57 centiem nevis 0,57 eiro
else:
    brauciens=cels*67#šeit ir tas pats, programma aprēķina ar 67 centiem
    
stavvieta=input("Vai taksis ir stāvvietā? (j/n):")
if stavvieta=="n":
    stavvietas_cena=220#arī šeit izmantoju 220 centus nevis 2,20 eiro
else:
    stavvietas_cena=0

bremze=input("Vai tu pa ceļam kaut kur vēlies apstāties? (j/n):")#bremze, jo šoferim ir lieki jābremzē
if bremze=="n":
    bremzes_cena=0
else:
    gaidisana=int(input("Cik ilgi tevi būs jāgaida? (cik minūtes)"))
    bremzes_cena=13*int(gaidisana)#un atkal programma aprēkinus veic ar 13 centiem


kopejas_izmaksas=brauciens+stavvietas_cena+bremzes_cena
print("")
print("serviss: 'Lauras taksis'")#izmantoju funkcijas, lai nav katru reizi jāraksta mainigais/100
print("Cena par tavu braucienu =",izmaksas(brauciens),"€")
print("Cena par takša izsaukšanu =",izmaksas(stavvietas_cena),"€")
print("Cena par gaidīšanu =",izmaksas(bremzes_cena),"€")
print("")
print("Kopējās izmaksas =",izmaksas(kopejas_izmaksas),"€")
print("Paldies, ka izvēlējāties servisu 'Lauras taksis'")

