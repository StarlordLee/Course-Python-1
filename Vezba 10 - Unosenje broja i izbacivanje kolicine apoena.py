amount = int(input("Enter amount: "))
tens = amount // 10
fives = (amount % 10) // 5
twos = (amount % 10 % 5) // 2
ones = (amount % 10 % 5 % 2) // 1
print("Tens: ", tens)
print("Fives: ", fives)
print("Twos: ", twos)
print("Ones: ", ones)

print(10 % 2)