import random
karakterler1="+-/*!&$#?=@"
karakterler2="abcdefghijklnopqrstuvwxyz"
karakterler3="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
karakterler4="1234567890"

choices=[1,2,3,4]
uzunluk=int(input("Uzunluk:  "))
aaaks=int(input("Ardarda gelebilecek aynı tip karakter sayısı:  "))
password=[]

l=random.choice(choices)
for i in range(uzunluk):
    a=random.choice(eval(("karakterler")+str(l)))
    while a in password:
        a=random.choice(eval(("karakterler")+str(l)))

    password.append(a)
    l=random.choice(choices)
    while i>aaaks-1 and password[i-aaaks-1] in eval(("karakterler")+str(l)):
        l=random.choice(choices)




print(" ".join(password))

