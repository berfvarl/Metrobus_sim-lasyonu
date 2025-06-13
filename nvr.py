import socket

def nvr_baslat():
    s = socket.socket()
    s.bind(("localhost", 8888))
    s.listen(5)
    print("[NVR] Dinlemede...")

    while True:
        client, addr = s.accept()
        data = client.recv(1024).decode()
        print(f"[NVR] Kameradan gelen: {data}")

        try:
            merkez_soket = socket.socket()
            merkez_soket.connect(("localhost", 7777))  # Merkez portu
            merkez_soket.send(data.encode())
            merkez_soket.close()
        except:
            print("[NVR] Merkeze bağlantı hatası.")

        client.close()

nvr_baslat()
