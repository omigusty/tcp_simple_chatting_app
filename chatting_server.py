import socket


def Inisialisasi():
    host_name = socket.gethostname()
    ip = socket.gethostbyname(host_name)
    port = 12345
    return host_name, ip, port


def Koneksi(konek, klien):
    while True:
        message = input('Pesan : ')
        konek.send(message.encode())
        message = konek.recv(1024)
        message = message.decode()
        print(klien, ':', message)


def Binding(sock, host_name, ip, port):
    sock.bind((host_name, port))
    print("Alamat IP: ", ip)
    name = input('Masukkan Username: ')
    print("menunggu koneksi...")
    sock.listen(1)
    conn, add = sock.accept()
    print("Menerima koneksi dari ", add[0])
    print('Connection Established. Terkoneksi dari: ', add[0])

    client = (conn.recv(1024)).decode()
    print(client + ' sudah terhubung.')

    conn.send(name.encode())
    Koneksi(conn, client)


def RunServer():
    s = socket.socket()

    host_name, ip, port = Inisialisasi()
    Binding(s, host_name, ip, port)


if __name__ == '__main__':
    RunServer()
