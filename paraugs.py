darzeni = ['zirņi','burkāni','kartupeļi','batātes','gurķi']
print(f'Oriģinālais saraksts: {darzeni}')
darzeni.sort() #atgriež jaunu sarakstu mainot oriģinālo
print(f'Sakārtots ar sort: {darzeni}')



viensSkaistsSaraksts=[5,4,6,7,1,8,3,2]
print(viensSkaistsSaraksts)
print(sorted(viensSkaistsSaraksts)) #atgriež jaunu sarakstu nemainot oriģinālo
print(viensSkaistsSaraksts)



darzeni_kartots=sorted(darzeni,reverse=True)
print(f'Apgriezts {darzeni_kartots}')



saraksts = ['viens','divi','trīs','pieci','septiņi','deviņi']
saraksts_augosi=sorted(saraksts,key=len) #sakārto pēc burtu skaita vārdā augoši
print(saraksts_augosi)
saraksts_dilstosi=sorted(saraksts,key=len,reverse=True)
print(saraksts_dilstosi) 

strs = ['rīts', 'Vakars', 'pusdienas', 'KOMPLEKSIŅŠ','ZEMENES']
strs.sort() # sort metodi nevar likt printā
print(f'Kārtots {strs}')
print(f'Kārtots ar str.lower:{sorted(strs,key=str.lower)}') #ignorē uppercase
print(f'Kārtots ar str.upper:{sorted(strs,key=str.upper)}') #ignorē lowercase
