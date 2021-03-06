import os
import random
from PIL import Image





#生成随机的宽高
def generate_width_height():
    height = random.randint(50, 100)
    times = random.randint(1,3)
    width = height*times
    
    print(height)
    print(width)
    return (width, height)



def split_image(img_path, save_path, flag=False):
    im = Image.open(img_path)
    width, height = im.size
    print(width/2, height/2)
    wid_start = random.randint(0, int(width/2))
    hei_start = random.randint(0, int(height/2))
    wid_dela, hei_dela = generate_width_height()
    wid_end = wid_start+wid_dela
    hei_end = hei_start+hei_dela
    if wid_end>width or hei_end > height:
        print('exceed original pic size')
        return 
    box = (wid_start, hei_start, wid_end, hei_end)
    
    region = im.crop(box)
    if flag:
        new_save_path = save_path.replace('result', 'result_resize')
        region.resize((100, 32),Image.ANTIALIAS).save(new_save_path)
        return
    region.save(save_path)


def start_task():
    save_path = './result/'
    for path,_,files in os.walk('./pic/'):
        print(path)
        print(files)
        i = 1
        for f_name in files:
            
            tmp_path = path+f_name
            print(tmp_path)
            tmp_save_path = save_path+str(i)+'.jpg'
            split_image(tmp_path, tmp_save_path, flag=True)
            i += 1
            print(i)
                      
if __name__=='__main__':
    print('1111111')
    #split_image('./test.jpg')
    start_task()
