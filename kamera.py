import random
import socket
import time

def kamera_calistir():
    while True:
        kalabalik = random.randint(0, 100)
        print(f"[KAMERA] Kalabalık tespit edildi: {kalabalik}")
        try:
            soket = socket.socket()
            soket.connect(("localhost", 8888))  # NVR portu
            soket.send(str(kalabalik).encode())
            soket.close()
        except:
            print("[KAMERA] NVR bağlantısı kurulamadı.")
        time.sleep(5)

kamera_calistir()
