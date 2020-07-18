import cv2


def display(window, image, x, y, w=600, h=600):
    cv2.namedWindow(window, cv2.WINDOW_NORMAL)
    cv2.moveWindow(window, x, y)
    cv2.resizeWindow(window, w, h)
    cv2.imshow(window, image)


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.flip(gray, 1)

        # Display the original frame
        display('Original', frame, 30, 100)

        # Display the gray scaled flipped image
        display('Gray Flipped', gray, 650, 100)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything's done, release the capture
    cap.release()
    cv2.destroyAllWindows()
