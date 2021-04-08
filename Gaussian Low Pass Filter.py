# Implement Image Blurring using Gaussian Low Pass Filter

from PIL import Image, ImageFilter 
img=Image.open('cat_image.jpg')
img=img.filter(ImageFilter.GaussianBlur)
img.save('catGaussianBlur.png') 
# img.show()
display(img)
