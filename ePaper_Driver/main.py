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
    
    # select random image from image directory
    imageNumber = random.randint(1,len(os.listdir('/home/pi/SmartPictureFrame/images')))
    imagePath = '/home/pi/SmartPictureFrame/images/K_L' + str(imageNumber) + '.bmp'
    
    # display image
    Himage = Image.open(imagePath)
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)    
    epd.sleep()
        
except:
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    exit()

