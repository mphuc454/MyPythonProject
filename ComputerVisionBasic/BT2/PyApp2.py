import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


path = r'img/Beautiful.png'
img = cv.imread(path)


def daoAnh(i):
    return 255 - i

def loga_img(c, i):
    return float(c) * cv.log(1.0 + i)

def gamma_img(c, i, g):
    return float(c) * np.pow(i, float(g))


fig, axs = plt.subplots(2,2, figsize=(10,10))
axs[0,0].imshow(img)
axs[0,0].set_title('Ảnh gốc')

axs[0,1].imshow(daoAnh(img))
axs[0,1].set_title('Đảo ảnh')

axs[1,0].imshow(loga_img(2, img))
axs[1,0].set_title('Ảnh Logarit')

axs[1,1].imshow(gamma_img(1.0, img, 3.0))
axs[1,1].set_title('Ảnh Gamma')

for ax in axs.flat:
    ax.axis('off')
plt.show()