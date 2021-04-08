# convert a color image to grayscale (method 1)
from PIL import Image
img=Image.open('cat_image.jpg')
width, height= img.size
pix=img.load()
for i in range(width):
  for j in range(height):
    r,g,b=pix[i,j]
    gray=(r+g+b)/3
    pix[i,j]=(int(gray), int(gray), int(gray))
img.save('catGrayImg.jpg')
img1=Image.open('catGrayImg.jpg')
# img1.show()
display(img1)


# convert a color image to grayscale (method 2)

from PIL import Image
img=Image.open('cat_image.jpg')
width, height= img.size
pix=img.load()
for i in range(width):
  for j in range(height):
    r,g,b=pix[i,j]
    gray=(r*0.299)+(g*0.587)+(b*0.114)
    pix[i,j]=(int(gray), int(gray), int(gray))
img.save('catGrayImg2.jpg')
img1=Image.open('catGrayImg2.jpg')
# img1.show()
display(img1)
