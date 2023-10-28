import socket
sock = socket.socket()
ip = "localhost"
port = 12345
sock.bind((ip, port))
sock.listen(10)
def write_log(client_name, addr):
    logs_file = open('logs.txt', 'w+')
    logs_file.write("\nconnect:")
    logs_file.write(client_name)
    logs_file.write(str(addr))
    logs_file.close()
while True:
    conn, addr = sock.accept()
    cname = conn.recv(2028).decode("UTF-8")
    if conn != "":
        print("In chat join", cname)
        while True:
            strt = str(conn.recv(2080).decode("UTF-8"))
            print(strt)
            if strt != "":
                conn.send(strt.encode("UTF-8"))