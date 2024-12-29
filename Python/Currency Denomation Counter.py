amount = int(input("Enter amount: "))

notes_100 = amount // 100
amount %= 100

notes_50 = amount // 50
amount %= 50

notes_20 = amount // 20
amount %= 20

notes_10 = amount // 10
amount %= 10

print("100s:", notes_100)
print("50s:", notes_50)
print("20s:", notes_20)
print("10s:", notes_10)
print("Remaining:", amount)
