from PIL import Image, ImageDraw,ImageFont



def add_watermark(imgPath, font, font_size, fill, text):
    im = Image.open("./test.jpg").convert('RGBA')
    txt=Image.new('RGBA', im.size, (0,0,0,0))
    fnt=ImageFont.truetype("/System/Library/Fonts/PingFang.ttc", 50)
    d=ImageDraw.Draw(txt)
    d.text((txt.size[0]-300,txt.size[1]-300), "北京航空航天大学", font=fnt, fill=(100,12,89,255))
    out=Image.alpha_composite(im, txt)
    out.show()






if __name__=="__main__":
    print
