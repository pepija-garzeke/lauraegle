fails=open("ziema.txt","w",encoding="UTF-8")
# "w" arī izveido neeksistējošu failu no jauna


#ieraksta failā datus
saraksts=["Alūksne\n","Valmiera\n","Balvi\n"]
fails.writelines (saraksts) #ieraksta vairākas rindiņas
fails.write("Man negaršo lakrica.\n")
fails.close()

#pārrakstīt kopētā faila saturu
fails=open("ziema copy.txt","w+",encoding="UTF-8")
fails.write("Man jāsalabo konsole.\n")
fails=open("ziema copy.txt","w+",encoding="UTF-8") #pirms katras darbības ir vēlreiz jāatver fails
print(fails.read()) #parāda faila saturu uz ekrāna
fails.close()

fails=open("ziema copy.txt","a+",encoding="UTF-8") # a+ pievieno jaunu tekstu jau esošajam
fails.write("Es salaboju konsoli.\n")
fails.close()


