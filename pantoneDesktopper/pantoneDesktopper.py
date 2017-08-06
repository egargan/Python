from PIL import Image, ImageDraw
import random

height = 1600
width = 2560

im = Image.new('RGB', (width, height))
gfx = ImageDraw.Draw(im)


def randColour():

    with open('rgbs.txt') as fp:

        cindex = random.randint(0, sum(1 for _ in fp))
        fp.seek(0)

        for _ in range(cindex):
            fp.readline()

        return fp.readline().rstrip('\n')



colourStr = randColour()

cHex = colourStr.split("/")[1]
r = int('0x' + cHex[0:2], 0)
g = int('0x' + cHex[2:4], 0)
b = int('0x' + cHex[4:6], 0)

print(r,g,b)
