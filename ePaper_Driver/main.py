#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import random
import os

try:
    epd = epd7in5.EPD()
    epd.init()
    
    if(time.strftime("%d %b", time.localtime()) == "07 Oct"):
        imagePath = '/home/pi/SmartPictureFrame/images/HAPPY_BIRTHDAY.bmp'
    elif(time.strftime("%d %b", time.localtime()) == "25 Nov"):
        imagePath = '/home/pi/SmartPictureFrame/images/K_L26.bmp'
    else:
        # select random image from image directory
        imageNumber = random.randint(1,len(os.listdir('/home/pi/SmartPictureFrame/images')) - 1)
        imagePath = '/home/pi/SmartPictureFrame/images/K_L' + str(imageNumber) + '.bmp'

    # display image
    Himage = Image.open(imagePath)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
    epd.sleep()
        
except:
    exit()

