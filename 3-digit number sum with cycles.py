# Berechnung der Quersumme einer dreistelligen Zahl mit Validierung
# Calculating the sum of the digits of a three-digit number with input validation

num = int(input("Bitte geben Sie eine dreistellige Zahl ein: "))

while not (100 < num <= 999):
    print("Fehler! Bitte Geben Sie eine genau dreistellige Zahl ein: ")
    num = int(input()) 

c = num%10
a = num//100 
b = (num//10)%10

total = a + b + c

print("Die Quersumme Ihrer Zahl beträgt: ", total)
more = input("Möchten Sie fortfahren? Ja/Nein: ").lower()

if more == 'ja':
    n = int(input("Bitte geben Sie an, wie viele weitere Zahlen Sie berechnen möchten: " ))
    total = 0
    for i in range(n+1):
        num = int(input("Bitte geben Sie eine dreistellige Zahl ein: "))

        while not (100 < num <= 999):
            print("Fehler! Bitte Geben Sie eine genau dreistellige Zahl ein: ")
            num = int(input()) 

        c = num % 10
        a = num // 100 
        b = (num // 10) % 10
        total = a + b + c
        print("Die Quersumme dieser Zahl beträgt: ", total)
    print("Tschüss!")
else: 
    print("Tschüss!")