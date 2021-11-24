#!/usr/bin/python3

import os, sys
import netifaces
import subprocess
import http.server
import socketserver

iface = input("Name of Interface: ")
url = input("Name of site to clone: ")
port = 8000

#------------------------------------------------------------------------
class Whatup:

	def hosts(self):

		ip = netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']
		try:
			d = open("hosts.txt", "w")
			d.write(ip + "	" + url)
			d.close()

		except:
			print("Opening custom host file failed")
			sys.exit()

#------------------------------------------------------------------------

	def clone(self):
		#url = sname
		DNULL = open(os.devnull, 'w')
		whereami = os.getcwd()
		wget = subprocess.call('wget', shell=True, stdout=DNULL, stderr=subprocess.STDOUT)

		if os.path.exists("templates/"):
			subprocess.Popen(f'wget -H -N -k -p -l 2 -nd -P templates/{url} --no-check-certificate {url}', shell=True).wait()
			print(whereami, url)

		else:
			os.makedirs("templates/")
			subprocess.Popen(f'wget -H -N -k -p -l 2 -nd -P templates/{url} --no-check-certificate {url}', shell=True).wait()
			print("ERROR")
			print(whereami, url)

#------------------------------------------------------------------------
if __name__ == '__main__':
	p = Whatup()
	p.hosts()
	p.clone()

	print("Serving " + url + " on port " + str(port))
	os.chdir("templates/" + url)
	httpd = socketserver.TCPServer(('', port), http.server.SimpleHTTPRequestHandler)
	httpd.serve_forever()
