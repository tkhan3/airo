import cv2
import matplotlib.pyplot as plt


def main():

    path = './images/apples.jpeg'
    input_image = cv2.imread(path, 1)

    # convert BGR to Gray for thresholding
    image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    thresh = 0
    max_val = 255

    ret1, output_bin_inv = cv2.threshold(image, thresh, max_val, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # convert GRAY to BGR for bitwise_and
    output_bin_inv = cv2.cvtColor(output_bin_inv, cv2.COLOR_GRAY2BGR)
    output_image = cv2.bitwise_and(input_image, output_bin_inv)

    # convert BGR to RGB for matplotlib
    output_image = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
    output = [input_image, output_bin_inv, output_image]

    titles = ['Original', 'Mask: ', 'Segmented: ']

    for i in range(len(output)):
        plt.subplot(1, 3, i + 1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()


if __name__ == "__main__":
    main()
