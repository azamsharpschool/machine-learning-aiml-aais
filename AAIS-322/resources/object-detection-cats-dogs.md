
# 🚀 **Detailed Walkthrough: Training and Running YOLOv8 Object Detection**

This guide walks you through the full lifecycle of training a YOLOv8 model—from installing dependencies, setting up your dataset, training the model, and finally running inference on a new image to extract the highest-confidence detection.

---

# ✅ **Step 1 — Install Ultralytics YOLO**

```python
!pip install ultralytics
```

YOLOv8 is provided by the **Ultralytics** library. The above command installs everything required to train and run YOLO models directly in Python (including inside Google Colab).

---

# ✅ **Step 2 — Define Your Dataset Paths**

```python
import os
from ultralytics import YOLO

ROOT_DIR = "/content/sample_data/train"
DATASET_DIR = "/content/sample_data/dataset.yaml"
```

* `ROOT_DIR`: Points to your *actual training images folder*.
* `DATASET_DIR`: Points to the `dataset.yaml` file that defines:

  * where your *train/val/test images* are located,
  * what *class names* the model should learn.

This YAML file is essential—YOLO uses it to understand the dataset structure.

---

# ✅ **Step 3 — Initialize the YOLOv8 Model**

```python
model = YOLO("yolov8n.yaml")
```

Here you create an instance of YOLO using the **YOLOv8n (nano)** architecture.

* `yolov8n.yaml` means you're starting **from scratch** with a small, fast model—great for learning and quick testing.

---

# ✅ **Step 4 — Train the Model**

```python
results = model.train(data=DATASET_DIR, epochs=20)
```

* `data=DATASET_DIR`: Tells YOLO where your dataset.yaml is.
* `epochs=20`: Number of training passes over the dataset.

During training, YOLO will automatically:

* Load your train/val images
* Train the model
* Evaluate accuracy on validation data
* Save outputs inside `runs/detect/trainX`

Each training run gets its own folder: `train`, `train2`, `train3`, etc.

Inside that folder:

* `weights/best.pt` = the best-performing model checkpoint
* `results.png` = loss curves
* Labels and metrics

---

# ✅ **Step 5 — Load the Trained Weights**

After training completes, load your best-performing model:

```python
model = YOLO("/content/runs/detect/train3/weights/best.pt")
```

Replace `train3` with the folder YOLO created for *your specific run*.

This loads the trained model so you can run predictions.

---

# ✅ **Step 6 — Choose an Image for Prediction**

```python
IMAGE_TO_BE_PREDICTED = "/content/sample_data/cat.png"
```

This is the input image you want YOLO to analyze.

---

# ✅ **Step 7 — Run Inference on the Image**

```python
results = model.predict(
    source=IMAGE_TO_BE_PREDICTED,
    conf=0.009,
    imgsz=640,
    save=True
)
```

Parameters:

* **`source`**: path to an image or directory
* **`conf=0.009`**: minimum confidence threshold
* **`imgsz=640`**: YOLO will resize input image to 640×640
* **`save=True`**: YOLO writes an output image with boxes drawn

YOLO returns a list of prediction results. Since we're predicting a single image:

```python
r = results[0]
```

---

# ✅ **Step 8 — Extract the Highest Confidence Box**

```python
if len(r.boxes) > 0:
    best = max(r.boxes, key=lambda b: float(b.conf[0]))
    cls_id = int(best.cls[0])
    conf = float(best.conf[0])
    label = model.names[cls_id]
    xyxy = best.xyxy[0].tolist()
```

Here's what each part does:

* `r.boxes`: all detected bounding boxes
* `max(..., key=lambda ...)`: find the highest-confidence prediction
* `best.cls[0]`: class index (e.g., 0 = cat, 1 = dog)
* `model.names`: maps numeric class → actual label from dataset.yaml
* `best.xyxy`: bounding box coordinates `[x1, y1, x2, y2]`

Finally:

```python
print(f"Highest confidence → Label: {label}, Confidence: {conf:.2f}, BBox: {xyxy}")
```

If no predictions were found:

```python
else:
    print("No objects detected.")
```

---

# ✅ **Step 9 — Print All Predictions**

```python
r = results[0]
print(r.boxes)
```

This shows raw bounding box objects (debug view).

Loop through each detected box:

```python
for box in r.boxes:
    cls_id = int(box.cls[0])
    conf = float(box.conf[0])
    label = model.names[cls_id]

    print(f"Label: {label}, Confidence: {conf:.2f}")
```

This prints a clean summary of all predictions in the image.

---

# 🎉 **Summary of the Workflow**

| Step                 | Purpose                                     |
| -------------------- | ------------------------------------------- |
| Install YOLO         | `pip install ultralytics`                   |
| Define dataset paths | Tell YOLO where your images + YAML file are |
| Initialize YOLO      | Choose your model architecture              |
| Train                | `model.train(...)` trains the model         |
| Load weights         | Use best checkpoint after training          |
| Predict              | Run inference on new images                 |
| Extract results      | Print highest-confidence detection          |
| Print all detections | View full prediction summary                |

---

