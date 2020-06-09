from PIL import Image
import cv2


im1 = Image.open('/home/martin/Documents/2020-01-28-043220_upscaled_image_x4.png')
im3 =im1.resize((1547, 873))
#1547
#873
im3.save('/home/martin/Pictures/2020-01-28-043220_upscaled_image_x4.png')


im2 = Image.open('/home/martin/Pictures/Screenshot from 2020-01-28 04-28-45.png')

im4 = im2.convert('RGB')
print(im3.mode,im2.mode)
im3 =Image.blend(im1,im4,0)

im3.save('veo')