import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg', 0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

rows, cols = img.shape
crow, ccol = rows//2, cols//2
fshift[crow-30:crow+30, ccol-30:ccol+30] = 0
f_ishift = np.fft.ifftshift(fshift)
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title('Input'), plt.xticks([]), plt.yticks([])

plt.subplot(122)
plt.imshow(img_back)
plt.title('High-Pass'), plt.xticks([]), plt.yticks([])

plt.show()