'''
给定图片的大小， 生成一系列的几倍于其宽的 正方形窗口图片
参数 输入
     raw_pic datadir 原始图片的路径
     width 窗口size
     save_dir 生成的各类scale的图片
     max_per_pic 每张图片最多 抠出的窗口数
     total_number 总共要获取多少张窗口图片
'''

import os
import sys
from PIL import Image


def scale_generate(width):
    l = []
    l.append(int(width*1.1))
    l.append(int(width*1.2))
    l.append(int(width*1.3))
    l.append(int(width*1.4))
    l.append(int(width*1.5))
    return l




def split_pic(w, max_per_pic, img_path):
    img_list = []
    im = Image.open(img_path)
    im.size

    im = Image.open(img_path)
    width, height = im.size
    j = 0
    for start_width in range(0, width, w):
        for start_height in range(0, height, w):
            if start_width+w > width or start_height+w > height:
                continue
            j += 1
            if j > max_per_pic: continue
            
            
            start_point = (start_width, start_height, start_width+w, start_height+w)
            img_list.append(im.crop(start_point))
    return img_list

def pic_generate(width, raw_pic_dir, save_dir, max_per_pic=10, total_number_per_scale=1000):
    scale_list = scale_generate(width)
    for scale in scale_list:
        print('current scale:'+str(scale))
        for path, _, files in os.walk(raw_pic_dir):
            c = 0
            for f_name in files:
                if c > total_number_per_scale: continue
                print('current scale '+str(scale)+'current scale number '+str(c) +' current file:'+f_name + " file consumed number:"+str(c))
                img_path = path+f_name
                #拿到一张原始图片后
                img_list = split_pic(scale, max_per_pic, img_path)
                c+=len(img_list)
                
                print('generate pic number is:'+ str(len(img_list)))
                i = 0
                for im in img_list:
                    i += 1
                    save_path = save_dir+'_'+str(scale)+'_'+str(i)+'_'+f_name
                    im.save(save_path)
                    
if __name__=='__main__':
    print('-_-')
    l = scale_generate(10)
    print(l)
    width = sys.argv[1]
    raw_pic_dir = sys.argv[2]
    save_dir = sys.argv[3]
    print(width, raw_pic_dir, save_dir)
    pic_generate(int(width), raw_pic_dir, save_dir)
