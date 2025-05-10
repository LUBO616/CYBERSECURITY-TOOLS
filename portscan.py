import socket

ip = input('Enter the ip address to scan: ')

for port in range(1,65535):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    result= sock.connect_ex((ip, port))

    if result == 0:
        print(f'Open Port: {str(port)}')
        sock.close()
    else:
        print(f'Closed port: {str(port)}')