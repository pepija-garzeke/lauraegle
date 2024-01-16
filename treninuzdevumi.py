print("Oriģinālais saraksts")
telefoni={"zimols":"apple",
    "modelis":"14",
    "gads":"2021"}
print(telefoni)
print("Jaunais saraksts")
telefoni.update({"gads":"2022"})
print(telefoni)

print("-----------")

skolas={"Nosaukums":"Siguldas Valsts ģimnāzija",
        "Novads":"Sigulda",
        "skolēni":"569",
        "gads":"2019"}
print(skolas)
skolas.clear()
print(skolas)

print("-----------")

augli={"a":"Mango",
       "b":"Banans",
       "C":"bumbiers",
       "d":"abols",
       "e":"tomats"}
print(augli)
augli.pop("a")
augli.pop("d")
print(augli)

print("-----------")

skaitli={"g":100,
         "h":200,
         "j":300,
         "l":400}
if 200 in skaitli.values():
    print("Skaitlis 200 ir vārdnīcā!")