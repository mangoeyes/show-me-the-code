#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-09-03 10:10:06
# @Author  : Huijun Wang 

from PIL import Image, ImageDraw, ImageFont

img = Image.open("picture.jpeg")

width, height = img.size
d = ImageDraw.Draw(img)

font = ImageFont.truetype("Arial.ttf", 25)

d.text((width-20,20), "4", fill = (255,0,0), font=font)

img.save('picture1.jpeg')
im = Image.open("picture1.jpeg")

im.show()