f=open('demo.txt','r',encoding='utf-8')  #f ir mainīgais failam(tas var arī nebūt f) un open atver failu
print(f.read())  #izdrukā faila saturu

f=open('demo.txt','r',encoding='utf-8')
print(f.readline())  #nolasa pirmo rindiņu

f=open('demo.txt','r',encoding='utf-8')
print(f.read(10))  #atgriež pirmos 10 simbolus, skaita arī atstarpes

f.close()  #failu vairs nevajag