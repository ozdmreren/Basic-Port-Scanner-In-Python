import socket
import sys
import os
import datetime


os.system("")


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid syntax error")
    print("Syntax swpeeper.py <id>")
    sys.exit()
    
print("-"*50)
print("Scanning is started at: {}".format(datetime.datetime.now()))
print("-"*50)
    
try:
    for port in range(20,70):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((target,port))
        
        print("Scanning port {}".format(port))
        
        s.settimeout(1)
        
        CRED = '\033[91m'
        CEND = '\033[0m'
        
        if result == 0:
            print("\x1b[6;30;42m " +"Port {} is open".format(port) + "\x1b[0m")
        else:
            print(CRED + "Unknown" + CEND)
        
        
except KeyboardInterrupt:
    print("Existing program ...")
    sys.exit()
        