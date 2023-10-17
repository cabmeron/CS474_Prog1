import cv2
import numpy as np

# Define averaging filters
avg_filter_7x7 = np.ones((7, 7), np.float32) / 49.0
avg_filter_15x15 = np.ones((15, 15), np.float32) / 225.0

# Define Gaussian filters
gaussian_filter_7x7 = np.array([
    [1, 6, 15, 20, 15, 6, 1],
    [6, 36, 90, 120, 90, 36, 6],
    [15, 90, 225, 300, 225, 90, 15],
    [20, 120, 300, 400, 300, 120, 20],
    [15, 90, 225, 300, 225, 90, 15],
    [6, 36, 90, 120, 90, 36, 6],
    [1, 6, 15, 20, 15, 6, 1]
], np.float32) / 4900.0

gaussian_filter_15x15 = np.ones((15, 15), np.float32)  # Add your 15x15 Gaussian mask values here
gaussian_filter_15x15 = gaussian_filter_15x15 / np.sum(gaussian_filter_15x15)  # Normalize

# Read the images
lenna_img = cv2.imread('lenna.jpg', cv2.IMREAD_GRAYSCALE)
sf_img = cv2.imread('sf.jpg', cv2.IMREAD_GRAYSCALE)

# Apply 7x7 averaging filter
lenna_avg_7x7 = cv2.filter2D(lenna_img, -1, avg_filter_7x7)
sf_avg_7x7 = cv2.filter2D(sf_img, -1, avg_filter_7x7)

# Apply 15x15 averaging filter
lenna_avg_15x15 = cv2.filter2D(lenna_img, -1, avg_filter_15x15)
sf_avg_15x15 = cv2.filter2D(sf_img, -1, avg_filter_15x15)

# Apply 7x7 Gaussian filter
lenna_gaussian_7x7 = cv2.filter2D(lenna_img, -1, gaussian_filter_7x7)
sf_gaussian_7x7 = cv2.filter2D(sf_img, -1, gaussian_filter_7x7)

# Apply 15x15 Gaussian filter
lenna_gaussian_15x15 = cv2.filter2D(lenna_img, -1, gaussian_filter_15x15)
sf_gaussian_15x15 = cv2.filter2D(sf_img, -1, gaussian_filter_15x15)

# If both  images do not display at the same time, comment one out
# Display the original and enhanced images
cv2.imshow('Original Image',lenna_img )
cv2.imshow('Original Image',sf_img )
cv2.imshow('Enhanced Image with Gaussion 7x7 Mask', lenna_avg_7x7)
cv2.imshow('Enhanced Image with Gaussion 15x15 Mask', lenna_avg_15x15)
cv2.imshow('Enhanced Image with Gaussion 7x7 Mask', sf_avg_7x7 )
cv2.imshow('Enhanced Imagewith Gaussion 15x15 Mask', sf_avg_15x15 )
cv2.waitKey(0)
cv2.destroyAllWindows()
