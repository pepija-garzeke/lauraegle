kontakti={'vards':[],'numurs':[]} #sākumā vārdnīcā ir tukši saraksti un vēlāk tukšajiem sarakstiem piešķir vērtības
kontakti['vards']=['Sarmīte','Mirdza','Laine','Leopolds','Frīdis'] 
kontakti['numurs']=['254388902','99872401','2348197562','349764768','40672457']
while True: #kods visu atkārtos, kamēr neizpildīsies funkcija exit
    print('\ndarbību opcijas:\n1-drukāt kontaktus uz ekrāna \n2-pievienot kontaktus \n3-izdzēst kontaktus \n4-iziet\n \n')
    izvele=input('Ko Jūs vēlaties darīt? (1/2/3/4) ')


    if izvele=='1':
        print(f'Jūs izvēlējāties drukāt kontaktus uz ekrāna:\n{kontakti}')

    elif izvele=='2':
        print('Jūs izvēlējāties pievienot jaunus kontaktus:')
        jauns_vards=input('Kāds vārds būs Jūsu jaunajam kontaktam? ')
        kontakti['vards'].append(jauns_vards) #append pievieno sarakstam jaunus mainīgos
        jauns_numurs=input('Kāds ir Jūsu jaunā kontakta numurs? ')
        kontakti['numurs'].append(jauns_numurs)
        print(f'Jūsu jaunais saraksts: {kontakti}')
    
    elif izvele=='3':
        print('Jūs izvēlējāties izdzēst kontaktus:')
        dzest=input('Ievadiet vārdu: ')
        index=kontakti['vards'].index(dzest) #metode index paņem mainīgo name un atrod atbilstošo
        kontakti['vards'].pop(index)
        kontakti['numurs'].pop(index)
        print(f'Jūsu jaunais saraksts: {kontakti}')

    elif izvele=='4':
        print('Jūs izvēlējāties iziet, atā!')
        exit()



