a = "Dobro"
b = "dobro"
c = "Lose"
d = "lose"
user_input = input("Da li se osecas dobro ili lose danas? ")
if(user_input in (a,b)):
    print("Sjajno! Samo tako nastavi!")
elif(user_input in (c,d)):
    print("Bas mi je zao! Bice bolje!")
else:
    print("Mozes samo uneti 'dobro' ili 'lose!")