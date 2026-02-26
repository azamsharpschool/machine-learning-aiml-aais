
# Drawing Boxes in a Video Using YOLO 

[Traffic Car Video on YOLO](https://www.kaggle.com/code/kirollosashraf/traffic-car-video-using-yolo/input)

## 🟦 Code you provided

```python
from ultralytics import YOLO
import cv2
from google.colab.patches import cv2_imshow  # Colab helper

# Load pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("/content/sample_data/download.mp4")

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.25)
    annotated_frame = results[0].plot()

    # ✅ Use cv2_imshow instead of cv2.imshow in Colab
    cv2_imshow(annotated_frame)

    # To avoid dumping hundreds of frames into the notebook,
    # break after showing a few frames
    frame_count += 1
    if frame_count > 5:   # show only first 5 frames
        break

cap.release()
```

---

## 🟨 Step-by-step explanation

### 1. **Imports**

```python
from ultralytics import YOLO
import cv2
from google.colab.patches import cv2_imshow
```

* `ultralytics.YOLO`: gives you the YOLOv8 model class.
* `cv2`: OpenCV library for computer vision.
* `cv2_imshow`: Colab-safe replacement for `cv2.imshow`. In a notebook you can’t open GUI windows, so this displays images **inline**.

---

### 2. **Load YOLOv8 model**

```python
model = YOLO("yolov8n.pt")
```

* Loads the **nano version** of YOLOv8 (lightweight, fastest).
* `yolov8n.pt` is pre-trained on the **COCO dataset** → it can recognize 80 everyday objects (car, person, bus, traffic light, dog, etc.).
* On first use, weights are downloaded automatically.

---

### 3. **Open the video file**

```python
cap = cv2.VideoCapture("/content/sample_data/download.mp4")
```

* Creates a video capture object for your file.
* `cap.read()` will now give you one frame at a time.
* If the file path is wrong, `ret` will always be `False`.

---

### 4. **Loop through frames**

```python
while True:
    ret, frame = cap.read()
    if not ret:
        break
```

* Reads the **next frame** from the video.
* `ret = False` means end-of-video (or read error), so the loop ends.

---

### 5. **Run YOLO on each frame**

```python
results = model(frame, conf=0.25)
```

* Passes the frame into YOLO for object detection.
* `conf=0.25` means “only show objects with confidence ≥ 25%.”
* The model internally:

  * Resizes the frame,
  * Runs it through the YOLO neural net,
  * Applies non-max suppression (to avoid duplicate boxes).

---

### 6. **Draw detections**

```python
annotated_frame = results[0].plot()
```

* `results[0]`: detections for this frame.
* `.plot()` returns a new frame with **bounding boxes + labels + confidence scores** drawn on top.

---

### 7. **Display frame in Colab**

```python
cv2_imshow(annotated_frame)
```

* Shows the annotated frame inline in the notebook.
* If this were desktop Python, you’d use `cv2.imshow` in a pop-up window, but Colab doesn’t allow that.

---

### 8. **Limit number of frames shown**

```python
frame_count += 1
if frame_count > 5:
    break
```

* Stops after 5 frames to avoid spamming your notebook with hundreds of images.
* Otherwise, you’d see one inline image per frame until the video ended.

---

### 9. **Release resources**

```python
cap.release()
```

* Closes the video file.
* Always a good practice to free memory and file handles.

---

## 🟩 What this code is supposed to do

* Open your video (`download.mp4`).
* Run YOLOv8n object detection frame by frame.
* Draw boxes and labels on detected objects (cars, people, etc.).
* Display the **first 5 annotated frames inline** in Colab.
* Stop early (otherwise, showing every frame would overwhelm the notebook).

---

✅ **Summary:**
This script previews how YOLOv8 detects objects in a video. It doesn’t save or play the full annotated video — it just shows the first few frames inline for inspection.

