import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", 24)
#打开图片
imageFile = "./test.jpg"
im = Image.open(imageFile)

#画图
draw = ImageDraw.Draw(im)
draw.text((160, 0), '你好'.encode('utf-8'), (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
draw = ImageDraw.Draw(im)                          #Just draw it!

#另存图片
im.save("target.jpg")
