termins=input("Vai pie tevis atrodas laikā nenodots izdevums? (j/n)") 
pieprasitie=input("Vai publikācija ir pieprasīto izdevumu sarakstā? (j/n")
gramata=input("Vai tu vēlies grāmatu? (j/n")
personals=input("Vai tu esi skolas personāls?") #no sākuma ir visi jautājumi, lai vēlāk varētu strādāt ar atbildēm
if termins=="j":
    print("Tu neesi cienīgs ņemt jaunus materiālus") #ja lietotājs nav nodevis kādu publikāciju, tad viņam nav atļauts izņemt jaunas publikācijas
elif pieprasitie=="j":
    print("Publikācija ir izsniegta uz 2 dienām") #ja lietotājs ir nodevis visas grāmatas, tad var domāt par jaunām grāmatām
elif gramata=="n":
    print("Žurnāls ir izsniegts uz 7 dienām") #ja tu nevēlies grāmatu, tev izsniegs žurnālu
elif personals=="j":
    print("Grāmata ir izsniegta uz 28 dienām")
else:
    print("Grāmata ir izsniegta uz 14 dienām") #pie else nav nosacījuma, tikai darbība

