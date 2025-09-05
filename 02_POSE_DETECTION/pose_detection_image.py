from ultralytics import YOLO
import cv2
model = YOLO("yolo11n-pose.pt")

image = cv2.imread("resources/person-image-2.jpg")

#image = cv2.imread("resources/2-person-image.jpg")

results = model(image)
annotated_image = results[0].plot()  # Get the annotated image

# Set desired width and height for display
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
cv2.namedWindow("Annotated Image", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Annotated Image", DISPLAY_WIDTH, DISPLAY_HEIGHT)


cv2.imshow("Annotated Image", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
