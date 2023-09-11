print('--------------------------------------------------------------')
print('1. Nomizotus, gabaliņos sagrieztus ābolus pārkaisa ar 2 kg cukura un atstāj uz nakti ievilkties. \n2. No rīta liek vārīties. Brīdī, kad sāk vārīties, vāra vēl 10 minūtes. Karstu pilda burciņās')
print('--------------------------------------------------------------')
print('Lai pagatavotu šo ābolu ievārījumu tev nepieciešami āboli un cukurs attiecībā 3:1')
aboli=int(input('Cik kg ar āboliem tev ir?(datus ievadi veselos kg)\n'))
e_kg=1.24 #šāds mainīgais bija dots specifikācijā un tas norāda cukura cenu kg 
cukurs=round(aboli/3,2) #Receptē ābolu:cukura attiecība ir 3:1 tāpēc cukura daudzums ir 3 reizes mazāks
print('--------------------------------------------------------------')
print(f'Tev būs nepieciešams {cukurs} kg cukura')
ievarijums_litros=round(aboli+cukurs,2)
cukura_cena=round(cukurs*e_kg,2)
print(f'Izmaksas par cukuru būs {cukura_cena} EUR')
print(f'Ar ievadītajiem sastāvdaļu daudzumiem, izdevās uzvārīt {ievarijums_litros} litrus ievārījuma.')
print('--------------------------------------------------------------')