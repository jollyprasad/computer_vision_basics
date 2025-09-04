import cv2
from ultralytics import YOLO

#model = YOLO("yolov8n.pt")

model = YOLO("yolo11n.pt")


image = cv2.imread("resources/person-image.jpg")
#image = cv2.imread("resources/fruits.jpg")

results = model(image)  

annotated_image = results[0].plot()  # Get the annotated image
cv2.imshow("Annotated Image", annotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()