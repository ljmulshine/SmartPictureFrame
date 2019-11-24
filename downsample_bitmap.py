import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from skimage import io
from skimage.transform import resize, rotate
from PIL import Image


image = io.imread("JPGS/IMG_11.jpg", as_grey=True)
image = resize(image, (384, 640), mode='symmetric')
image = rotate(image, 0)


bitmap = np.array(image) * 255
print(bitmap)
bitmap = np.dot((bitmap > 110).astype(float), 255)
print(bitmap)

plt.imshow(bitmap, cmap='gray')
plt.show()
im=Image.fromarray(bitmap.astype(np.uint8))
im.save('K_L30.bmp')


#nPhoto = 5
#imageFiles = os.listdir('images')
#for file in imageFiles[1]:
#    if file.endswith('.jpg'):
#        # read, resize and rotate jpg
#        image = io.imread('images/' + file, as_grey=True)
#        image = resize(image, (384, 640), mode='symmetric')
#        image = rotate(image, 180)
#        bitmap = np.array(image) * 255
#        bitmap = np.dot((bitmap > 80).astype(float), 255)
#        im=Image.fromarray(bitmap.astype(np.uint8))
        
        #        # save photo
        #        nPhoto = nPhoto + 1
        #        im.save('K_L' + str(nPhoto) +  '.bmp')
