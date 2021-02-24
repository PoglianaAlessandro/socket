import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224#numero porta
def connessione_server(address, port):
    sock_service = socket.socket()
    sock_service.connect((address, port))
    print("Connesso a " + str((address, port)))
    invia_comandi(sock_service)
    sock_service.close()
#La funzione riceve la socket connessa al server e la utilizza per richiedere il servizio
def invia_comandi(sock_service):
    print("sono nella funzione invia dati")
    while True:
        #try per evitare gli errori
        try:
            dati = input("Inserisci i dati da inviare (digita ko per uscire): ")
        except EOFError:#condizione che si avvia in caso di errori
            print("\nOkay. Exit")
            break#in caso di errori si ferma il programma
        if not dati:#se non si inviano dati
            print("Non puoi inviare una stringa vuota!")
            continue#il programma non si blocca
        if dati == 'ko':#se viene inserita la scritta "ko" la comunicazione viene interrotta
            print("Chiudo la connessione con il server!")
            break
        #trasforma la string in byte
        dati = dati.encode()#trasformiamo la stringa in byte

        sock_service.send(dati)#ivia dati al server

        dati = sock_service.recv(2048)#riceve i dati

        if not dati:
            print("Server non risponde. Exit")
            break
        
        dati = dati.decode()#decodifica i dati da byte in stringa

        print("Ricevuto dal server:")
        print(dati + '\n')

if __name__ == '__main__':
    connessione_server(SERVER_ADDRESS, SERVER_PORT)