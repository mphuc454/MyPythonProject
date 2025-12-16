import numpy as np
import cv2 as cv

img = cv.imread("D:\ThuMucCuaTui\Programmer\PythonApp\img\Beautiful.png")


def Harmonic(gray, ksize):
    count = ksize // 2
    pad = np.pad(gray, count) + 10e-9
    out = np.zeros(gray.shape, dtype=np.float64)
    M,N  = gray.shape
    for row in range(M):
        for col in range(N):
            sub = pad[row:row+ksize, col:col+ksize]
            A = ksize * ksize
            B = np.sum(1/sub)
            out[row, col] = A/B
            
    return np.clip(out,0, 255).astype(np.uint8)

def contraHarmonic(gray, ksize, Q):
    count = ksize // 2
    pad = np.pad(gray, count) + 10e-9
    out = np.zeros(gray.shape, dtype=np.float64)
    M,N  = gray.shape
    for row in range(M):
        for col in range(N):
            sub = pad[row:row+ksize, col:col+ksize]
            A = np.sum(sub**(Q+1))
            B = np.sum(sub+Q)
            out[row, col] = A/B
            
    return np.clip(out,0, 255).astype(np.uint8)
    

cv.imshow("Img", Harmonic(cv.cvtColor(img, cv.COLOR_BGR2GRAY), 5))
cv.waitKey()
cv.destroyAllWindows