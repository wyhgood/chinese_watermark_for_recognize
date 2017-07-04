from PIL import Image
import random
import os

#im = Image.open("daodao_crop.jpg")
mark = Image.open("./oneday.png")

for root, dirs, files in os.walk('./result/'):        
        for f in files:
            im = Image.open('./result/'+f)
            
            layer = Image.new('RGBA', im.size, (0,0,0,0))
            #layer.show()
            r1 = 30+random.randint(0, 20)
            r2 = 30+random.randint(0, 20)
            layer.paste(mark, (r1+100, r2+100))
            out=Image.composite(layer, im, layer)
            out.save('./result/'+f)
