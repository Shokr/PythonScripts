"""
This is a quick script to extract background from image, it is based on lowpass filter
"""

from sys import argv

from PIL import Image

image_name = ""
if len(argv) != 4:
    print("My have input, output and factor")
    exit()
else:
    image_name = argv[1]
    out = argv[2]
    factor = float(argv[3])

kFilteringFactor = factor


def filter(r, g, b, prevR, prevG, prevB):
    accelFunc = lambda c, p: (c * kFilteringFactor) + (p * (1 - kFilteringFactor))
    accelR = accelFunc(r, prevR)
    accelG = accelFunc(g, prevG)
    accelB = accelFunc(b, prevB)
    return (accelR, accelG, accelB)


def process_image(image_name, out):
    im = Image.open(image_name)
    pix = im.load()

    outim = Image.new('RGB', im.size)
    outpix = outim.load()

    for y in range(1, im.size[1]):
        pr = pix[0, y][0]
        pg = pix[1, y][0]
        pb = pix[2, y][0]
        for x in range(1, im.size[0]):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            pr, pg, pb = filter(r, g, b, pr, pg, pb)
            if sum([pr, pg, pb]) / 3 < 125:
                outpix[x, y] = pix[x, y]
            else:
                outpix[x, y] = (255, 255, 255)

    outim.save(out)


process_image(image_name, out + str(kFilteringFactor) + ".png")

# from glob import glob

# counter = 0
# for image_name in glob("./Pictures/*.jpg"):
#     process_image(image_name, './out/' + str(counter) + ".png")
#     counter += 1
