import cv2

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error: Cannot open video source.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Frame", frame)

    if cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
        break

    key = cv2.waitKey(20) & 0xFF

    if key == ord("q"):
        break

    if key == ord("a"):
        cv2.imwrite("image.png", frame)
        print("Image saved as 'image.png'")

        if cv2.getWindowProperty("Frame", cv2.WND_PROP_VISIBLE) < 1:
            break


cap.release()
cv2.destroyAllWindows()
