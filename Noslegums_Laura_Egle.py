from datetime import datetime
def beigas(mainigais): #ja lietotājs izvēlas pārtraukt programmas darbību, programma beidz strādāt un atvadās
    if mainigais=="stop" or mainigais=="iziet" or mainigais=="exit":
        print("---------\nTu izvēlējies beigt programmas darbību! Ceru, ka programma bija noderīga. Atā!")
        exit()

def pareizs_vards(pareizaisVards): #funkcija izdzēš visas ievadītās atstarpes un atgriež vārdu ar lielo burtu
    jaunaisVards = pareizaisVards.replace(" ", "")
    return jaunaisVards.capitalize()

def iegut_datus(): #funkcija iegūst datus no lietotāja, visi dati ir globāli, lai tos varētu izmantot ārpus funkcijas
    global eksperimenta_nosaukums
    global laiks
    global vards
    global vieta
    eksperimenta_nosaukums=input("Lūdzu, ievadi veiktā eksperimenta nosaukumu!\n")
    beigas(eksperimenta_nosaukums) #pēc katra ievadītā vārda, tiek izsaukta funkcija beigas(), lai pārbaudītu, vai ievadītais vārds nav stop, iziet vai exit
    laiks=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    vards=input("\nLūdzu, ievadi savu vārdu!\n")
    beigas(vards)
    vieta=input("\nLūdzu, norādi vietu, kur tika veikts eksperiments (piemēram, pilsētu kurā veici eksperimentu)!\n")
    beigas(vieta)
    print("---------")

def saglabat_datus(): #funkcija izveido jaunu teksta failu un, nepārrakstot iepriekšejos datus, ieraksta failā jaunos datus
    datuNosaukums="eksperimenta_dati.txt"
    try:
        with open(datuNosaukums,"a",encoding="UTF-8")as dati:
            dati.write(f"{pareizs_vards(eksperimenta_nosaukums)} {laiks} {pareizs_vards(vards)} {pareizs_vards(vieta)}\n") #ierakstot jaunos datus, tiek izsaukta funkcija pareizs_vards(), lai teksta failā ierakstītu vārdus bez atstarpēm un ar lielajiem burtiem
            print(f"Jūsu jaunā eksperimenta dati ir veiksmīgi pievienoti teksta failam '{datuNosaukums}'\n")
            print("Ja vēlies pievienot vēl datus, turpini atbildēt uz jautājumiem! Ja jebkurā brīdī vēlies iziet no programmas, atbildes vietā ieraksti: stop, iziet vai exit.\n")
    except Exception as e:
        print(f"Kļūda: neparedzēta kļūda - {e}")
def galvena():
    print("\nLabdien! Esi sveicināts šajā programmā! Šeit Tev būs iespēja pierakstīt dažādu eksperimentu datus (laiku, vārdu, vietu, datumu)!\nJa jebkurā brīdī vēlies iziet no programmas, atbildes vietā ieraksti: stop, iziet vai exit.\n---------")
    while True: #while True, lai programma turpinātos, līdz lietotājs izvēlas iziet
        iegut_datus()
        saglabat_datus()
galvena()