# OpenCV Learning & Practice

This repository contains my work while learning and practicing OpenCV.
It is structured into basics, advanced image processing, and face recognition.

This repo is meant for learning and reference. Each file focuses on a single concept so it’s easy to revisit later.

---

## Overview

This project covers core OpenCV concepts, starting from basic image operations and moving toward more advanced preprocessing techniques and a simple face recognition pipeline.

The focus is on understanding how things work rather than building a production-ready system.

---

## Folder Structure

```
├── 01basics
│   ├── 01read.py
│   ├── 02rescale.py
│   ├── 03rescale.py
│   ├── 04rescale.py
│   ├── 05draw.py
│   ├── 06draw.py
│   ├── 07draw_rectangle.py
│   ├── 08draw_circle.py
│   ├── 09draw_line.py
│   ├── 10write_text.py
│   ├── 11convert_to_grayscale.py
│   ├── 12blur.py
│   ├── 13edge_cascade.py
│   ├── 14dilating.py
│   ├── 15eroding.py
│   ├── 16resize.py
│   ├── 17cropping.py
│   ├── 18translation.py
│   ├── 19rotation.py
│   ├── 20Flipping.py
│   └── 21contours.py
│
├── 02advance
│   ├── 01color_space.py
│   ├── 02color_channels.py
│   ├── 03blurring_techniques.py
│   ├── 04bitwise_operations.py
│   ├── 05masking.py
│   ├── 06histogram.py
│   ├── 07thresholding.py
│   └── 08gradients.py
│
├── Faces
│   ├── train
│   │   ├── Ben Afflek
│   │   ├── Elton John
│   │   ├── Jerry Seinfield
│   │   ├── Madonna
│   │   └── Mindy Kaling
│   │
│   └── val
│       ├── ben_afflek
│       ├── elton_john
│       ├── jerry_seinfeld
│       ├── madonna
│       └── mindy_kaling
│
├── Photos
│   ├── cat.jpg
│   ├── cat_large.jpg
│   ├── cats.jpg
│   ├── cats 2.jpg
│   ├── group 1.jpg
│   ├── group 2.jpg
│   ├── lady.jpg
│   └── park.jpg
│
├── Videos
│   ├── dog.mp4
│   └── kitten.mp4
│
└── .gitignore
```

---

## What This Repo Covers

Basics:

- Reading images and videos
- Rescaling and resizing
- Drawing shapes and text
- Color conversion
- Blurring
- Edge detection
- Morphological operations
- Image transformations
- Contour detection

Advanced:

- Color spaces (BGR, RGB, HSV, LAB)
- Color channels
- Blurring techniques
- Bitwise operations
- Masking
- Histograms
- Thresholding
- Gradients

Face Recognition:

- Face detection using Haar Cascades
- Training an LBPH face recognizer
- Predicting faces on validation images
- Drawing bounding boxes and labels
- Working with confidence values

---

## Tech Stack

- Python
- OpenCV
- NumPy
- Matplotlib

---

## How to Run

Clone the repository:
git clone https://github.com/your-username/opencv-learning.git

Install dependencies:
pip install opencv-python opencv-contrib-python numpy matplotlib

Run any script:
python 01basics/21contours.py
python 02advance/06histogram.py
python Faces/recognize.py

Each script opens its own window to display output.

---

## Notes

- This repository is for learning and reference
- Code prioritizes clarity over optimization
- Some scripts reuse the same images for simplicity
- Face recognition accuracy depends on dataset quality

---

## Why This Repository

I created this repository to:

- Learn OpenCV fundamentals properly
- Experiment without overengineering
- Keep a structured reference for later
- Understand preprocessing before higher-level computer vision tasks

---

## License

This project is open source and available under the MIT License.
