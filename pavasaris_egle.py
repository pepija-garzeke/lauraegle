import math #math pievienošana ļauj izmantot matemātiskās funkcijas
def faktorials(skaitlis): #funkcija 'faktorials' aprēķina lietotāja ievadītā skaitļa faktoriālu 
    if skaitlis>13: #skaitlis nevar būt lielāks par 13
        print('Ievadītais skaitlis ir pārāk liels')
    elif skaitlis<=0: #skaitlim jābūt pozitīvam
        print('Ievadītais skaitlis nav pozitīvs')
    elif skaitlis==13: #ievadītais skaitlis nevar būt 13, jo 13 nav mazāks par 13
        print('13 nav MAZĀKS par 13')
    else:
        print(f'Faktoriāls: {math.factorial(skaitlis)}') #math.factorial aprēķina skaitļa faktoriālu

def zvaigznites(n): #funkcija 'zvaigznites' uz ekrāna izvada noteiktu skaitu zvaigznīšu
    for i in range(1,n+1,1): #n+1, jo otrais parametrs norāda beigu skaitli, ko vairāk neizvada uz ekrāna
        print('*',end='')
    print('\r') 

def tuksas_rindas(): #funkcia 'tuksas_rindas izvada divas tukšas rindiņas'
    print('\n\n')

def virsraksts(): #funkcija 'virsraksts' izsauc jau iepriekš izveidotās funkcijas
    print('Faktoriāla aprēķināšana')
    zvaigznites(55)
    skaitlis=int(input('Ievadi veselu pozitīvu skaitli, kas mazāks par 13: \n'))
    faktorials(skaitlis)

virsraksts()
while True: #while True atkārto programmas noteiktu daļu
    izvele=input('Vai vēlaties turpināt darbu? (j-jā, citi taustiņi-nē)\n')
    if izvele=='j':
        tuksas_rindas()
        skaitlis=int(input('Ievadi veselu pozitīvu skaitli, kas mazāks par 13: \n'))
        faktorials(skaitlis)
    else: #ja lietotājs izvēlas neturpināt darbu, programma apstājas
        tuksas_rindas()
        print('paldies!')
        exit()

       
