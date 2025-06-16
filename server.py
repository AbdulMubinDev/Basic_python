import socket 


ip = '0.0.0.0'
port = 9501


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ip, port))
s.listen(1)

print(f"[+] Server Listening on {ip}:{port}")

client_socket, addr = s.accept()
print(f"[+] Connection from {addr} has been established.")

while True:
    cmd = input("Shell> ")

    if cmd.lower() == 'exit':
        client_socket.send(b'exit')
        print("[-] Closing connection......")
        break
    client_socket.send(cmd.encode())
    response = client_socket.recv(4096).decode()
    print(response)

client_socket.close()
s.close()