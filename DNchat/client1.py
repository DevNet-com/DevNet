import socket
from tkinter import *
from tkinter import ttk

client_name = "clientV"
sock = socket.socket()
ip = 'localhost'
port = 12345
sock.connect((ip, port))
sock.send((str(client_name)).encode("UTF-8"))
def send_String():
    txt = Label() 
    txt.pack()
    txt["text"] = entry.get()
    sock.send((txt["text"]).encode("UTF-8"))
    print(sock.recv(2080).decode("UTF-8"))
    root.mainloop()

root = Tk()     # создаем корневой объект - окно
root.title("Client")     # устанавливаем заголовок окна
root.geometry("650x450")    # устанавливаем размеры окна

entry = ttk.Entry()
entry.place(x=5, y=410, width=550, height=35)
send_str = entry.get()
btn = ttk.Button(text="send", command=send_String)
btn.pack(padx=10, pady=10)
btn.place(x=560, y=410, width=90, height=35)
root.mainloop()