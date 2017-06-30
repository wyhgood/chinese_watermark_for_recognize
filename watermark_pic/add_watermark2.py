from PIL import Image
import random
import os

#im = Image.open("daodao_crop.jpg")
mark = Image.open("./oneday2.png")

for root, dirs, files in os.walk('./split_dir/'):        
        for f in files:
            im = Image.open('./split_dir/'+f)
            
            layer = Image.new('RGBA', im.size, (0,0,0,0))
            #layer.show()
            #r1 = 30+random.randint(0, 20)
            #r2 = 30+random.randint(0, 20)
            layer.paste(mark, (0, 0))
            out=Image.composite(layer, im, layer)
            out.save('./split_dir_with_mark/'+f)
