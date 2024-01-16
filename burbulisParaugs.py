#Programma ļauj lietotājam ievadīt skaitļus
#tos sakārto ar burbuļkārtošanu
#izaicinājums - tajā pašā programmā uztaisīt funkciju ar quickSort un selectionSort
#papildināt un noformēt pēc saviem ieskatiem

def burbulis(virkne):
    elementi=len(virkne) #kopējais elementu skaits
    for i in range(elementi):
        for j in range(0, elementi-i-1): #elements peld uz augšu, nonākot īstajā vietā
            #izlaiž pēdējo (sakārtoto) elementu
            if virkne[j]>virkne[j+1]: #ja patiess, tad notiek elementu maiņa
                virkne[j], virkne[j+1] = virkne[j+1], virkne[j]

def sakartot():
    elementi=int(input("Ievadiet skaitļu skaitu, kas atradīsies virknē:\n"))
    virkne=[]

    for i in range(elementi):
        skaitlis=int(input(f"Ievadiet {i+1}. skaitli (skaitlim jābūt veselam un pozitīvam):\n"))
        virkne.append(skaitlis)

    burbulis(virkne)
    print("Sakārtotā skaitļu virkne:")
    for skaitlis in virkne:
        print(skaitlis, end=" ")
    print("\n\nPaldies par darbu!\n")

sakartot()