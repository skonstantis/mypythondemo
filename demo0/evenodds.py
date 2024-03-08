def isEven(number):
    if number % 2 == 0:
        return True
    return False

def isPrime(num):
    for i in range(2, num):
        if num % i == 0: 
            return False
    return True

numbers = []
while 1:
    while 1:
        try:
            number = int(input("number/add number, 0/end sequence: "))
            break
        except:
            print("Nan, try again!")
    if number == 0:
        break
    numbers.append(number)
    
evens = 0
odds = 0 
primes = 0
for i in numbers:
    if isPrime(i):
        primes += 1
    if isEven(i):
        evens += 1
    else:
        odds += 1

total = odds + evens
print("Primes: ", primes / total * 100, "%", "Evens: ", evens / total * 100, "%", "Odds: ", odds / total * 100, "%")