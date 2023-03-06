# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:47:33 2023

@author: User
"""
import pytesseract
import random
from io import BytesIO
from PIL import ImageFilter, ImageFont, ImageDraw, Image

def Ocr(img_name):
    img = Image.open(img_name)
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)
   
 
def check_code(width=120, height=30, char_length=4, font_file='../static/fonts/framdit.ttf', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')
 
    def rndChar():
        """
        生成随机字母
        :return:
        """
        chooses =[]
        a = chr(random.randint(65, 90))
        b = chr(random.randint(97, 122))
        chooses.append(a)
        chooses.append(b)
        return random.choice(chooses)
 
    def rndColor():
        """
        生成随机颜色
        :return:
        """
        return (random.randint(0, 255), random.randint(10, 255), random.randint(64, 255))
 
    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndChar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text([i * width / char_length, h], char, font=font, fill=rndColor())
    
    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
 
    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndColor())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rndColor())
 
    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
 
        draw.line((x1, y1, x2, y2), fill=rndColor())
   
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)
    
 
if __name__ == '__main__':
 
    #保存到文件
    img,code = check_code()
    with open('code.png','wb') as f:
        img.save(f,format='png')
 
    # 保存到内存
    Ocr('code.png')
    
    # img, code_string = check_code()
    # stream = BytesIO()
    # img.save(stream, 'png')