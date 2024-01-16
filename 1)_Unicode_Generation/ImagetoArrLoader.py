from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
from matplotlib import pyplot as plt

import os

def load_image(filename):
 # load the image
 img = load_img(filename, color_mode = "grayscale", target_size=(28, 28))
 # convert to array
 img = img_to_array(img)
 # reshape into a single sample with 1 channel
 img = img.reshape(28, 28)
 # prepare pixel data
 img = img.astype('float32')
 img = img / 255.0
 return img

print("Lib Imported!")

unicodes_data = []

count = 0;

for i in os.listdir('Images/'):
    if(count%1000 == 0):
        print(count," done")
    unicodes_data.append(load_image(f'Images/{i}'))
    count+=1

unicodes_data = np.array(unicodes_data)
np.save('../Assets/Unicode_Data.npy',unicodes_data)
print("done")
    
