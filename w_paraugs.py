fails=open('dati.txt','a',encoding='utf-8')  #izveidos failu
fails.write('Ingvera sula garšo pēc suši!!\n')
#katru reizi, kad palaiž programmu, teksts tiek pievienots failam atkārtoti

fails=open('dati.txt','r',encoding='utf-8')
print(fails.read())

fails=open('dati.txt','w',encoding='utf-8')
#w pārraksta datus
fails.write('Mācos rakstīt failā\n')

fails=open('dati.txt','a',encoding='utf-8')
#a pievieno jaunu tekstu, neizdzēšot veco
fails.write('Man negaršo cola\n')


fails.close()