skaitli= [100,200,45,2,0.5,77,100,55,400]
zoo = ['zebra','lūsis','lama','kamielis','briedis']

print(f'Nesakārtots saraksts: {skaitli}')
print(f'Sakārtots saraksts: {sorted(skaitli)}')
print('------------------------------------------------------------')
print(f'Nesakārtots saraksts: {zoo}')
print(f'Sakārtots saraksts: {sorted(zoo)}')
print('------------------------------------------------------------')
print(f'Dilstoša secībā: {sorted(skaitli,reverse=True)}')
print(f'Dilstošā secībā: {sorted(zoo,reverse=True)}')



#dārzeņi, atslēga ir dārzenis un vērtība ir dārzeņu skaits, kas šodien apēsts
elementi=0
while elementi<7:
    darzeni={'darzenis':[],'skaits':[]}
    jauns_darzenis=input('\n\n\nKādu dārzeni Tu šodien apēdi?  ')
    darzeni['darzenis'].append(jauns_darzenis)
    jauns_skaits=float(input('Cik tādus dārzeņus Tu šodien apēdi?  '))
    darzeni['skaits'].append(jauns_skaits)
    elementi=elementi+1
    
darzeni_kartots=sorted(darzeni)
print(darzeni_kartots)


