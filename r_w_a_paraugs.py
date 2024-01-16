#izveidot txt failu ar nosaukumu dati2.txt
failins=open('dati2.txt','a',encoding='utf-8')

#ierakstīt failā sarakstu ar 3 pilsētām
failins=open('dati2.txt','w',encoding='utf-8')
saraksts=['Sigulda\n','Ogre\n','Aizkraukle\n']
failins.writelines(saraksts) #ieraksta vairākas rindiņas
failins.write('\nHello, World!') #ieraksta vienu virkni

#pārrakstīt faila saturu uz 3 valstīm
failins=open('dati2.txt','w',encoding='utf-8')
failins.write('Latvija, \nSomija, \nPakistāna') #writelines neļauj sev pāri pārrakstīt


failins=open('dati2.txt','w',encoding='utf-8')
valstis={
    'Daugavpils':'Latvija',
    'Čitagonga':'Bangladeša',
    'Vladivostoka':'Krievija'
}
for object in valstis:
    failins.write(valstis[object]+'\n')