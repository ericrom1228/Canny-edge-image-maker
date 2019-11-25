import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
	pass

img = cv2.imread('Eric_Romano.jpg',0)
window_title = 'edges with trackbar'

cv2.namedWindow(window_title)
cv2.createTrackbar('min', window_title, 0, 200, nothing)
cv2.createTrackbar('max', window_title, 300, 500, nothing)

while True:
	
	minval = cv2.getTrackbarPos('min', window_title)
	maxval = cv2.getTrackbarPos('max', window_title)
	
	edges = cv2.Canny(img,minval,maxval)
	numpy_horizontal = np.hstack((img,edges))
	cv2.imshow(window_title, numpy_horizontal)
	if cv2.waitKey(1) == 27: #27 is the value of the ESC key
		break

cv2.destroyAllWindows()

'''
plt.subplot(1,2,1), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2), plt.imshow(edges, cmap='gray'), plt.title('Edges')
plt.xticks([]), plt.yticks([])

plt.show()
'''

