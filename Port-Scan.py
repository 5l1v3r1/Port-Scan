#!/usr/bin/python2
#############################
import sys, optparse,platform
sys.path.append('./lib/')
import core_ps
import socket
#############################
opsys = platform.system()
usage_utama = "[?] Use 'Port-Scan.py --help' to show Help Contents"
#############################

def main():
	core_ps.clearscreen(opsys)
	### VARIABEL UTAMA ###
	ps_scanrange = 1000
	ps_timeout = 0.2
	### END OF ### VARIABEL UTAMA ###

	core_ps.judul()
	try:
		if sys.argv[1] == "-h" or "--help":
			print "[X] Example: Port-Scan.py -t 192.168.229.128"
			print "             Port-Scan.py --t 192.168.229.128 -r 100 --timeout=0.3"
			print ""
	except IndexError:
		None
	parser = optparse.OptionParser()
	parser.add_option("-t",dest="TARGET",help="Specify the Target")
	parser.add_option("--target",dest="TARGET",help="Specify the Target")
	parser.add_option("-r",dest="PORT_RANGE",help="Port Scan Range (Default is 1000)")
	parser.add_option("--range",dest="PORT_RANGE",help="Port Scan Range (Default is 1000)")
	parser.add_option("--timeout",dest="TIMEOUT",help="Timeout for scanning Port (Default is 0.2) [OPTIONAL]")
	(options,args) = parser.parse_args()
	if options.TARGET == None:
		print usage_utama
		exit()
	try:
		if bool(options.TARGET) == True:
			ps_target = options.TARGET
		if bool(options.PORT_RANGE) == True:
			ps_scanrange = options.PORT_RANGE
		if bool(options.TIMEOUT) == True:
			ps_timeout = options.TIMEOUT
	except:
		main()
	print ""
	print "[>] Set Target --------> %s" % ps_target
	print "[>] Set Scan Range ----> 1 to %s" % ps_scanrange
	print "[>] Set Scan Timeout --> %s" % ps_timeout 
	print ""
	print "[#]=========={ Start Scanning... }==========[#]"
	print ""
	print "[*] Getting IP Address..."
	try:
		ps_ipaddr = socket.gethostbyname(ps_target)
		print "[+] IP Address : %s" % ps_ipaddr
	except:
		print core_ps.err_cantcon
		exit()
	print ""
	print "[*] Scanning for Opened Port..."
	total_scanned = 0
	for i in range(1,int(ps_scanrange) + 1):
		try:
			total_scanned += 1
			ps_konek = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			ps_konek.settimeout(float(ps_timeout))
			ps_hasil = ps_konek.connect_ex((ps_ipaddr,i))
			if ps_hasil == 0:
				print "[+] Port {} is Open".format(i)			
			ps_konek.close()
		except KeyboardInterrupt:
			print ""
			print core_ps.err_keyint
			break
	print ""
	print "[*] Total Scanned Port : %s" % total_scanned
	print ""
	print "[#]=========={ Scanning Complete }==========[#]"


if __name__ == '__main__':
	main()