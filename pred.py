from ultralytics import YOLO
from .csvpopulate import add_column_values as cp


model = YOLO("ashfbhjsgfj")

from .geot import get_geotag as gt
geotags = []
imgnames = []
import os
dirr = "/content/Predict"
for file in os.listdir(dirr):
  s = f'{dirr}/{file}'
  fName = f'{file}'
  print(s)
  model.predict(source = s, save=True, conf=0.35, line_width=3)
  latlong = gt(s)
  imgnames.append(fName)
  geotags.append(latlong)
  print(s,"_\-Done")

cp("geotegss.csv", "Geo_Tag_URL", imgnames)

