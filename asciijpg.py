from PIL import Image,ImageDraw,ImageFont
import math

image = Image.open("morotskaka.jpg")
scaleFac = 0.8
charWidth = 10
charHeight = 18
w,h = image.size
image = image.resize((int(scaleFac*w),int(scaleFac*h*(charWidth/charHeight))),Image.NEAREST)
w,h = image.size
pixels = image.load()
outputImage = Image.new('RGB',(charWidth*w,charHeight*h),color=(0,0,0))
draw = ImageDraw.Draw(outputImage)
font = ImageFont.truetype('/usr/share/fonts/truetype/NotoMono-Regular.ttf',15)
outputImage = Image.new('RGB',(charWidth*w,charHeight*h),color=(0,0,0))
print(outputImage)
draw = ImageDraw.Draw(outputImage)


def getSomeChar(h):
    chars  = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    charArr = list(chars)
    l = len(charArr)
    mul = l/256
    return charArr[math.floor(h*mul)]

for i in range(h):
        for j in range(w):
            r,g,b = pixels[j,i]
            grey = int((r/3+g/3+b/3))
            pixels[j,i] = (grey,grey,grey)
            #draw = [getSomeChar(grey)[index:index + charWidth] for index in range(0, charWidth, charHeight)]
            #draw = (getSomeChar(grey))
            #print(draw)

new_pixels = getSomeChar(grey)
new_pixels = ''.join(new_pixels)
new_pixels_count = len(new_pixels)
ascii_image = [new_pixels[index:index + charWidth] for index in range(0, new_pixels_count, charWidth)]
ascii_image = "\n".join(ascii_image)
print(ascii_image)