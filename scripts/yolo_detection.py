from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')

image_path = 'sample.jpg'

results = model(image_path)

for result in results:
    boxes = result.boxes
    for box in boxes:
        print('Objeto detectado:', box.cls)

annotated_frame = results[0].plot()
cv2.imwrite('results/detection_result.jpg', annotated_frame)

print('Detección finalizada')
