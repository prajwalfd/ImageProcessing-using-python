# Implement Intensity Slicing with and without background on an image

from PIL import Image
img=Image.open('cat_image.jpg')
#img.show()
width, height= img.size
pix=img.load()
intenA=50
intenB=150
for i in range(width):
  for j in range(height):
    r,g,b=pix[i,j]
    if((intenA<=r and r<=intenB)or (intenA<=g and g<=intenB)or(intenA<=b and b<=intenB)):
      r=g=b=255
    else:
      r=r
      g=g
      b=b
    pix[i,j]=(r,g,b)

img.save('catslicing2.jpg')
img1=Image.open('catslicing2.jpg')
# img1.show()
display(img1)
    

    

