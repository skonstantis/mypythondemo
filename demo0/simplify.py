def find_diairetes(number):
    list = []
    for i in range(1, number + 1):
        if number % i == 0:
            list.append(i)
    return list

def find_mcd(diairetes_arithmiti, diairetes_paronomasti):
    mcd = 0
    for i in diairetes_arithmiti:
        for j in diairetes_paronomasti:
            if i == j:
                mcd = i
    if mcd == 0:
        return "Mcd doesn't exist!"
    return mcd

def mcd(arithmitis, paronomastis):
    diairetes_arithmiti = find_diairetes(arithmitis)
    diairetes_paronomasti = find_diairetes(paronomastis)
    return find_mcd(diairetes_arithmiti, diairetes_paronomasti)

while 1:
    try:
        arithmitis = float(input("Give numerator: "))
        break
    except:
        print("Numinator must be a number, try again!")

while 1:
    try:
        paronomastis = float(input("Give denominator: "))
        break
    except:
        print("Denominator must be a number, try again!")
        
mcd = mcd(int(arithmitis), int(paronomastis))
print("Simplified: ", int(arithmitis / mcd), "/", int(paronomastis / mcd))

