def burbulis(virkne):
    elementi=len(virkne) #kopējais elementu skaits
    for i in range(elementi):
        for j in range(0, elementi-i-1): #elements peld uz augšu, nonākot īstajā vietā  
            #izlaiž pēdējo (sakārtoto) elementu
            if virkne[j]<virkne[j+1]: #ja patiess, tad notiek elementu maiņa
                    virkne[j], virkne[j+1] = virkne[j+1], virkne[j]

def sakartot():
    elementi=int(input("Ievadiet studentu saraksta izmēru (Cik studentu būs sarakstā?):\n"))
    virkne=[]

    for i in range(elementi):
        vards=input(f"Ievadiet {i+1}. studenta vārdu:\n")
        skaitlis=int(input(f"Ievadiet {i+1}. studenta rezultātu (vesels skaitlis 0-100):\n"))
        virkne.append((skaitlis, vards))
    
    burbulis(virkne)
    print("Skolēnu rezultāti dilstošā secībā:")
    for skaitlis in virkne:
        print(skaitlis, end="\n")
    print("\n\nPaldies par darbu!\n")

sakartot()
#bubbleSort strada



