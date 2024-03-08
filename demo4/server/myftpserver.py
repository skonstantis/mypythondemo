import socket
import threading
import os

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE =  "BYE"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print("[NEW CONNECTION]", addr, "CONNECTED")
    print("[ACTIVE CONNECTIONS]", threading.active_count() - 1)
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE or msg == DISCONNECT_MESSAGE.lower():
                print("[NEW DISCONNECTION]", addr, "DISCONNECTED")
                break
            msg = msg.lower()
            messageList = msg.split()
            if len(messageList) > 2 or len(messageList) < 1:
                send(conn, "INVALID COMMAND")
                print("[INVALID COMMAND RECEIVED]", addr, msg)
            else:
                if msg == "list":
                    files = os.listdir()
                    filestring = ""
                    for i in files:
                        filestring += '\n' + i
                    send(conn, filestring)
                    print("[VALID COMMAND RECEIVED]", addr, msg)
                elif len(messageList) == 2:
                    if(messageList[0] == "cd"):
                        try:
                            os.chdir(messageList[1]) 
                            send(conn, os.getcwd())
                            print("[VALID COMMAND RECEIVED]", addr, msg)
                        except:
                            send(conn, "SPECIFIED DIRECTORY DOESN'T EXIST")
                            print("[INVALID COMMAND RECEIVED]", addr, msg)
                    elif(messageList[0] == "mkdir"):
                        try:
                            os.mkdir(messageList[1]) 
                            send(conn, "DIRECTORY CREATED")
                            print("[VALID COMMAND RECEIVED]", addr, msg)
                        except:
                            send(conn, "INVALID DIRECTORY NAME")
                            print("[INVALID COMMAND RECEIVED]", addr, msg)
                    elif(messageList[0] == "get"):
                        try:
                            files = os.listdir()
                            if messageList[1] not in files or "." not in messageList[1]:
                                conn.send(b"ER")
                                raise Exception()
                            file = open(messageList[1], "rb")
                            conn.send(b"OK")
                            data = file.read()
                            conn.sendall(data)
                            conn.send(b"<END>")
                            file.close()
                            send(conn, "FILE RECIEVED")
                            print("[VALID COMMAND RECEIVED]", addr, msg)
                        except:
                            send(conn, "FILE DOESN'T EXIST OR IS DIRECTORY")
                            print("[INVALID COMMAND RECEIVED]", addr, msg)
                    elif(messageList[0] == "put"):
                        done = False
                        try:
                            if conn.recv(2) != "OK".encode(FORMAT):
                                raise Exception()
                            fileBytes = b""
                            while not done:
                                data = conn.recv(1)
                                fileBytes += data
                                if fileBytes[-5:] == b"<END>":
                                    done = True
                                    fileBytes = fileBytes[:-5]
                            file = open(messageList[1], "wb")
                            file.write(fileBytes)
                            file.close()
                            send(conn, "FILE RECIEVED")
                        except:
                            send(conn, "NO SUCH FILE")
                    else:
                        send(conn, "INVALID COMMAND")
                        print("[INVALID COMMAND RECEIVED]", addr, msg)
                else:
                    send(conn, "INVALID COMMAND")
                    print("[INVALID COMMAND RECEIVED]", addr, msg)
    conn.close()
    print("[ACTIVE CONNECTIONS]", threading.active_count() - 2) #LAST COMMAND OF THIS THREAD

def start():
    server.listen()
    print("[STARTED] THE SERVER HAS STARTED", SERVER)
    print("[LISTENING] THE SERVER IS LISTENING ON", SERVER)
    print("[ACTIVE CONNECTIONS]", threading.active_count() - 1)
    
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
    
def send(client, msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

print("[STARTING] THE SERVER IS STARTING...")
start()