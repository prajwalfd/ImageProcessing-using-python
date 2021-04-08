#Extract the Red Channel images from an image

from PIL import Image
img=Image.open('cat_image.jpg')
width, height= img.size
pix=img.load()
for i in range(width):
  for j in range(height):
    r,g,b=pix[i,j]
    pix[i,j]=(r,0,0)
img.save('catRed.jpg')
img1=Image.open('catRed.jpg')
# img1.show()
display(img1)


#Extract the Green Channel images from an image

from PIL import Image
img=Image.open('cat_image.jpg')
width, height= img.size
pix=img.load()
for i in range(width):
  for j in range(height):
    r,g,b=pix[i,j]
    pix[i,j]=(0,g,0)
img.save('catGreen.jpg')
img1=Image.open('catGreen.jpg')
# img1.show()
display(img1)


#Extract the Blue Channel images from an image

from PIL import Image
img=Image.open('cat_image.jpg')
width, height= img.size
pix=img.load()
for i in range(width):
  for j in range(height):
    r,g,b=pix[i,j]
    pix[i,j]=(0,0,b)
img.save('catBlue.jpg')
img1=Image.open('catBlue.jpg')
img1.show()
display(img1)
