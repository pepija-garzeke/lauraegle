x=int(input("Ievadi kādu veselu, pozitīvu skaitli!\n"))
y=int(input("Ievadi kādu citu veselu, pozitīvu skaitli!\n"))
if x>y:
    A,B=x,y
else:
    A,B=y,x

while True:
    C=A%B
    if C!=0:
        A,B=B,C
        C=A%B
    else:
        print(f"Ievadītie skaitļi {x,y} un lielākais kopīgais dalītājs ir {B}.")
        exit()