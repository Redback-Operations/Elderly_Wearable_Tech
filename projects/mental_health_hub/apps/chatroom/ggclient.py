import socket
import threading

HOST = '127.0.0.1'
PORT = 5000

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receive messages
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "GARGI":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred. Connection closed.")
            client.close()
            break

# Send messages
def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode('utf-8'))

# Run both in parallel
threading.Thread(target=receive).start()
threading.Thread(target=write).start()
