# googleimagesdownload -k "baseball game" -s medium -l 500 -o fastai/courses/dl1/data/baseballcricket -i 
# train/baseball -cd ~/chromedriver

# googleimagesdownload -k "baseball game" -s medium -wr '{"time_min":"09/01/2018","time_max":"09/30/2018"}'
#    -l 500 -o fastai/courses/dl1/data/baseballcricket -i train/baseball -cd ~/chromedriver

from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images



# import os
# from PIL import Image

# img_dir = r"path/to/downloads/directory"
# for filename in os.listdir(img_dir):
#     try :
#         with Image.open(img_dir + "/" + filename) as im:
#              print('ok')
#     except :
#         print(img_dir + "/" + filename)
#         os.remove(img_dir + "/" + filename)