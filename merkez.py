import socket

def merkez_baslat():
    s = socket.socket()
    s.bind(("localhost", 7777))
    s.listen(5)
    print("[MERKEZ] Dinlemede...")

    while True:
        client, addr = s.accept()
        data = client.recv(1024).decode()
        print(f"[MERKEZ] NVR'dan veri alındı: {data}")
        try:
            yogunluk = int(data)
            if yogunluk > 60:
                print(">> 🚍 Kalabalık yoğun, metrobüs gönderiliyor.")
            else:
                print(">> ✅ Durum normal.")
        except:
            print("[MERKEZ] Veri çözümlemede hata.")
        client.close()

merkez_baslat()
istasyon_soket = socket.socket()
istasyon_soket.connect(("localhost", 6666))  # İstasyon portu
istasyon_soket.send("metrobüs gönderiliyor")
istasyon_soket.close()
