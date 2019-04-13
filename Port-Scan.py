#!/usr/bin/python2
#!/usr/env python2

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
    Do not Paste and Copy it.
    Changing the Variabel and the Author Name didn't make You be a Programmer '''
# Note: ASCII Art is copyrighted to kevin kreamer - kreamer@centraltx.net
#       visit: https://www.asciiart.eu/weapons/knives

import socket,platform,os,argparse
if platform.system() == 'Windows':
	os.system('cls')
else:
	os.system('clear')
def jeda():
	raw_input("Press [ENTER] ")

parser = argparse.ArgumentParser()
parser.add_argument("--target",dest='target',help="Specify Target HOST/IP",type=str)
parser.add_argument("--range",dest='range',help="Port Scanning Range",type=int,default=1024)
parser.add_argument("--timeout",dest='timeout',help="Scanning Timeout",type=float,default=0.5)
options = parser.parse_args()

if options.target == '' or options.target == 'None' or options.target == None:
	print ""
	print "[!] Error: Target unidentificated! Please check again"
	print "           Your command! learn on 'EXAMPLE.txt'"
	print "           or You can try run 'Port-Scan.py --help' command"
	print ""
	jeda()
	exit()

try:
	print ""
	ip_address = socket.gethostbyname(options.target)
except:
	print "[!] Error: Can't find IP Address from {0}".format(options.target)
	print "           check Your connection or check the Host Address!"
	print ""
	jeda()
	exit()

print '''
       .---.
       |---|    Port-Scan.py ---> Port Scanning Tool (Python2)
       |---|    Coded by M-XacT-666 (copyright)
       |---|
   .---^ - ^---.
   :___________:
      |  |//|
      |  |//| 
      |  |//|  Target           : {0}
      |  |//|  IP Address       : {1}
      |  |//|  Scanning Range   : {2}
      |  |//|  Scanning Timeout : {3}
      |  |.-|
      |.-'**|
       \***/
        \*/
         V
'''.format(options.target,ip_address,options.range,options.timeout)

print ""
confirm = raw_input("Confirmation (Y/n) > ")
if confirm == "n" or confirm == "N" or confirm == "no" or confirm == "NO" or confirm == "No":
	print ""
	print "[-] Scanning Canceled with Confirmation..."
	print ""
	exit()
else:
	pass

print ""
print "[-] WARNING: This Tools only work with TCP Port!"
print "[+] Start Scanning to %s" % ip_address

for i in range(1,(options.range + 1)):
	try:
		pedang = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		pedang.settimeout(options.timeout)
		hasil = pedang.connect_ex((ip_address,i))
		if hasil == 0:
			print " |---> Port %s is Open as TCP!" % i
		else:
			pass
	except KeyboardInterrupt:
		print ""
		print "[-] Attack Canceled with Keyboard Interrupt by User..."
		print ""
		jeda()
		break
	except:
		print ""
		print "[-] Unknown Error has been occured! Sorry..."
		print ""
		exit()
print "[+] Stop Scanning to %s" % ip_address

# Copyright by M-XacT-666
''' Script Kiddie, learn this script and modify with Your own style.
    Do not Paste and Copy it.
    Changing the Variabel and the Author Name didn't make You be a Programmer '''