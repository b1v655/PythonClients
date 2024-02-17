import socket
import msvcrt
import thread
import sys
import winsound
from input_timeout import readInput

username = raw_input("Enter your name : ")

def prompt(nl):
    if nl:
         sys.stdout.write('\n')
    sys.stdout.write('\r')
    
def printing():
    while True:
        try:
            data = client.recv(200)
            if not data:
                print "Server down"
                sys.exit()
            else:
                winsound.Beep(500,300)
                sys.stdout.write('\r')
                sys.stdout.write(data+"            "'\n')
                sys.stdout.flush()
                prompt(False)
        except SystemExit,m:
            client.close()
            sys.exit()
        except:
            pass
def writing():
    while True:
        try:
            msg = readInput()
            if msg == 'exit':
                sys.exit()
            elif msg != '':
                msg = msg.strip()
                client.sendall("["+username+"]: "+msg)
                prompt(True)
        except SystemExit,m:
            client.close()
            sys.exit()
        except:
            pass

server_address = ('25.47.224.249', 10000)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_address)
client.sendall(username)
client.settimeout(1.0)
prompt(False)

try:
    thread.start_new_thread( printing,() )
    thread.start_new_thread( writing,() )
except:
    print "itt a hiba"
    client.close()
    sys.exit()

while 1:
    pass

