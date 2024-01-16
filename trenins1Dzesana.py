fileName="dzest.txt"
deleteMe="Drīz būs Ziemassvētku brīvdienas!"
try:
    with open(fileName,"r", encoding="UTF-8") as data: #r atver failu lasīšanai un saglabā mainīgajā data
        rows=data.readlines()#readlines ielasa visas rindas no faila un saglabā sarakstā
    with open(fileName, "w", encoding="UTF-8")as data:
        for row in rows: #iterē cauri visām saraksta rindām
            if deleteMe not in row:
                data.write(row)#ja neatrod vārdu, tad šo rindu ieraksta atpakaļ failā, ignorējot vai izdzēšot rindas, kuras jāizdzēš
    print(f"Rindas ar vārdu '{deleteMe}' ir veiksmīgi dzēstas no faila '{fileName}'.")
except Exception as e:
    print(f"Kļūda: neparedzēta kļūda - {e}")


