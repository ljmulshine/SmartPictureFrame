#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd7in5
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

try:
    epd = epd7in5.EPD()
    epd.init()
    
    print "read bmp file"
    Himage = Image.open('/home/pi/SmartPictureFrame/images/K_L1.bmp')
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)
        
    epd.sleep()
        
except:
    print 'traceback.format_exc():\n%s' % traceback.format_exc()
    exit()

