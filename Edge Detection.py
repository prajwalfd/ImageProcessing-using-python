# Implement Edge Detection in an image

from PIL import Image, ImageFilter
im = Image.open('cat_image.jpg')
# im.show()
display(im) 
# Input image must be of mode = Greyscale (L) for edge detection
im1 = im.convert("L")
im1.save('catGrey.jpg')
# im1.show()
display(im1) 

im2 = im1.filter(ImageFilter.FIND_EDGES)
im2.save('Edge.jpg')
# im2.show()
display(im2) 
