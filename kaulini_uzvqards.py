import random
print("Metamā kauliņa mešanas sacensdības")
pirmais=str(input("Ievadiet pirmā spēlētāja vārdu!: "))
otrais=str(input("Ievadiet otrā spēlētāja vārdu: "))
metieni = int(input("cik metieni?:"))
reizes = 1
kopsumma1=0
kopsumma2=0

while metieni>0:
    summa1=random.randint(1,6)
    summa2=random.randint(1,6)
    print(f"Ievadiet spēlētāja {pirmais} {reizes}. metiena rezultātu: {summa1}")
    print(f"Ievadiet spēlētāja {otrais} {reizes}. metiena rezultātu: {summa2}")
    reizes+=1
    metieni-=1
    kopsumma1=kopsumma1+summa1
    kopsumma2=kopsumma2+summa2

print(f"spēlētāja {pirmais} punktu summa: {kopsumma1}")
print(f"spēlētāja {otrais} punktu summa: {kopsumma2}")

if kopsumma1>kopsumma2:
    print(f"Uzvar {pirmais}")
elif kopsumma1==kopsumma2:
    print("Neizšķirts")
else:
    print(f"Uzvar {otrais}")
































print("BUILD SUCCESSFUL (total time: 47 seconds)")
    

