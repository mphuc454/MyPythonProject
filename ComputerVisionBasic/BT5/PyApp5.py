import numpy as np
import cv2 as cv

img = cv.imread(r'D:\ThuMucCuaTui\Programmer\PythonApp\img\Beautiful.png', 0)
def conv(gray, kernel):
    ks = kernel.shape[0]
    half = ks // 2
    padded = np.pad(gray, half)
    out = np.zeros_like(gray, dtype=np.float32)
    M, N = gray.shape
    for row in range(M):
        for col in range(N):
            sub = padded[row:row+ks, col:col+ks]
            out[row, col] = np.sum(sub * kernel)
    return out

def Laplacian(gray):
    kernel = np.array([[0, -1, 0],
                      [-1, 5, -1],
                      [0, -1, 0]])
    return np.clip(conv(gray, kernel), 0, 255).astype(np.uint8)

def sobel(gray):
    kx = np.array([[1,0,-1],
                   [2,0,-2],
                   [1,0,-1]])
    ky = np.array([[1,2,1],
                   [0,0,0],
                   [-1,-2,-1]])

    sx = conv(gray, kx)
    sy = conv(gray, ky)

    sobel_img = 0.5 * sx + 0.5 * sy
    sharp_img = gray + sobel_img

    sobel_img = np.clip(sobel_img, 0, 255).astype(np.uint8)
    sharp_img = np.clip(sharp_img, 0, 255).astype(np.uint8)

    return sobel_img, sharp_img 


lap = Laplacian(img)
sobel_img, sharp_img = sobel(img) 

cv.imshow('Origin Image', img)
cv.imshow('Laplacian', lap)
cv.imshow('Sobel', sobel_img) 
cv.imshow('Sharp Image', sharp_img)

cv.waitKey(0)
cv.destroyAllWindows()
