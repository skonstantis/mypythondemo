flag = True
while(flag):
    try:
        feet = int(input("Number of feet: ")) 
        heads = int(input("Number of heads: "))
        flag = False
    except:
        print("Wrong input! Try again!")

result = [i for i in range(0, heads + 1) if(((heads - i) * 4 + i * 2) == feet or ((heads - i) * 2 + i * 4) == feet)]
if(len(result) == 0):
    print("No possible combination")
else:
    if result[0] * 4 + result[1] * 2 == feet:
            print("Rabbits:", result[0])
            print("Chickens:", result[1])
    else:
        print("Chickens:", result[0])
        print("Rabbits:", result[1])