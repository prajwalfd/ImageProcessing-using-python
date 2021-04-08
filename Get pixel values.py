#Get pixel values in an image (method1)
from PIL import Image
img=Image.open('cat_image.jpg')
coord=x,y=100,100
print(img.getpixel(coord))
