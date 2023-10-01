# source used: geeksforgeeks

import numpy as np

def quantize_image(image, levels):
    max_value = np.max(image)
    quantized_image = (image * (levels - 1) // max_value) * (255 // (levels - 1))
    return quantized_image

def read_pgm(filename):
    with open(filename, 'rb') as f:
        # Read the PGM header
        f.readline()  # Skip the PGM magic number
        dimensions = f.readline().decode().split()
        width, height = int(dimensions[0]), int(dimensions[1])
        max_value = int(f.readline().decode())

        # Read the image data
        image_data = np.fromfile(f, dtype=np.uint8, count=width * height, sep=' ')
        image = np.reshape(image_data, (height, width))
        return image

def write_pgm(filename, image):
    with open(filename, 'wb') as f:
        f.write(b'P5\n')
        f.write(f"{image.shape[1]} {image.shape[0]}\n".encode())
        f.write(b'255\n')
        image.tofile(f, sep=' ')

def main():
    input_images = ["lenna.pgm", "peppers.pgm"]
    output_levels = [128, 32, 8, 2]

    for input_image in input_images:
        image = read_pgm(input_image)
        for levels in output_levels:
            quantized_image = quantize_image(image, levels)
            output_filename = f"{input_image.split('.')[0]}_L{levels}.pgm"
            write_pgm(output_filename, quantized_image)

if __name__ == "__main__":
    main()
