suma = 0
for i in range(0,11):
    if(i%2==0):
        suma += i
print(suma)

suma = 0
for i in range(0,11,2):
    suma += i
print(suma)

for i in[3,14,15,6,77]:
    print(i, end=" ")
#Sa ovim end na kraju smo odradili da sve bude u istom redu.

lista = [i for i in range (0,5)]
print(lista)
print(lista[2:4])
#Line 17 - ovo je slice, izabrali smo samo parce iz liste.

