import socket
import json

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024
NUM_MESSAGES = 5

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

primoNumero = float(input("Inserisci primo numero: "))
operazione = input("Inserisci l'operazione (+,-,*,/, %)")
secondoNumero = float(input("Inserisci secondo numero: "))

messaggio = {
    "primoNumero": primoNumero,
    "operazione": operazione,
    "secondoNumero": secondoNumero
}

messaggio = json.dumps(messaggio)
sock.sendto(messaggio.encode("UTF-8"), (SERVER_IP, SERVER_PORT))
data, addr = sock.recvfrom(1024)
print("Risultato: ", data.decode())


sock.close()