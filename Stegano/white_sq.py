from PIL import Image

original = Image.open('whitesqure.gif')
width, height = original.size

steg = Image.new('RGB', (width, height))

for k in range(3):
    for i in range(width):
        s = ""
        for j in range(height):
            r = original.getpixel((i,j))
            if (r == 0):
                steg.putpixel((i,j), (0, 0, 0))
            else: steg.putpixel((i,j), (255, 255,255))

steg.save("steg.png")
