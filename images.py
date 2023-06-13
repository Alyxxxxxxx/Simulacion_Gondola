from matplotlib import pyplot as plt
from skimage.io import imread
from skimage import transform


img = imread("parque.jpg")
plt.imshow(img,extent=(0,2,0,100))
plt.show()
