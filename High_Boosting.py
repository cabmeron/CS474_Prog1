import cv2
import numpy as np

# Load the images 
lenna = cv2.imread('lenna.jpg', cv2.IMREAD_COLOR)
f_16 = cv2.imread('f_16.jpg', cv2.IMREAD_COLOR)

# Define the size of the Gaussian filter
k_size = (7, 7)

# Choose the enhancement factor (K) for high-boost filtering 
# I used 1,1.5,2 for first set of  k values
#set 3,2,3  for k values
# set 5,4,5 for k values
# set 7,4,5 for k values
K_values = [5, 4, 5]  # Experiment with different K values

for K in K_values:
    # Apply Gaussian blur to the images
    lenna_smoothed = cv2.GaussianBlur(lenna, k_size, 0)
    f_16_smoothed = cv2.GaussianBlur(f_16, k_size, 0)

    # Calculate the difference between the original and smoothed images
    lenna_difference = lenna - lenna_smoothed
    f_16_difference = f_16 - f_16_smoothed

    # Multiply the difference by the enhancement factor (K)
    lenna_enhanced = lenna + K * lenna_difference
    f_16_enhanced = f_16 + K * f_16_difference

    # Ensure pixel values are within the valid range [0, 255]
    lenna_enhanced = np.clip(lenna_enhanced, 0, 255).astype(np.uint8)
    f_16_enhanced = np.clip(f_16_enhanced, 0, 255).astype(np.uint8)

    # if both images do not display at the same time comment one out and repeat
    # Display or save the enhanced images
    cv2.imshow(f'Lenna Enhanced (K={K})', lenna_enhanced)
    cv2.imshow(f'F-16 Enhanced (K={K})', f_16_enhanced)
    cv2.waitKey(0)

# Close all open windows
cv2.destroyAllWindows()

