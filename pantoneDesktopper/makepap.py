from PIL import Image, ImageDraw, ImageFont
import random

import os.path
import sys

hexchars = ['0','1','2','3','4','5','6','7','8','9',
            'a','b','c','d','e','f',
            'A','B','C','D','E','F']

# Get random colour from pantone rgb list
with open('rgbs.txt') as fp :

    # Expect current colour at top, in form '#current=lineindex'
    currentClr = fp.readline()
    numlines = sum(1 for _ in fp)

    while True :

        fp.seek(0)

        # Get randnum between 1 and list length
        # (index 0 holds current wallpaper colour data)
        cindex = random.randint(1, numlines)

        for _ in range(cindex) :
            fp.readline()

        clrStr = fp.readline().rstrip('\n')
        splitClrStr = clrStr.split("/")

        if clrStr and len(splitClrStr) == 2 :

            clrDesc = clrStr.split("/")[0]
            clrHex = clrStr.split("/")[1]

            if len(clrHex) == 6 and all(c in hexchars for c in clrHex) :
                break

print(cindex) # line number to stdout, for use in sed


height = 1600
width = 2560
fntsize = int((width * height) / 400**2)

# Create pap
im = Image.new('RGB', (width, height), "#"+clrHex)
gfx = ImageDraw.Draw(im)

txt  = "PANTONE " + clrDesc + "\n" + clrHex
fnt = ImageFont.truetype('Pixeled.ttf', fntsize)

sqsize = int(height/3)
strk = int(fntsize/4)
sqx = int(width/2 - sqsize/2)
sqy = int(height/2 - sqsize/2)

gfx.rectangle(((sqx, sqy),(sqx + sqsize, sqy + sqsize)), fill="white")
gfx.rectangle(((sqx + strk, sqy + strk),
              (sqx + sqsize - strk, sqy + sqsize - strk)), fill="#"+clrHex)

gfx.text((sqx + fntsize*1.5, sqy + sqsize - fntsize*6), txt, font=fnt, fill="white")


im.save(os.path.expanduser("~/pap.png"), "PNG")
