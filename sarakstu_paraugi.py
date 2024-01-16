#uzrakstīt programmu, kurā ir divi saraksti. ar + abus apvienot.
manssaraksts=["svece","2","sāls"]#pirmā elementa indekss = 0
otrssaraksts=["karstmaizes","brauniji","kafija"]

lielaissaraksts=manssaraksts+otrssaraksts
print(lielaissaraksts)#vai arī uzreiz print(manssaraksts+otrssaraksts)



#nokopēt saraksta vērtības un ielikt tās jaunā sarakstā.
milzis=["zupa","dzērvene","tastatūra"]
jauns=list(milzis)#šī ir saraksta kopēšana
print(milzis)
print(jauns)



#izveidot sarakstu ar četriem krāsu nosaukumiem. Atrast katra elementa garumu.
krasas=["zils","dzeltens","sarkans","pelēks"]
jaunais_saraksts=[]#tukšs saraksts
for krasa in krasas:
    burti=0#katru reizi, kad palaiž sarakstu, burtu skaits atgriežas uz 0
    for burts in krasa:
        burti+=1#katru reizi pieskaita 1
    pagaidu_saraksts=[krasa,burti]
    jaunais_saraksts.append(pagaidu_saraksts)
print(jaunais_saraksts)
#kā šo kodu var uzrakstīt ar mazāk rindiņām?
#vai ir vienkāršāks veids kā atrast vārda garumu?
krasas=["zils","dzeltens","sarkans","pelēks"]
for krasa in krasas:
    print(len(krasa))
#ir vēl viens variants
colors=["blue","yellow","red","orange"]
jaunssaraksts=[]
for color in colors:
    jaunssaraksts.append([color,len(color)])
print(jaunssaraksts)



