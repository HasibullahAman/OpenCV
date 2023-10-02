import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageOps

image = Image.open("../images/lenna.png")
image.quantize(20)
image.show()

# image_gray = ImageOps.grayscale(image)
# image_gray.show()
# plt.imshow(image)
print(image.format)
print(image.size)
print(image.mode)

# image_gray.save('baboon2.jpg')

