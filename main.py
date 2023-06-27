from ultralytics import YOLO
model = YOLO('yolov8m.pt')
model.train(data='custom_dtat.yaml', imgsz = 640, epochs = 50, workers = 4)