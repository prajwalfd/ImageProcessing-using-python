# Get the Digital Negative of an image

from PIL import Image
img=Image.open('cat_image.jpg')
width, height= img.size
pix=img.load()
for i in range(width):
  for j in range(height):
    r,g,b=pix[i,j]
    pix[i,j]=(255-r,255-g,255-b)
img.save('catN.jpg')
img1=Image.open('catN.jpg')
# img1.show()
display(img1)
