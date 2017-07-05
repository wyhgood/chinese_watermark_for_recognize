'''
随机添加水印 
 输入 watermark_path 水印路径
      pic_dir  待添加水印的 图片
      save_dir 
将水印 在随机位置 添加到图片上
'''

import os
import random
from PIL import Image

def add_watermark(pic_dir, watermark_path, save_dir):
    im = Image.open(watermark_path)
    width, height = im.size
    i = 0
    for path, _, files in os.walk(pic_dir):
        for f_name in files:
            i += 1
            print(i)
            img_path = path+f_name
            im_tmp = Image.open(img_path)
            w, h = im_tmp.size
            layer = Image.new('RGBA', im_tmp.size, (0,0,0,0))
            #layer.show()
            #print(int(-width/4))
            
            r1 = random.randint(0, w-width)
            r2 = random.randint(0, h-height)                                     
            #r1 = random.randint(0, w-width)
            #r2 = random.randint(0, w-height)
            print(r1, r2)
            #layer.paste(im, (r1, r2))
            layer.paste(im, (r1, r2))
            out=Image.composite(layer, im_tmp, layer)
            out.save(save_dir+f_name)
            out.close


if __name__=='__main__':
    add_watermark('./result_pic/','./tencent1.png','tmp/')
