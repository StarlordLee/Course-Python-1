Broj = int(input("Unesi broj "))
"""Ovo int ispred je da odmah konvertuje taj broj u integer, a 
ne string, da ga ne tretira kao karakter, vec broj!"""
if(Broj%2==0):
    print("Broj " + str(Broj) + " je paran")
else:
    print("Broj " + str(Broj) + " je neparan")
    print("Broj %d je neparan" % Broj)
    print(f"Broj {Broj} je neparan")
#Idemo dalje.
print("___________________")
x = 2
x = x + 10
x += 10
print(x)
print (12 & 10)
# De ovo gore iz powerpointa ponovi.
print("___________________")
a = 12
a = a >> 2 #Isto sto i a>>= 2
print("___________________")
print(a>>2)
print(a)
print("___________________")

