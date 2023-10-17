import cv2
import numpy as np

# Load your image
image = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
image_two = cv2.imread('sf.jpg', cv2.IMREAD_GRAYSCALE)
# Define Laplacian masks
laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

laplacian_sharpened = cv2.filter2D(image, -1, laplacian)
laplacian_sharpened_two = cv2.filter2D(image_two, -1, laplacian)

# Display the sharpened images
# you might have to comment one out to see the image
cv2.imshow('Laplacian Sharpened', laplacian_sharpened)
#cv2.imshow('Laplacian Sharpened', laplacian_sharpened_two)
cv2.waitKey(0)
cv2.destroyAllWindows()

