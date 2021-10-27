#!/usr/bin/python3

# Script to get rid of the random 12-count chunk that the CLI version
# of youtube-dl appends to the downloaded tracks in current directory.
# It leaves every filetype but mp3 alone.

import os

for x in os.listdir():		# Read through the directory content
	
	if x[-4:] == '.mp3':		# If it's an mp3 rename it, otherwise leave it alone

		first, last = x.split('.')

		y = str(first)				# Get the string without randoms
		yd = len(y) - len(y[-12:])
		yf = y[:yd]

		output = (yf + '.' + last) 	 # Add the '.mp3' again

		os.rename(x, output)		# Rename string to shortened version (Source, Destination)

	else:
		pass

sys.exit()	