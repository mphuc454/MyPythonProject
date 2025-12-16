import numpy as np
img = np.array([[5,2,6,10],
                [4,3,4,11],
                [3,9,2,20],
                [9,10,11,25]])

def convolution(gray, kernel):
    output = np.zeros((gray.shape), dtype=np.float32)
    ksize = kernel.shape[0]
    p_count = ksize // 2
    padded = np.pad(gray, p_count)
    M, N = gray.shape
    for row in range(M):
        for col in range(N):
            sub = padded[row:row+ksize, col:col+ksize]
            output[row, col] = np.sum(sub * kernel)
    return output
            

def mean_Filter(gray, ksize):
    k = np.zeros((ksize, ksize), dtype=np.float32)
    k /= (ksize + ksize)
    out = convolution(gray, k)
    return np.clip(out, 0, 255).astype(np.uint8)

def median(gray, Ksize):
    output = np.zeros_like(gray)
    p_count = Ksize // 2
    padded = np.pad(gray, p_count)
    M, N = gray.shape
    for row in range(M):
        for col in range(N):
            sub = padded[row:row+Ksize, col:col+Ksize]
            arr = np.sort(sub, axis= None)
            index = sub.size // 2
            output[row, col] = arr[index]
    return output

def median2(gray, Ksize):
    output = np.zeros_like(gray)
    p_count = Ksize // 2
    M, N = gray.shape
    for row in range(M):
        for col in range(N):
            sub = gray[max(0, row-p_count) : min(M, row+p_count+1), max(0, col-p_count) : min(M, col+p_count+1)]
            arr = np.sort(sub, axis= None)
            index = sub.size // 2
            if(sub.size % 2 == 1):
                output[row, col] = arr[index]
            else:
                output[row, col] = arr[index] +arr[index+1]
    return output

res = convolution(img, img)
print(res)