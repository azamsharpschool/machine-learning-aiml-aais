
# 🚦 Object Detection Walkthrough with YOLOv5

We’ll use a **pretrained YOLOv5s model** to detect objects in an image.

---

## ✅ Step 1: Clone the YOLOv5 Repository

```python
!git clone https://github.com/ultralytics/yolov5
```

* This downloads the official YOLOv5 repository from GitHub.
* It contains model definitions, training scripts, utils, and pretrained weights.
* Cloning ensures you get the latest version with everything bundled.

---

## ✅ Step 2: Navigate to YOLOv5 directory and install dependencies

```python
%cd yolov5
!pip install -r requirements.txt
```

* `%cd yolov5` changes your working directory to the cloned repo.
* `requirements.txt` lists all required Python libraries (like `opencv`, `pandas`, `matplotlib`, etc.).
* Installing them ensures YOLOv5 runs smoothly.

---

## ✅ Step 3: Import Required Libraries

```python
import torch
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
from IPython.display import display, Image
```

* **torch** → backbone deep learning framework (YOLOv5 uses PyTorch).
* **cv2 (OpenCV)** → handles image loading, color conversion, and drawing bounding boxes.
* **matplotlib** → displays images inside Colab.
* **IPython.display.Image** → alternative way to show images inline.

---

## ✅ Step 4: Load the YOLOv5 Pretrained Model

```python
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
```

* Uses `torch.hub` to download a pretrained YOLOv5 model.
* `'yolov5s'` = **YOLOv5 small** (fast, light, good for demo).
* Pretrained on **COCO dataset (80 common object classes)**.
* Other options: `'yolov5m'`, `'yolov5l'`, `'yolov5x'` (larger = more accurate, slower).

---

## ✅ Step 5: Load Your Image

```python
image_path = '/Users/azamsharp/Desktop/machine-learning/traffic-light.png'
image = cv2.imread(image_path)

plt.imshow(image)
plt.show()
```

* Loads the image from disk using OpenCV.
* Note: **OpenCV loads images in BGR format** (blue–green–red).
* That’s why the colors look strange unless we convert to RGB later.

---

## ✅ Step 6: Convert Image from BGR to RGB

```python
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
```

* Converts OpenCV’s BGR format → Matplotlib-friendly RGB format.
* Ensures colors are displayed correctly when plotting.

---

## ✅ Step 7: Perform Object Detection

```python
results = model(image_rgb)
```

* Feeds the image into YOLOv5.
* **YOLO outputs bounding boxes, class names, and confidence scores.**
* `results` contains everything in multiple formats (tensors, pandas, images).

---

## ✅ Step 8: Visualize Results with Bounding Boxes

```python
for _, row in results.pandas().xyxy[0].iterrows():
    # Draw rectangle (xmin, ymin, xmax, ymax)
    cv2.rectangle(
        image,
        (int(row['xmin']), int(row['ymin'])),
        (int(row['xmax']), int(row['ymax'])),
        (255, 0, 0), 2
    )
    # Add label text
    cv2.putText(
        image,
        row['name'],
        (int(row['xmin']), int(row['ymin'] - 10)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (255, 0, 0), 2
    )

# Convert back to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
plt.imshow(image_rgb)
plt.axis("off")
plt.show()
```

* **`results.pandas().xyxy[0]`** → gives a Pandas DataFrame with detections:

  * `xmin, ymin, xmax, ymax` = bounding box coordinates
  * `confidence` = detection confidence (0–1)
  * `class` = numeric ID
  * `name` = readable class name (e.g., "traffic light")
* We loop through each detection and draw rectangles + labels.
* Finally, we display the annotated image in RGB format.

---

# 🎯 What You Learned

* How to set up YOLOv5 in Colab/local
* How classification differs from detection (one label vs. multiple objects + boxes)
* How to run inference on an image and visualize results
* Why RGB/BGR conversion matters in OpenCV

