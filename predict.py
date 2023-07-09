from ultralytics import YOLO
model = YOLO('YOLO_Custom_v8m.pt')
model.predict(source=0, save=True, conf = 0.37, show = True)  # source=0 for capture from webcam/camera. Change value to the desired camera.