# Implement Contrast Stretching on an image

from PIL import Image
img=Image.open('cat_image.jpg')
width, height= img.size
pix=img.load()
l=(0.5)
m=2
n=(0.5)
intenA=50
intenB=200
v=(l*intenA)
w=(m*(intenB-intenA)+v)
for i in range(width):
  for j in range(height):
    r,g,b=pix[i,j]

    if r<=intenA:
      r=(int)(l*r)

    elif r<=intenB:
      r=(int)(m*(r-intenA)+v)

    else:
      r=(int)(n*(r-intenB)+w)
    
    if g<=intenA:
      g=(int)(l*g)

    elif g<=intenB:
      g=(int)(m*(g-intenA)+v)

    else:
      g=(int)(n*(g-intenB)+w)

    if b<=intenA:
      b=(int)(l*b)

    elif b<=intenB:
      b=(int)(m*(b-intenA)+v)

    else:
      b=(int)(n*(b-intenB)+w)
    pix[i,j]=(r,g,b)

img.save('catcontrast.jpg')
img1=Image.open('catcontrast.jpg')
# img1.show()
display(img1)
    

    

