import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

image_path = "./new_cat.png"
image = cv.imread(image_path)
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

cv.imshow("cat",image_rgb)
# plt.show()
cv.waitKey(0)