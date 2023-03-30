import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))
print("Server in attesa di messaggi: ")
while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)

    if not data:
        break

    data = data.decode()
    data = json.loads(data)
    primoNumero = data["primoNumero"]
    operazione = data["operazione"]
    secondoNumero = data["secondoNumero"]
    if operazione == "+":
        reply = primoNumero + secondoNumero
    elif operazione == "-":
        reply = primoNumero - secondoNumero
    elif operazione == "*":
        reply = primoNumero * secondoNumero
    elif operazione == "/":
        reply = primoNumero / secondoNumero
    else:
        reply = "errore"
    reply = str(reply)
    sock.sendto(reply.encode(), addr)