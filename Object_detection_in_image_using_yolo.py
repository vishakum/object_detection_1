from ultralytics import YOLO
import cv2

model=YOLO("images/yolov8l.pt")
results=model("Images/Screenshot 2024-11-08 155532.png",show=True)
cv2.waitKey(0)
