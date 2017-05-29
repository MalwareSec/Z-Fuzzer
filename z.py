#!/usr/bin/Python2.7.12
# 0x5A = 'Z'
import sys
import socket
from time import sleep

#Defining Global Variables
ftp = 21
ssh = 22
tln = 23
smtp = 25

buff = '0x5A' * 50

def fuzzer_loop(target, port):
    while True:
        try:
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            s.connect((target, port))
            s.recv(1024)

            print "Sending Buffer with length: "+str(len(buff))
            s.send(buff)
            s.close()
            #set sleep time
            sleep(1)
            buff = buff + '0x5A' * 50
        except:
            print "[*] Crashed with buffer length: " +str(len(buff)-50)
            sys.exit()

def usage():
    print 'Welcome to the Z Fuzzer tool'
    print ''
    print 'Usage: python z.py -t [target IP] -p [target port]'
    print ''
    print '-f --ftp for port 21' #File transfer protocol
    print '-s --ssh for port 22' #Secure Shell
    print '-l --tln for port 23' #telnet
    print '-m --smtp for port 25' #Simple Mail Transfer Protocol
    print '-h --help for help menu'
    print ''
    print 'Examples:'
    print ''
    print 'python z.py -t 192.168.1.2 -p 4444'
    print 'python z.py -t 192.168.1.2 -f'
    print 'python z.py -t 192.168.1.2 -m'
    print ''
    sys.exit(0)


def main():
    global ftp
    global ssh
    global tln
    global smtp

    if not len(sys.argv[1:]):
        usage()

    #read the commandline options
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:t:p:f:s:l:m', ['help', 'target', 'port', 'ftp', 'ssh', 'tln', 'smtp'])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o,a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-f', '--ftp'):
            port = ftp
        elif o in ('-s', '--ssh'):
            port = ssh
        elif o in ('-l', '--telnet'):
            port = tln
        elif o in ('-m', '--smtp'):
            port = smtp
        elif o in ('-t', '--target'):
            target = a
        elif o in ('-p', '--port'):
            port = int(a)
        else:
            assert False, 'Unhandled Option'

    if len(target) and port > 0:
        fuzzer_loop(target, port)

main()
