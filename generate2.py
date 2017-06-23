import random
from PIL import Image, ImageDraw,ImageFont



def add_watermark(imgPath, font, font_size, text, fill=(100,12,89,255)):
    im = Image.open(imgPath).convert('RGBA')
    txt=Image.new('RGBA', im.size, (0,0,0,0))
    #fnt=ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 50)
    fnt=ImageFont.truetype(font, font_size)

    d=ImageDraw.Draw(txt)
    
    d.text((txt.size[0]-300,txt.size[1]-300), text, font=fnt, fill=fill)
    out=Image.alpha_composite(im, txt)
    out.save('target.jpg')
    out.show()
    
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

if __name__=="__main__":
    text = read_word()
    font = "/System/Library/Fonts/PingFang.ttc"
    img_path = "./test.jpg"
    add_watermark(img_path, font, 50, text, fill=(100,12,89,255))

    
