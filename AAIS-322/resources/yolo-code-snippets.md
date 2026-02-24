
# 🟢 Beginner-Level Coding Demos

These are easy wins that make students feel powerful.

---

## 1️⃣ Count Objects in an Image

Instead of just detecting, count.

Example:

* How many cars?
* How many people?
* How many traffic lights?

```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("street.jpg")[0]

counts = {}

for box in results.boxes:
    label = results.names[int(box.cls[0])]
    counts[label] = counts.get(label, 0) + 1

print(counts)
```

💡 Teaching moment:

* Dictionaries
* Looping over detections
* Data aggregation

---

## 2️⃣ Filter Specific Objects Only

Only show traffic lights:

```python
for box in results.boxes:
    label = results.names[int(box.cls[0])]
    if label == "traffic light":
        print("Traffic light detected!")
```

Teaches:

* Conditional logic
* Practical filtering

---

## 3️⃣ Change Confidence Threshold

```python
model.predict("street.jpg", conf=0.7)
```

Explain:

* Higher confidence → fewer false positives
* Lower confidence → more detections

This opens discussion about trade-offs.

---

# 🟡 Intermediate-Level Coding Demos

Now things get exciting.

---

## 4️⃣ Real-Time Webcam Detection

```python
model.predict(source=0, show=True)
```

Students LOVE this.

Now they see:

* Real-time AI
* Their own face detected as “person”

Teaching moment:

* Real-time systems
* Performance constraints

---

## 5️⃣ Draw Custom Boxes with OpenCV

Instead of using `.show()`, manually draw.

```python
import cv2

img = cv2.imread("street.jpg")

for box in results.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow("Custom Detection", img)
cv2.waitKey(0)
```

Now they understand:

* How bounding boxes are coordinates
* How AI integrates with standard computer vision tools

---

## 6️⃣ Crop Detected Objects

Extract each detected object as a new image.

```python
for i, box in enumerate(results.boxes):
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    crop = img[y1:y2, x1:x2]
    cv2.imwrite(f"object_{i}.jpg", crop)
```

Use case:

* Face extraction
* License plate extraction
* Medical tumor cropping

This feels advanced but is simple.

---

# 🔵 More Impressive Coding Ideas

These elevate your lecture.

---

## 7️⃣ Build a Simple "Smart Counter"

Example:

* Count how many people enter a frame.

Introduce:

* Frame-by-frame processing
* Simple tracking logic

This leads to surveillance and retail analytics discussions.

---

## 8️⃣ Detection + Decision Logic

Example:

```python
if counts.get("traffic light", 0) > 0:
    print("Prepare to slow down")
```

Now you're connecting:
Detection → Decision-making

This is where autonomous systems begin.

---

## 9️⃣ Build a Mini Project Idea

### Grocery Store Shelf Monitor

* Detect soda bottles
* Count inventory
* Print “Restock needed” if count < 5

### Parking Lot Monitor

* Detect cars
* Count empty spots

### Safety Helmet Detection

* Detect person
* Detect helmet
* Print warning if person detected without helmet

Students love these practical hooks.

---

# 🟣 Architecture-Level Things You Can Show

Since you teach AI systems, you can go deeper.

---

## 10️⃣ Show Detection as Part of a Pipeline

Explain:

Camera → Detection → Post-processing → Decision Engine → Action

Even draw:

```
Image → YOLO → Filter → Business Logic → Output
```

This shows real-world system design.

---

# 🔥 If You Want to Really Impress

You could show:

* Export YOLO to ONNX
* Run it in a Flask API
* Build a simple web app
* Or connect to a SwiftUI frontend (which fits your background perfectly)

Now students see:
AI is not isolated — it’s part of systems.

---

# 🧠 What I’d Recommend for Your Teaching Style

Since you’re strong in:

* Architecture
* Systems
* Real-world AI

I’d show:

1. Basic detection
2. Counting objects
3. Filtering logic
4. Decision-making example
5. Connect to autonomous vehicle or medical imaging

That gives:
Code + Systems Thinking

