a=int(input("a="))
b=int(input("b="))
darb=input("+/-/*/dalisana:")
if darb=="+":
    c=a+b
elif darb=="-":
    c=a-b
elif darb=="*":
    c=a*b
elif darb=="dalisana":
    c=a/b
else:
    c="klūda!"
print("atbilde =",c)

