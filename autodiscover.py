import socket
import time

def start_broadcasting():
    port = 55555
    message = b"CAPYPI_OS_DISCOVERY"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print("🌐 [自動廣播 IP 服務] 已啟動...")
    
    while True:
        try:
            s.sendto(message, ('<broadcast>', port))
            time.sleep(3)
        except Exception as e:
            print(f"廣播例外錯誤: {e}")
            break

if __name__ == "__main__":
    start_broadcasting()