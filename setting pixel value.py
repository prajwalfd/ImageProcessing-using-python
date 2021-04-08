#Set pixel values in an image

from PIL import Image
img=Image.open('cat_image.jpg')
coord=x,y=100,100
print(img.getpixel(coord))
img.putpixel(coord,(0,0,0,255))
print(img.getpixel(coord))
