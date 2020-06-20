import qrcode
# example data
data = "http://shokr.works"
# output file name
filename = "site.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)