#izveidot sarakstu "atzimes" ar testā iegūtajiem punktiem(10 rezultāti no 71 līdz 99)
#ar for ciklu iziet cauri visam sarakstam
#ar elif nosacījumu uz ekrāna parādīt punktus un atzīmi
# >=90 - A, >=80 - B, 70-80 - C, 60-70 - D, <60 - F
#grūtāk - var pielikt datu ievadi. Atkarībā no ievadītā skaitļa, parādīt burtu

rezultats=[72,75,81,83,94,96,97,89,79,80]
rez=[]
for punkti in rezultats:
    if punkti >=90:
        atzime="A"
    elif punkti >=80:
        atzime="B"
    elif punkti >=70:
        atzime="C"
    elif punkti >=60:
        atzime="D"
    else:
        atzime="F"
    rez.append([punkti,atzime])
print(rez)

   