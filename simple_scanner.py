import socket 
import threading 
import time 

def scanner(target, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open on {target}")
    except socket.error as err:
        pass
    finally:
        s.close()

target = input("Enter the target IP address or hostname: ")
start_port = int(input("Enter the starting port number: "))
end_port = int(input("Enter the ending port number: ")) 

print(f"Scanning {target} from port {start_port} to {end_port}.....")
time.sleep(1)

threads = []

for port in range (start_port, end_port +1):
    t = threading.Thread(target=scanner, args=(target, port))
    threads.append(t)
    t.start()
for t in threads:
    t.join()

print("Scanning completed ✅")