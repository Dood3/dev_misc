#!/usr/bin/python3

import sys
import qrcode

#---------------------------------------------------

if len(sys.argv) <= 2:
	print("====================================================")
	print("Create a QR-Code leading to a link as .png:")
	print("python3 "(sys.argv[0]) +" <link> <outputfile>")
	print("====================================================")
	sys.exit(0)

#---------------------------------------------------

qr = qrcode.QRCode(
	version = 1,
	error_correction = qrcode.constants.ERROR_CORRECT_H,
	box_size = 7,
	border = 4,
	)

qr.add_data(sys.argv[1])
qr.make(fit = True)

img = qr.make_image()
img.save(sys.argv[2] + ".png")
