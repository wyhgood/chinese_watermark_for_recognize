#-*- coding: utf-8 -*-  
from PIL import Image,ImageDraw,ImageFont  
ttfont = ImageFont.truetype("/Library/Fonts/.ttf",20)

im = Image.open("FINISH.jpg")  
draw = ImageDraw.Draw(im)  
draw.text((10,10),u'韩寒', fill=(0,0,0),font=ttfont)  
draw.text((40,40),unicode('杨利伟','utf-8'), fill=(0,0,0),font=ttfont)  
im.show()
