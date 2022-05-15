import socket


def Inisialisasi():
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    port = 12345
    return server_host, ip, port


def Koneksi(soc, nama):
    while True:
        message = (soc.recv(1024)).decode()
        print(nama, ":", message)
        message = input("pesan : ")
        soc.send(message.encode())


def Binding(sock, host, ip, port):
    print('Alamat IP Client: ', ip)
    host = input('Masukkan alamat IP Server:')
    name = input('Masukkan username: ')

    sock.connect((host, port))

    sock.send(name.encode())
    server_name = sock.recv(1024)
    server_name = server_name.decode()

    print(server_name, ' Telah bergabung...')
    Koneksi(sock, server_name)


def RunClient():
    s = socket.socket()

    server_host, ip, port = Inisialisasi()
    Binding(s, server_host, ip, port)


if __name__ == '__main__':
    RunClient()
