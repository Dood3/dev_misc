#!/usr/bin/python3

import sys
import base64

#--------------------------------------------------------------------

if sys.version_info < (3,0):
	
	print("====================================================")
	print("")
	print("      Nope, at least Python 3.0 or go home..       ")
	print("")
	print("====================================================")
	sys.exit()

#--------------------------------------------------------------------

if len(sys.argv) <= 3:
	
	print("====================================================")
	print("")
	print("DECODE a file with a list of base64 encoded strings")
	print((sys.argv[0]) +" -d <inputfile> <outputfile>")
	print("")
	print("ENCODE a file with a list of strings to base64")
	print((sys.argv[0]) +" -e <inputfile> <outputfile>")
	print("")
	print("PREPEND a string before every line in a .txt file")
	print((sys.argv[0]) +" -p <string to prepend> <inputfile> <outputfile>")
	print("")
	print("APPEND a string after every line in a .txt file")
	print((sys.argv[0]) +" -a <string to append> <inputfile> <outputfile>")
	print("")
	print("URL-ENCODE a string")
	print((sys.argv[0]) +" -u <string to encode>")
	print("")
	print("SEARCH & CHANGE strings in a file and write it to a new one")
	print((sys.argv[0]) +" -r <inputfile> <old_string> <outputfile> <new_string>")
	print("")
	print("====================================================")
	sys.exit()

#--------------------------------------------------------------------

def f_decode():

	try:
		inf = open(sys.argv[2], "rb")
		outf = open(sys.argv[3], "a")
		
		for line in inf:  
    			decode = base64.b64decode(line).strip()
    			s = str(decode, 'utf-8')
    			outf.write(s + '\n')
    
		outf.close()

	except:
		print((sys.argv[0]) +" -d inputfile outputfile")

#--------------------------------------------------------------------

def f_encode():

	try:
		inf = open(sys.argv[2], "rb")
		outf = open(sys.argv[3], "a")

		for line in inf:  
    			encode = base64.b64encode(line).strip()
    			s = str(encode, 'utf-8')
    			outf.write(s + '\n')
    
		outf.close()

	except:
		print((sys.argv[0]) +" -e inputfile outputfile")

#--------------------------------------------------------------------

import urllib.parse

def url_enc():
	input_string = sys.argv[2]
	out_string = urllib.parse.quote_plus(input_string)
	print(out_string)

#--------------------------------------------------------------------

def prepend():
	
	try:
		name_p = str(sys.argv[2])
		dictionary_p = sys.argv[3]

		inf = open(dictionary_p, "r")
		outf = open(sys.argv[4], "a")

		for line in inf:
			addition_p = name_p + line.strip()
			outf.write(addition_p + '\n')

		outf.close()

	except:
		print((sys.argv[0]) +" -p string_to_prepend inputfile outputfile") 

#----------------------------------------------------------------------

def append():

	try:
		name_a = str(sys.argv[2])
		dictionary_a = sys.argv[3]

		inf = open(dictionary_a, "r")
		outf = open(sys.argv[4], "a")

		for line in inf:
			addition_a = line.strip() + name_a
			outf.write(addition_a + '\n')

		outf.close()

	except:
		print((sys.argv[0]) +" -a string_to_append inputfile outputfile")

#----------------------------------------------------------------------

def refactor():

	try:
		with open(sys.argv[1], 'r') as file:

			filedata = file.read()
			filedata = filedata.replace(sys.argv[2], sys.argv[4])

			with open(sys.argv[3], 'w') as file:
				file.write(filedata)

	except:
		print((sys.argv[0]) +" -r <inputfile> <old_string> <outputfile> <new_string>")

#----------------------------------------------------------------------

if (sys.argv[1]) == "-d":
	f_decode()
	sys.exit()

elif (sys.argv[1]) == "-e":
	f_encode()
	sys.exit()

elif (sys.argv[1]) == "-u":
	url_enc()
	sys.exit()

elif (sys.argv[1]) == "-p":
	prepend()
	sys.exit()

elif (sys.argv[1]) == "-a":
	append()
	sys.exit()

elif (sys.argv[1]) == "-r":
	refactor()
	sys.exit()

else:
	print("Somewhere along the way you got lost... Bye bye")
	sys.exit()