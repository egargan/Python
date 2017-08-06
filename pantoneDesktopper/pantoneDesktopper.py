from PIL import Image, ImageDraw, ImageColor
import random

height = 1600
width = 2560

# Get random colour from pantone rgb list
with open('rgbs.txt') as fp:

    cindex = random.randint(0, sum(1 for _ in fp))
    fp.seek(0)

    for _ in range(cindex):
        fp.readline()

    colourStr = fp.readline().rstrip('\n')

# Create pap with base colour
im = Image.new('RGB', (width, height), "#" + colourStr.split("/")[1])
gfx = ImageDraw.Draw(im)

#with open("pap.png", 'w+') as wfp:
im.save("pap.png", "PNG")
