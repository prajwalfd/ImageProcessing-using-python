# Create a new image by morphing 2 images

from PIL import Image
im1 = Image.open('Python.png').convert('L')
im1.save('logopythonconvert.jpg')
# im1.show()
display(im1) 
im2 = Image.open('cat_image.jpg').convert('L')
im3=im2.resize((180,180)) #both image size shold be same. cheak in image properties
im3.save('catresize.jpg')
# im3.show()
display(im3) 
im3 = Image.blend(im1, im3, 0.5)
im3.save('blend.jpg')
# im3.show()
display(im3) 
