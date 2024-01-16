valstis={'Latvija':1.884,
        'Somija':5.541,
        'Sveice':8.703,
        'Zviedrija':10.42,
        'Francija':67.75,
        'Spanija':47.42,
        'Luksemburga':0.64,
        'Danija':5.857,
        'Kanada':38.25,
        'Belgija':11.59}

iedzivotajiAugosi=sorted(valstis,key=valstis.get) #izveidoju sakārtotos sarakstus jau sākumā, lai vēlāk tos izmantotu
iedzivotajiDilstosi=sorted(valstis,key=valstis.get,reverse=True)
valstisAugosi=sorted(valstis,key=len)
valstisDilstosi=sorted(valstis,key=len,reverse=True)

while True: #while True, lai programma vienmēr noskaidrotu lietotāja vēlmes
    print('\nLabdien! Šeit ir Tavas iespējas: \n1-sakārtot valstis pēc to nosaukumiem augošā secībā \n2-sakārtot valstis pēc to nosaukumiem dilstošā secībā \n3-sakārtot valstis pēc to iedzīvotāju skaita augošā secībā \n4-sakārtot valstis pēc to iedzīvotāju skaita dilstošā secībā \n5-pievienot jaunu valsti un iedzīotaju skaitu \n6-apskatīt visas valstis')
    izvele=input('Ko Tu vēlies darīt? (ievadi skaitli) (ja vēlies iziet no programmas, raksti stop)  ')
    if izvele=='1':
        print('\n\nSakārtotas valstis pēc to nosaukumiem augošā secībā:')
        for vertiba in valstisAugosi: #izmantojot for ciklu valstis un iedzvotju skaits parādās skaistā stabiņā
            print(vertiba,valstis[vertiba])
    elif izvele=='2':
        print('\n\nSakārtotas valstis pēc to nosaukumiem dilstošā secībā:')
        for vertiba in valstisDilstosi:
            print(vertiba,valstis[vertiba])
    elif izvele=='3':
        print('\n\nSakārtotas valstis pēc to iedzīvotāju skaita(miljoni) augošā secībā:')
        for vertiba in iedzivotajiAugosi:
            print(vertiba,valstis[vertiba])
    elif izvele=='4':
        print('\n\nSakārtotas valstis pēc to iedzīvotāju skaita(miljoni) dilstošā secībā:')
        for vertiba in iedzivotajiDilstosi:
            print(vertiba,valstis[vertiba])
    elif izvele=='5':
        jaunaValsts=input('Tu izvēlējies pievienot jaunu valsti, kādu valsti pievienosi?  ')
        if jaunaValsts=='stop':  #ja lietotājs ievada stop ievadot jaunu valsti vai iedzīvotājus, programma apstājas
            print('Jūs izvēlējāties iziet, atā!')
            exit()    
        jauniIedzivotaji=input('Cik iedzīvotāju ir šajā valstī?  ')
        if jauniIedzivotaji=='stop':
            print('Jūs izvēlējāties iziet, atā!')
            exit() 
        valstis.update({jaunaValsts:jauniIedzivotaji})  #funkcija .update() atjauno sarakstu, pievienojot tam jaunu atslēgu un vērtību
        print('\n\nŠeit ir visas valstis kopā ar tikko pievienoto:') #pēc valsts pievienošanas programma parāda atjaunoto sarakstu
        for vertiba in valstis:
            print(vertiba,valstis[vertiba])
    elif izvele=='6':
        print('\n\nVisas valstis:')
        for vertiba in valstis:
            print(vertiba,valstis[vertiba])
    elif izvele=='stop': #ja lietotājs vēlas beigt strādat, programma apstājas
        print('Jūs izvēlējāties iziet, atā!')
        exit()
    else:
        print('Jūs ievadījāt nepareizus datus, lūdzu mēģiniet vēlreiz!') #ja lietotājs ievada datus, kas nav prasīti, var mēģināt vēlreiz
    
    
    

       

