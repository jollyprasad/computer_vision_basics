import cv2
from ultralytics import YOLO

model = YOLO("yolo11n-pose.pt")

# for camera input
cap = cv2.VideoCapture(0)

# for video input
#cap = cv2.VideoCapture("resources/free-yoga-video-1.mp4")  # Replace "video.mp4" with your video file path

# Set desired width and height for display
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
cv2.namedWindow("Live Camera Feed", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live Camera Feed", DISPLAY_WIDTH, DISPLAY_HEIGHT)

while True:
    ret, frame = cap.read()
    results = model(frame)
    annotated_frame = results[0].plot()
    cv2.imshow("Live Camera Feed", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()