krasas = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for atslega in sorted(krasas):
    print(atslega,krasas[atslega]) #sakārto pēc atslēgas augošā secībā



#izveidot sarakstu ar sorted() funkciju, kas atgriež vērtības augošā secībā. Ar for ciklu iziet cauri key:value pāriem jaunajā vārdnīcā
veikals = {
    'banāni':12,
    'apelsīni':32,
    'arbūzi':21,
    'mandarīni':17,
    'vīnogas':15
    }
#zemāk ir mans avriants, kas izprintē visu stabiņos
kartots=sorted(veikals,key=veikals.get)
for vertiba in kartots:
    print(vertiba,veikals[vertiba])
    
#zemāk ir skolotājaas variants, kas izprintē rindiņā
kartots = sorted(veikals,key=veikals.get)
kartota_vardnica = {}

for key in kartots:
    kartota_vardnica[key] = veikals[key]
print(kartota_vardnica)