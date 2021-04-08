#Read,Open, Write,Save and get dimensions (size) of an image

from google.colab.patches import cv2_imshow
from PIL import Image
img =Image.open('cat_image.jpg')
display(img)


################ to save image file ###################
from PIL import Image
img=Image.open('cat_image.jpg')
img.save('cat1.jpg') #image will be saved


################ to get dimensions ###################
from PIL import Image
img=Image.open('cat_image.jpg')
print("Image size is: ")
#print(img.size)
width, height= img.size
print('width: ',width)
print('Height: ',height)

# Insert your image and give path. I've used "cat_image.jpg" 

