def divisor_count(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

def divisor(num):
    list = []
    for i in range(1, num + 1):
        list.append(divisor_count(i))
    return list
    
print(divisor(12))