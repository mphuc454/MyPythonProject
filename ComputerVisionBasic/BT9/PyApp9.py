import cv2 as cv
import numpy as np

img = cv.imread('', cv.IMREAD_GRAYSCALE)

def adaptive_median_filter(gray, max_min_size):
    img_height, img_width = img.shape
    output = np.zeros(img.shape, img.dtype)
    for row in np.arange(0, img_height):
        for col in np.arange(0, img_width):
            output[row, col] = amf(gray, row, col, max_min_size)
    return output


def amf(gray, row, col, max_min_size):
    ksize = 3
    Zxy = gray[row, col]
    M, N = gray.shape
    while ksize <= max_min_size:
        d = ksize // 2
        Sxy = gray[max(0, row - d):min(M, row + d + 1), max(0, col - d):min(M, col + d + 1)]
        Zmin = np.min(Sxy)
        Zmax = np.max(Sxy)
        Zmed = np.median(Sxy)

        if Zmin < Zmed < Zmax:
            if Zmin < Zxy < Zmax:
                return Zxy
            else:
                return Zmed
        else:
            ksize += 2

        return Zmed