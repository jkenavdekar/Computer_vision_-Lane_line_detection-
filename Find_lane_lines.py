import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

image_color = mpimg.imread('road2.jpg')
#plt.imshow(image_color)
print(image_color.shape)

image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
#plt.imshow("GrayScale", image_gray)
cv2.imshow("Gray_image", image_color)
cv2.waitKey(0)
cv2.destroyAllWindows

print(image_gray.shape)


image_copy = np.copy(image_gray)
image_copy[(image_copy[:,:] < 250)] = 0
cv2.imshow("Lane_detect", image_copy)
cv2.waitKey(0)
cv2.destroyAllWindows

