#!/usr/bin/env python3


input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

sock_service = socket.socket()

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))

protocollo = ["SYN" , "SYN ACK","ACK with Data","ACK for Data"]
step=0
dati = str(step)

while True:

    dati=dati.encode() 

    sock_service.send(dati)

    print("Invio:" + str(step) + " - " + protocollo[step])

    dati = sock_service.recv(2048)

    if not dati:
        print("Nessuna risposta dal server")
        break

    dati = dati.decode()
    step = int(dati)

    if dati == '3':
        print("Ricevuto:" + str(step) + " - " + protocollo[step])
        print("Termino connessione")
        break
    else:
        step = int(dati)
        print("Ricevuto:" + str(step) + " - " + protocollo[step])
        step+=1
        dati= str(step)

sock_service.close()