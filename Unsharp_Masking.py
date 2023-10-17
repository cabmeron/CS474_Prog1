import cv2
import numpy as np

# Load the image
image = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)
image_2 = cv2.imread('f_16.jpg', cv2.IMREAD_COLOR)
# Define the size of the Gaussian filter
k_size = (7, 7)

# Apply Gaussian blur to the original image
smoothed_image = cv2.GaussianBlur(image, k_size, 0)

# Choose the enhancement factor (K)
K = 1  # for unsharp masking (K=1)
# K = 2  # for high-boost filtering (K>1)

# Calculate the difference between the original and smoothed image
difference = image - smoothed_image

# Multiply the difference by the enhancement factor (K)
enhanced_image = image + K * difference
enhanced_image_2 = image_2 + K * difference

# Ensure pixel values are within the valid range [0, 255]
enhanced_image = np.clip(enhanced_image, 0, 255).astype(np.uint8)

# If both  images do not display at the same time, comment one out
# Display the original and enhanced images
cv2.imshow('Original Image', image)
cv2.imshow('Enhanced Image', enhanced_image)
cv2.imshow('Original Image', image_2)
cv2.imshow('Enhanced Image', enhanced_image_2)
cv2.waitKey(0)
cv2.destroyAllWindows()


