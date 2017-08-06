from PIL import Image, ImageDraw, ImageFont
import random

height = 1600
width = 2560
fntsize = int((width * height) / 300**2)

# Get random colour from pantone rgb list
with open('rgbs.txt') as fp:
    # Get randnum between 0 and list length
    cindex = random.randint(0, sum(1 for _ in fp))
    fp.seek(0)

    for _ in range(cindex):
        fp.readline()
    clrStr = fp.readline().rstrip('\n')

clrDesc = clrStr.split("/")[0]
clrHex = clrStr.split("/")[1]

# Create pap
im = Image.new('RGB', (width, height), "#"+clrHex)
gfx = ImageDraw.Draw(im)

txt  = "PANTONE " + clrDesc + "\n" + clrHex
hlvtc = ImageFont.truetype('helveticaneuebold.ttf', fntsize)

sqsize = int(height/3)
strk = int(fntsize/4)
sqx = int(width/2 - sqsize/2)
sqy = int(height/2 - sqsize/2)

gfx.rectangle(((sqx, sqy),(sqx + sqsize, sqy + sqsize)), fill="white")
gfx.rectangle(((sqx + strk, sqy + strk),
              (sqx + sqsize - strk, sqy + sqsize - strk)), fill="#"+clrHex)

gfx.text((sqx + fntsize, sqy + sqsize - fntsize*3), txt, font=hlvtc, fill="white")


im.save("pap.png", "PNG")
