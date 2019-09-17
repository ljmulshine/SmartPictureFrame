import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from skimage import io
from skimage.transform import resize, rotate
from PIL import Image


image = io.imread("K_L2.jpg", as_grey=True)
image = resize(image, (384, 640), mode='symmetric')
image = rotate(image, 180)


bitmap = np.array(image) * 255
print(bitmap)
bitmap = np.dot((bitmap > 100).astype(float), 255)
print(bitmap)

plt.imshow(bitmap, cmap='gray')
plt.show()
im=Image.fromarray(bitmap.astype(np.uint8))
im.save('K_L2.bmp')