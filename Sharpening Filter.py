# Enhance an Image using a Sharpening Filter

from PIL import Image, ImageFilter 
im=Image.open('cat_image.jpg')
# im.show()
display(im) 
im1 = im.filter(ImageFilter.SHARPEN); 
im1.save('catSharp1.png') 
im2 = im1.filter(ImageFilter.SHARPEN); 
im2.save('catSharp2.png') 
im3=Image.open('catSharp1.png') 
im4=Image.open('catSharp2.png') 
# im3.show()
# im4.show()
display(im3)
display(im4)
