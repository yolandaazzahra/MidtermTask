# -*- coding: utf-8 -*-
"""MidtermTask.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1G_RSK7QTI41mIzSrWZdt-IZA8PglO_3l

Nama : Yolanda Azzahra

NPM : 2306319514
"""

from google.colab import auth
auth.authenticate_user()

!git config --global user.name "yolandaazzahra"
!git config --global user.email "yolandaazzahra2906@gmail.com"

!git add MidtermTask.ipynb
!git commit -m "Update MidtermTask.ipynb"
!git push origin main

"""Installing Required Libraries"""

# Install YOLOv5 dependencies and OpenCV for video processing
!pip install torch torchvision torchaudio
!pip install opencv-python
!git clone https://github.com/ultralytics/yolov5  # Clone YOLOv5 repository
!pip install -r yolov5/requirements.txt  # Install YOLOv5 requirements

"""Uploading a Video File and Loading YOLOv5 Model"""

from google.colab import drive
import torch
import cv2

# Mount Google Drive to load video
drive.mount('/content/drive')

# Load YOLOv5 model (Pre-trained on COCO dataset)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Load video from Google Drive
video_path = '/content/drive/MyDrive/kucing oren.mp4'
cap = cv2.VideoCapture(video_path)

""" Detecting Objects Frame-by-Frame Using YOLOv5"""

import numpy as np  # Ensure numpy is imported
from google.colab.patches import cv2_imshow  # Import cv2_imshow for Colab

# Updated loop for displaying results in Google Colab
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection on the frame
    with torch.amp.autocast("cuda"):
        results = model(frame)

    # Display the results in Colab using cv2_imshow
    cv2_imshow(np.squeeze(results.render()))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()