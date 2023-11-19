a = 3
b = 4
c = 5
if a+b > c and b+c > a and a+c > b:
    print("Mozemo napraviti trougao!")
else:
    print("Nemas dovoljno za trougao!")

#Ili, isti kod na drugaciji nacin:

if(a<b):
    if(a<c):
        mini = a
    else:
        mini = c
else:
    if(b<c):
        mini = b
    else: 
        mini = c
print(mini)
print(min(3,4))