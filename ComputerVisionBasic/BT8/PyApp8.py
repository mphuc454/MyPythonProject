import numpy as np

image = np.array([
    [4, 5, 7, 3],
    [7, 11, 5, 8],
    [4, 9, 10, 6],
    [3, 8, 7, 11]
])


def threshold(gray, T):
    out = np.zeros_like(gray)
    out[gray <= 1] = 0
    out[gray > T] = 1
    return out


def createHist(gray, L):
    hist = np.zeros((L,), dtype=np.int32)
    M, N = gray.shape
    for row in range(M):
        for col in range(N):
            g = gray[row, col]
            hist[g] += 1
    return hist


def findOtsu(gray, L):
    hist = createHist(gray, L)
    var0 = 0
    found_T = 0
    index = np.array(range(L))
    for T in range(L):
        w0 = np.sum(hist[:T + 1]) / gray.size
        w1 = 1 - w0
        m0 = np.sum(hist[:T + 1] * index[:T + 1]) / np.sum(hist[:T + 1])
        m1 = np.sum(hist[T + 1:] * index[T + 1:]) / np.sum(hist[T + 1:])
        var = w0 + w1 * (m0 - m1) * (m0 - m1)
        if var > var0:
            var0 = var
            found_T = T
    return found_T

print(threshold(image, 6))
