import socket
import os

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  #ONLY FOR CLIENT CALLS FROM THE SAME PC. IF CALLED FROM ANOTHER PC WITHIN THE SAME NETWORK CHANGE TO SERVER LOCAL IP
FORMAT = 'utf-8'
DISCONNECT_MESSAGE =  "BYE"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("[CONNECTION]", "CONNECTED TO SERVER", ADDR)
print("[COMMANDS]")

print("\t[COMMAND]", "LIST", "LIST OF ALL DIRECTORIES AND FILES IN CURRENT SERVER DIRECTORY")
print("\t[COMMAND]", "MKDIR 'FILENAME'", "MAKE A NEW SERVER DIRECORY")
print("\t[COMMAND]", "PUT 'FILENAME'", "SEND DIRECTORY TO SERVER")
print("\t[COMMAND]", "GET 'FILENAME'", "RECIEVE DIRECTORY FROM SERVER")
print("\t[COMMAND]", "CD 'DIRECTORY'", "CHANGE CURRENT SERVER DIRECTORY")
print("\t[COMMAND]", "BYE", "DISCONNECT FROM SERVER")


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)   
    
    msg = msg.lower()
    messageList = msg.split()
    if len(messageList) == 2 and messageList[0] == "get":
        done = False
        error = False
        if client.recv(2) != "OK".encode(FORMAT):
            error = True
        fileBytes = b""
        while not done and not error:
            data = client.recv(1)
            fileBytes += data
            if fileBytes[-5:] == b"<END>":
                done = True
                fileBytes = fileBytes[:-5]
        if not error:
            file = open(messageList[1], "wb")
            file.write(fileBytes)
            file.close()
    if len(messageList) == 2 and messageList[0] == "put":
        files = os.listdir()
        error = False
        if messageList[1] not in files or "." not in messageList[1]:                            
            client.send(b"ER")
            error = True 
        if not error:          
            client.send(b"OK")
            file = open(messageList[1], "rb")
            data = file.read()
            client.sendall(data)
            client.send(b"<END>")
            file.close()

    msg_length = int(msg_length) 
    msg_length = client.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        print("[NEW MESSAGE]", client.recv(msg_length).decode(FORMAT))

while True:
    command = input("[ENTER COMMAND] ")    
    send(command)
    if(command == DISCONNECT_MESSAGE or command == DISCONNECT_MESSAGE.lower()):
        print("[DISCONNECTION]", "DISCONNECTED FROM SERVER", ADDR)
        break