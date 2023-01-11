import socket
import termcolor

open = 0
close = 0
total = 0

def scan(target, ports):
    i = 0
    global total
    total = ports
    for port in range(1,ports+1):
        if i==0:
            global open, close
            open = 0
            close = 0
            print(termcolor.colored("\nScanning the Ip address " + str(target),"green"))
            i = i + 1
        portscan(target,port)

def portscan(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Open port "+str(port))
        openport()
        sock.close()
    except:
        closeport()

def openport():
    global open
    open = open + 1
    check()

def closeport():
    global close
    close = close + 1
    check()

def check():
    global open, close, total
    if(open+close==total):
        if(open == 0):
            print(termcolor.colored("!there are no open ports for the given device","red"))
        print(termcolor.colored("\nTotal Ports: "+str(total),"magenta")+termcolor.colored("\t\tClosed Ports: "+str(close),"red")+termcolor.colored("\t\tOpen Ports: "+str(open),"green"))


targets = input(termcolor.colored("Enter target(s) to scan","yellow")+termcolor.colored(" (split them by ,)","magenta")+termcolor.colored(": ","yellow"))
ports = int(input(termcolor.colored("Enter no of ports upto which you want to scan : ","yellow")))

if "," in targets:
    for ip_addr in targets.split(","):
        scan(ip_addr.strip(' '),ports)
else:
    scan(targets, ports)
