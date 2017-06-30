import os
import random
from PIL import Image, ImageDraw,ImageFont



def add_watermark2(start_point, save_path, im, font, font_size, text, fill=(100,12,89,255), flag=False):
    im = im.convert('RGBA')
    txt=Image.new('RGBA', im.size, (0,0,0,0))
    #fnt=ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 50)
    fnt=ImageFont.truetype(font, font_size)

    d=ImageDraw.Draw(txt)
    
    d.text(start_point, text, font=fnt, fill=fill)
    out=Image.alpha_composite(im, txt)
    if flag:
        new_save_path = save_path.replace('word', 'word_resize')
        out.resize((100,32), Image.ANTIALIAS).save(new_save_path)
        return
    out.save(save_path)
    #out.show()
    
#随机生成1-6个文字
def read_word():
    total = random.randint(1, 6)
    res = ''
    with open('./resource/word.txt', 'r') as f:
        lines = f.readlines()
        size = len(lines)
        for i in range(0, total):
            index = random.randint(0, size-1)
            res+=lines[index].strip()
        return res


def generate():
    result_path = './pic_with_word/'    
    for path, _, files in os.walk('./result/'):
        print(files)
        print(path)
        for f_name in files:
            tmp_path = path+f_name
            print(tmp_path)
            font = "/System/Library/Fonts/PingFang.ttc"
            text = read_word()
            im = Image.open(tmp_path)
            width, height = im.size
            start_point = (random.randint(0, int(width/3)), random.randint(0, int(height/3)))
            font_size = int(2*width/8)
            save_path = result_path+f_name

            add_watermark2(start_point, save_path, im, font, font_size, text, fill=(100,12,89,255), flag=True)
           
            

            
if __name__=="__main__":
    text = read_word()
    font = "/System/Library/Fonts/PingFang.ttc"
    img_path = "./test.jpg"
    generate()
    #add_watermark(img_path, font, 50, text, fill=(100,12,89,255))
