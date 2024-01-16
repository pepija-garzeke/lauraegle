#izveidot vārdnīcu, kas satur sarakstu
valstis = {'Somija':['Helsinki','Rovaniemi','Tampere','Kemijarvi','Jyvaskyle'],
    'Norvēģija':['Oslo','Bergena','Arendāla','Trumse','Molde'],
    'Dānija':['Kopenhāgena','Odense','Esbjerga','Aarhus','Ronne']}
#pirmais variants ar for ciklu
for atslega, vertiba in valstis.items():
    for i in vertiba:
        print('{}:{}'.format(atslega,i)) #pirmaa figūriekava ir atslēga un otrā figūriekava ir vērtība
    print('-----------------')
print("-----------------")
#otrs variants ar for ciklu vienai atslēgu grupai
for i in valstis["Dānija"]:
    print(i)

#iegūt pirmās 3 pilsētas no Somijas
print(valstis["Somija"][:3])

#iegūt pēdējās divas pilsētas no Norvēģijas
print(valstis["Norvēģija"][-2:])

#iegūt visas pilsētas no Somijas, izņemot 3 pēdējās
print(valstis["Somija"][:-3])

#iegūt otro līdz piekto pilsētu no Dānijas
print(valstis["Dānija"][1:5])
