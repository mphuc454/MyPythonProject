import cv2 as cv
import numpy as np

def stretch(gray):
    min = gray.min()
    max = gray.max()
    change = 255 / (max - min)
    out = (gray - min) * change
    return out
    
def createIdealP(shape, D0):
    H = np.zeros(shape, dtype=np.float32)
    M,N = shape
    D0 = D0 * D0
    for u in range(M):
        for v in range(N):
            D = (u-M/2) **2 + (v-N/2)**2
            if D <= D0:
                H[u,v] = 1
    return H
def createIdealP_Circle(shape, D0):
    H = np.zeros(shape, dtype=np.uint8)
    M,N = shape
    cx = N//2
    cy = M//2
    cv.circle(H, (cx, cy), D0, 1, -1)
    return H
    
img = cv.imread(r'D:\ThuMucCuaTui\Programmer\PythonApp\img\AirportImg.jpg', 0)
Fuv = np.fft.fft2(img)
Fuv = np.fft.fftshift(Fuv)
spaceF =np.log1p(np.abs(Fuv))
spaceF = np.clip(spaceF*5,0,255).astype(np.uint8)


cv.imshow('Original Image', img)
# cv.imshow('SpaceF', spaceF)
# cv.imshow('Stretch', stretch(spaceF))
D0 = 20
H = 1 - createIdealP_Circle(Fuv.shape, D0)
Guv = Fuv * H
spaceG = np.log1p(np.abs(Guv))
spaceG = np.clip(spaceG, 0, 255).astype(np.uint8)
# cv.imshow('Stretch', stretch(spaceF))

Guv = np.fft.ifftshift(Guv)
gxy = np.fft.ifft2(Guv)
gxy = np.clip(np.abs(gxy),0, 255).astype(np.uint8)
cv.imshow('Filtered Image', gxy)
cv.waitKey()
cv.destroyAllWindows()


