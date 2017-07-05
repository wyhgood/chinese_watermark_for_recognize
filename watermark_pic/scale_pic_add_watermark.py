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
    for path, _, files in os.walk(pic_dir):
        for f_name in files:
            img_path = path+f_name
            im_tmp = Image.open(img_path)
            w, h = im_tmp.size
            layer = Image.new('RGBA', im.size, (0,0,0,0))
            #layer.show()                                                                                                                            
            r1 = random.randint(int(-width/4), w-width+int(width/4))
            r2 = random.randint(int(-height/4), h-height+int(height/4))                                     
            #layer.paste(im, (r1, r2))
            layer.paste(im, (0, 0))
            out=Image.composite(layer, im_tmp, layer)
            out.save(save_dir+f_name)


if __name__=='__main__':
    add_watermark('./result_pic/','./tencent1.png','tmp/')
