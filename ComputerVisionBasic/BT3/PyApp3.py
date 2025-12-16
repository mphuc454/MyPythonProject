import numpy as np
import cv2 as cv

L = 8
img = np.array([[4,7,4,7,3],
                [2,5,5,3,6],
                [7,4,3,1,3],
                [5,6,2,4,3],
                [4,4,5,3,3]])

def histCal(gray, l):
    hist = np.zeros((l,), dtype= float)
    M, N = gray.shape
    for i in range(M):
        for j in range(N):
            g = gray[i,j]
            hist[g] += 1
    hist /= gray.size
    return hist

def histEqual(gray, l):
    hist = histCal(gray, l)
    cs = np.zeros_like(hist)
    for k in range(l):
        cs[k] = hist[:k+1].sum()
    cMax = 1
    gMin = np.min(gray)
    cMin = cs[gMin]
    conf = (L-1)/(cMax-cMin)
    cs = np.round((cs-cMin) * conf)
    cs = cs.astype(np.uint8)


    out = np.zeros_like(gray)
    M,N = gray.shape
    for r in range(M):
        for c in range(N):
            g = gray[r,c]
            out [r,c] = cs[g]
    return out


print("Histogram: ",histCal(img, L))
print(histEqual(img, L))

