for i in range(1,10):
    print("*", end=" ")
    if i%3==0:
        print()

print("Idemo na bilo koji broj ispod!")

n = 10
for i in range(1,n*n+1):
    print("*", end=" ")
    if i%n==0:
        print()

for i in range(0, 10):
    if(i==5):
        break
    print(i)

for i in range(0,10):
    if(i>5 and i<8):
        continue
    print(i)

for i in range(0,20):
    for j in range(0,20):
        print(str(i)+" "+str(j))