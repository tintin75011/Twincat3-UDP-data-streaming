# client_udp.py
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# (optionnel mais recommandé) timeout pour éviter de bloquer indéfiniment
sock.settimeout(5)

# Envoi du message

sock.sendto(b"Hello depuis un autre terminal", ("192.168.1.2", 10000))

# Réception de la réponse
try:
    data, addr = sock.recvfrom(1024)  # 1024 = taille max du message
    print(f"Réponse du serveur ({addr}) : {data.decode()}")
except socket.timeout:
    print("Aucune réponse du serveur")

sock.close()
