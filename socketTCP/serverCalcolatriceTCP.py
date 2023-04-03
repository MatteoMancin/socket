#Server
import socket
import json

IP = "127.0.0.1"
PORTA = 65432
DIM_BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:

  sock_server.bind((IP, PORTA))

  sock_server.listen()

  print(f"Server in ascolto su {IP}:{PORTA}")

  while True:
    sock_service, address_client = sock_server.accept()

    with sock_service as sock_client:

      data = sock_client.recv(DIM_BUFFER).decode()
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
      print(f"Ricevuto messaggio dal client {sock_client}: {data}")
      sock_client.sendall(reply.encode())