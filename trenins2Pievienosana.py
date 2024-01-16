fileName="dzest.txt"
addMe="Man nepatīk tumši rīti!"
try:
    with open(fileName,"a", encoding="UTF-8")as data: # a pievieno jaunas rindiņas, neizdzēšot jau esošās, bet w pievieno jaunas rindiņas un izdzēš jau esošās
        data.write(f"\n{addMe}") #sākumā tas \n, lai jaunā rindiņa būtu jaunajā rindiņā nevis blakus iepriekšējam
        print(f"Rinda ar vārdiem '{addMe}' ir veiksmīgi pievienota!")
except Exception as e:
    print(f"Kļūda: neparedzēta kļūda - {e}")
