import socket
import select
import Queue
import sys

server_address = ('25.47.224.249', 10000)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setblocking(0)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

server.bind(server_address)

server.listen(5)

inputs = [server]

msg_q = Queue.Queue()
username = {}

while inputs:
    timeout = 1
    readable, writeable, excable = select.select(inputs, inputs, inputs, timeout)

    if not (readable or writeable or excable):
        continue
    
    for s in readable:
        try:
            if s is server:
                client, client_addr = s.accept()
                client.setblocking(1)
                name = client.recv(20)
                print "Kliens csatlakozott:", name.strip(), client_addr
                username[client] = name.strip()
                for f in writeable:
                    f.sendall("Kliens csatlakozott: "+username[client])
                inputs.append(client)
            elif not sys.stdin.isatty():
                print "Close the system"
                inputs.remove(server)
                for c in inputs:
                    c.close()
                inputs = []
                server.close()
            else:
                data = s.recv(200)
                data = data.strip()
                if data:
                    msg_q.put(data)
                else:
                    
                    print "Kliens kilepett:", username[s]
                    inputs.remove(s)
                    if s in writeable:
                        writeable.remove(s)
                    for f in writeable:
                        f.sendall("Kliens kilepett: "+username[s])
                    s.close()
        except socket.error,m:
            print "Hiba"
            sname=username[s]
            inputs.remove(s)
            s.close()
            if s in writeable:
                writeable.remove(s)
            for f in writeable:
                f.sendall("Kliens kilepett: "+sname)
    
    while not msg_q.empty():
        try:
            next_msg = msg_q.get_nowait()
            print "MSG:", next_msg
        except Queue.Empty:
            break
        else:
            for s in writeable:
                if not next_msg.startswith("["+username[s]+"]"):
                    s.sendall(next_msg)
                    print "SEND", username[s], next_msg
