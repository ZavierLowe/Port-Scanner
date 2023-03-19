import  socket 
from colorama import init,Fore


init()
GREEN = Fore.GREEN
RESET = Fore.RESET
RED =  Fore.RED

def is_port_open (host,port) :
    s = socket.socket()
    try:
         s.connect((host,port))
         s.settimeout(0.2)
    except:
         #Cannont Connect, port is closed
         #return false
         return False
         raise
    else:
         return True


host =  input("Enter the host ")
port_range_1 = input("Enter first port range ")
port_range_2 = input("Enter second port range ")

port_range_1 = int(port_range_1)
port_range_2 = int(port_range_2)


for port in range (port_range_1,port_range_2):
     if is_port_open(host,port):
          print(f"{GREEN}[ + ]{host} : {port} is open {RESET}") 
     else:
          print(f"{RED}[ ! ]{host} : {port} is closed {RESET}", end="\r")