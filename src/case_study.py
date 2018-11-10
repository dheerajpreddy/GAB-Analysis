# import the necessary packages
# from PIL import Image
# import pytesseract
# import argparse
# import cv2
# import os
import json
from hatesonar import Sonar

# dir = "../graphics/bower_gabs/"
# images = os.listdir(dir)
#
# # image = cv2.imread(images[0])
# # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# gabs = []
# for img in images:
#     text = pytesseract.image_to_string(Image.open(dir+img))
#     gabs.append(text)
#
# fp2 = open('case_study.json', 'w')
# json.dump(gabs, fp2)
# fp2.close()

with open('case_study.json', 'r') as fp:
    gabs = json.load(fp)

sonar = Sonar()
responses = []

for i in range(len(gabs)):
    responses.append(sonar.ping(text=gabs[i]))
    # print(sonar.ping(text=gabs[i]))
    # break

fp2 = open('case_study_sonar.json', 'w')
json.dump(responses, fp2)
fp2.close()
