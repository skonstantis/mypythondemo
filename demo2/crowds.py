import random

class Node:
    def __init__(self, id):
        self.id = id
        self.is_down = False

while True:
    n = input("Enter node number: ")
    try:
        n = int(n)
        if(n < 3):
            raise Exception("Invalid input")
        break
    except Exception:
        print("Try again!")
        
while True:
    p = input("Enter propability [0, 1]: ")
    try:
        p = float(p)
        if p < 0 or p > 1:
            raise Exception("Invalid input")
        break
    except Exception:
        print("Try again!")

while True:
    sender_id = input("Enter node id of sender [0, n]: ")
    try:
        sender_id = int(sender_id)
        if sender_id < 0 or sender_id > n:
            raise Exception("Invalid input")
        break
    except Exception:
        print("Try again!")

while True:
    receiver_id = input("Enter node id of receiver [0, n]: ")
    try:
        receiver_id = int(receiver_id)
        if receiver_id < 0 or receiver_id > n or receiver_id == sender_id:
            raise Exception("Invalid input")
        break
    except Exception:
        print("Try again!")
        

nodes = []
for i in range(0, n):
    nodes.append(Node(i))

while True:
    while True:
        while True:
            rand = random.randint(0, n)
            if rand != sender_id or rand != receiver_id:     
                print("Sending via node: ", int(rand))
                break
        if random.random() >= 0.1:
            break
        
    if random.random() < p:
        print("message delivered")
        break