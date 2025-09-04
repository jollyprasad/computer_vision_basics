# Computer Vision — YOLOv8 Object Detection (User Manual)

This project contains three simple Python programs that run object detection with YOLOv8 using OpenCV:

- `simple_object_detection.py`: Detect objects in a single image and show an annotated window.
- `object_detection_from_video.py`: Detect objects from a video file (e.g., `traffic.mp4`).
- `live_camera_feed.py`: Detect objects from your live webcam feed.

A small YOLOv8 model file `yolov8n.pt` is included for quick tests.

## Prerequisites
- Python 3.8–3.12 on Windows
- A working webcam (for `live_camera_feed.py`)
- A video file (e.g., `traffic.mp4`) for `object_detection_from_video.py`


# 1) Install dependencies
```
pip install -r requirements.txt
```
This installs `ultralytics` (YOLOv8) and `opencv-python`.

# 2) Renaming and updating the environment file
Rename the environment files as ".env" from ".env.example" and enter your API_KEYS

## Files
- `simple_object_detection.py` — image inference script
- `object_detection_from_video.py` — video file inference script
- `live_camera_feed.py` — webcam/live camera inference script
- `yolov8n.pt` — YOLOv8n model weights
- `traffic.mp4` — example input video
- `person-image.jpg`, `fruits.jpg` — example images

## How to Run
Make sure your virtual environment is activated if you created one.

### 1) Single image
Run:
```powershell
python simple_object_detection.py
```
Defaults to `person-image.jpg`. To change the image, edit the script and set the file you want:
```python
image = cv2.imread("person-image.jpg")
# image = cv2.imread("fruits.jpg")
```
The program will open a window titled "Annotated Image". Press `q` or close the window to exit.

### 2) Video file
Run:
```powershell
python object_detection_from_video.py
```
- The script reads `traffic.mp4` by default:
  ```python
  cap = cv2.VideoCapture("traffic.mp4")
  ```
  Change the path to your own video file if needed.
- The annotated video is resized to 800×600 for display and shown in a window titled "Video Object Detection".
- Press `q` to quit.

### 3) Live camera
Run:
```powershell
python live_camera_feed.py
```
- Uses the default camera index `0`:
  ```python
  cap = cv2.VideoCapture(0)
  ```
  If you have multiple cameras or the default doesn’t work, try `1`, `2`, etc.
- A window titled "Live Camera Feed" will appear. Press `q` to quit.

## Switching models
`yolov8n.pt` is the small, fast model. You can switch to other YOLOv8 models (e.g., `yolov8s.pt`, `yolov8m.pt`) by placing the weights in the project folder and changing:
```python
model = YOLO("yolov8n.pt")
```

## Tips and Notes
- GPU (CUDA) is used automatically if available via PyTorch; otherwise, inference runs on CPU.
- Larger models may improve accuracy but will be slower.
- For best webcam performance, close other apps that use the camera.

## Troubleshooting
- Camera window is black or doesn’t open:
  - Another app may be using the camera. Close it and try again.
  - Try a different camera index: `cv2.VideoCapture(1)`.
  - Ensure Windows camera privacy permissions allow desktop apps.
- Video file won’t open:
  - Check the file path and file name in the script.
  - Try an absolute path like `C:\\path\\to\\your_video.mp4`.
- Module not found (e.g., cv2):
  - Reinstall dependencies: `pip install -r requirements.txt` (ensure your venv is active).
- Very slow on CPU:
  - Stick with `yolov8n.pt` (already the smallest model).
  - Close other CPU-intensive applications.

## Exit controls
- All programs use the same exit key: press `q` while the window is focused.

## License

This sample is intended for educational and demonstration purposes. 


