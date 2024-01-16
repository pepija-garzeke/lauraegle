import random
gajieni=["akmens","papīrs","šķēres"]

cilveka_gajiens=input("Ievadi savu gājienu(akmens/šķēres/papīrs):")
datora_gajiens=random.choice(gajieni)


print(f"Cilvēks: {cilveka_gajiens} vs. Dators: {datora_gajiens}")
if cilveka_gajiens==datora_gajiens:
    print("Neizšķirts!")
elif cilveka_gajiens=="akmens" and datora_gajiens=="šķēres":
    print("Uzvara!")
elif cilveka_gajiens=="papīrs" and datora_gajiens=="akmens":
    print("Uzvara!")
elif cilveka_gajiens=="šķēres" and datora_gajiens=="papīrs":
    print("Uzvara!")
else:
    print("Dators uzvar :(")
