import numpy as np
from PIL import Image
from PIL import ImageOps

# in bellow, we work to show how we can get a copy from an image and how it changes the id in memory
image = Image.open('../images/baboon.png')
image.show()
image_copy = image.copy()
print(id(image))
print(id(image_copy))

# flip and mirror the image
# how to flip the image
image_flip =ImageOps.flip(image)
image_flip.show()