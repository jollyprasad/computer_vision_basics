import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture("resources/traffic.mp4")  # Replace "video.mp4" with your video file path

model = YOLO("yolov8n.pt")  # Load the YOLOv8 model

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()  # Get the annotated frame

    # Resize the frame to fit the screen (e.g., 800x600)
    resized_frame = cv2.resize(annotated_frame, (800, 600))

    cv2.imshow("Video Object Detection", resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
    # Process results (e.g., draw bounding boxes)

cap.release()
cv2.destroyAllWindows()