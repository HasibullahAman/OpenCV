import numpy as np
from PIL import ImageOps
from PIL import Image
images = Image.open('../images/cat.png')
# images.show(images)

# convert the image to grayscale
image_to_gray =ImageOps.grayscale(images)
# image_to_gray.show()
print(image_to_gray.mode)
print(image_to_gray.format)
print(image_to_gray.width)
print(image_to_gray.height)