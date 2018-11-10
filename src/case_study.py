# import the necessary packages
from PIL import Image
import pytesseract
import argparse
import cv2
import os
import json

# dir = "../graphics/bower_gabs/"
# images = os.listdir(dir)
#
# # image = cv2.imread(images[0])
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gabs = []
# for img in images:
#     text = pytesseract.image_to_string(Image.open(dir+images[0]))
#     gabs.append(text)
#
# fp2 = open('case_study.json', 'w')
# json.dump(gabs, fp2)
# fp2.close()
