import socket
import time


class Istasyon:
    def __init__(self, ad):
        self.ad = ad
        self.gelen_metrobüs = 0

    def metrobüs_kabul_et(self):
        self.gelen_metrobüs += 1
        print(f"[{self.ad}] Yeni bir metrobüs geldi. Toplam: {self.gelen_metrobüs}.")


def istasyon_baslat():
    istasyon = Istasyon("Kadıköy")
    s = socket.socket()
    s.bind(("localhost", 6666))  # Merkezden veri almak için portu açıyoruz
    s.listen(5)
    print(f"[{istasyon.ad}] İstasyon dinlemede...")

    while True:
        client, addr = s.accept()
        data = client.recv(1024).decode()
        print(f"[{istasyon.ad}] Gelen emir: {data}")

        if data == "metrobüs gönderiliyor":
            istasyon.metrobüs_kabul_et()
        else:
            print(f"[{istasyon.ad}] Bilinmeyen emir: {data}")

        client.close()


# İstasyonu başlat
istasyon_baslat()
