import cv2
import matplotlib.pyplot as plt


def main():
    path = './images/cameraman.tiff'

    image = cv2.imread(path, 0)

    thresh = 0
    max_val = 255

    plt.hist(image.ravel(), 256, [0, 256]);
    plt.show()

    ret0, output_bin = cv2.threshold(image, thresh, max_val, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    ret1, output_bin_inv = cv2.threshold(image, thresh, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    ret2, output_to_zero = cv2.threshold(image, thresh, max_val, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
    ret3, output_to_zero_inv = cv2.threshold(image, thresh, max_val, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU)
    ret4, output_trunc = cv2.threshold(image, thresh, max_val, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)

    output = [image, output_bin, output_bin_inv, output_to_zero, output_to_zero_inv, output_trunc]

    titles = ['Original', 'Binary: ' + str(ret0), 'Binary Inv: ' + str(ret1),
              'Zero: ' + str(ret2), 'Zero Inv: ' + str(ret3), 'Trunc: ' + str(ret4)]

    for i in range(6):
        plt.subplot(2, 3, i + 1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
