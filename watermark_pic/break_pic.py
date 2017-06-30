import os
from PIL import Image



def crop_and_save(im, start_point, tmp_path):
    im.crop(start_point).save(tmp_path)

def split(images_path, w, h, save_path):
    for path, _, files in os.walk(images_path):
        c = 0
        for f in files:
            c += 1
            print('progress :'+str(c))
            image_path = path+f
            im = Image.open(image_path)
            width, height = im.size
            i = 0
            for start_width in range(0, width, w):
                for start_height in range(0, height, h):
                    if start_width+w > width or start_height+h > height:
                        continue
                    i += 1
                    start_point = (start_width, start_height, start_width+w, start_height+h)
                    tmp_path = save_path+str(i)+'_'+f
                    crop_and_save(im, start_point, tmp_path)
                
if __name__=='__main__':
    save_path = 'split_dir/'
    w = 227
    h = 56
    images_path = './download_pic/'
    split(images_path, w, h, save_path)
    
