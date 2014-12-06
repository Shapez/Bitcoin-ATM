####Create a QR code#####
import qrcode
import json
from pprint import pprint
import urllib

with open('blockchain_api.json') as json_data:
	data = json.load(json_data)
pprint(data)
data["address"]["1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F"]
qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10, border=4)
qr.add_data('address')
qr.make(fit=True)

img = qr.make_image()
