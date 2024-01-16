import math
augumi={'vārds':[],'augums':[]}#sākumā vārdnīcā ir tukši saraksti un vēlāk tukšajiem sarakstiem piešķir vērtības
augumi['vārds']=['Sarmīte','Mirdza','Laine','Leopolds','Frīdis','Amanda','Ingars','Viesturs','Viktorija','Lība','Rigonda','Ilze'] 
augumi['augums']=['172','185','164','184','162','164','165','167','177','184','165','180']
print(f'Labdien, šeit ir jūsu mērījumu dati:')
for key, value in augumi.items(): #programma parāda vārdus un augumus dažādās rindiņās
    print(key, ' : ', value)
papildus=input('Vai Jūs interesē esošo datu kopējā un vidējā vērtība?(j/n)  ') #papildus programma piedāvā apskatīt sākotnējo datu kopējo un vidējo vērtību
if papildus=='j':
    print('Visu datu kopējā vērtība ir 2069 cm')
    print('Visu datu vidējā vērtība ir 172,4 cm')

while True:
        print('\ndarbību opcijas:\nJa vēlaties redzēt visas vārdnīcā esošās vērtības, ievadiet: viss\nJa vēlaties pievienot jaunus datus, ievadiet: jauns\nJa vēlaties izdzēst vārdnīcā esošus datus, ievadiet: dzēst\nJa vēlaties iziet no programmas, ievadiet: iziet')
        izvele=input('\nKo Jūs vēlaties darīt?  ')    
        if izvele=='viss':
             for key, value in augumi.items(): #programma parāda vārdus un augumus dažādās rindiņās
                print('\n',key, ' : ', value)       
        elif izvele=='jauns':
            jauns_vards=input('\nievadiet jaunu vārdu:  ')
            augumi['vārds'].append(jauns_vards) #append pievieno sarakstam jaunus mainīgos
            jauns_augums=int(input('\nKāds ir jaunais augums?(cm)  '))
            augumi['augums'].append(jauns_augums)
            print(f'\nVārds un augums ko Jūs pievienojāt ir {jauns_vards} : {jauns_augums}cm')  
            print('Jaunais saraksts: ') #programma automātiski parāda jauno sarakstu, lai lietotājam nav vienmēr jāizvēlās opcjia:jauns
            for key, value in augumi.items(): #programma parāda vārdus un augumus dažādās rindiņās
                print(key, ' : ', value)  
        elif izvele=='dzēst':
            dzest=input('\nIevadiet vārdu: ')
            index=augumi['vārds'].index(dzest) #metode index paņem mainīgo vārds un atrod atbilstošo augumu
            augumi['vārds'].pop(index) #metode pop izdzēš vērtību no vārdnīcas
            augumi['augums'].pop(index)
            print(f'\nCilvēks, kura augumu Jūs izdzēsāt no saraksta ir: {dzest}')
            print('Jaunais saraksts: ') #programma automātiski parāda jauno sarakstu, lai lietotājam nav vienmēr jāizvēlās opcija:jauns
            for key, value in augumi.items(): #programma parāda vārdus un augumus dažādās rindiņās
                print(key, ' : ', value)  
        elif izvele=='iziet':
            print('Jūs izvēlējāties iziet, atā!')
            exit()
        else:
            print('Jūs ievadījāt nepareizus datus. Mēģiniet vēlreiz!')





        