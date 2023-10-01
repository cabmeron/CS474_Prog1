# resource used: geeksforgeeks

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the source and target images
# also used with the other images
source_image = cv2.imread('boat.pgm', cv2.IMREAD_GRAYSCALE)
target_image = cv2.imread('sf.pgm', cv2.IMREAD_GRAYSCALE)

# Calculate histograms of the source and target images
source_hist = cv2.calcHist([source_image], [0], None, [256], [0, 256])
target_hist = cv2.calcHist([target_image], [0], None, [256], [0, 256])

# Normalize the histograms to have values between 0 and 1
source_hist /= source_hist.sum()
target_hist /= target_hist.sum()

# Calculate cumulative distribution functions (CDFs) of the histograms
source_cdf = np.cumsum(source_hist)
target_cdf = np.cumsum(target_hist)

# Initialize a mapping function to map source CDF to target CDF
mapping = np.interp(source_cdf, target_cdf, range(256))

# Apply the mapping to the source image
matched_image = mapping[source_image]

# Convert the result to uint8 format
matched_image = matched_image.astype(np.uint8)

# Display the original source, target, and matched images
plt.figure(figsize=(12, 4))
plt.subplot(131), plt.imshow(source_image, cmap='gray'), plt.title('Source Image')
plt.subplot(132), plt.imshow(target_image, cmap='gray'), plt.title('Target Image')
plt.subplot(133), plt.imshow(matched_image, cmap='gray'), plt.title('Matched Image')
plt.show()
  
