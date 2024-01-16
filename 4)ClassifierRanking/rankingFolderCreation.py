from PIL import Image
import numpy as np
# example of saving an image with the Keras API
from keras.preprocessing.image import load_img
from keras.preprocessing.image import save_img
from keras.preprocessing.image import img_to_array


final_ranking = np.load("../Assets/RankingEuclidean_FinalRankedUnic.npy",allow_pickle = True)
for i in range(len(final_ranking)):
    final_ranking[i][0] = final_ranking[i][0] * 255
    #print(final_ranking[i][0])
    
    if(final_ranking[i][2] == 0):
        filename = f'0/{i}.png'
    elif(final_ranking[i][2] == 1):
        filename = f'1/{i}.png'
    elif(final_ranking[i][2] == 2):
        filename = f'/2/{i}.png'
    elif(final_ranking[i][2] == 3):
        filename = f'3/{i}.png'
    elif(final_ranking[i][2] == 4):
        filename = f'4/{i}.png'
    elif(final_ranking[i][2] == 5):
        filename = f'5/{i}.png'
    elif(final_ranking[i][2] == 6):
        filename = f'6/{i}.png'
    elif(final_ranking[i][2] == 7):
        filename = f'7/{i}.png'
    elif(final_ranking[i][2] == 8):
        filename = f'8/{i}.png'
    elif(final_ranking[i][2] == 9):
        filename = f'9/{i}.png'

        
    save_img(filename, final_ranking[i][0].reshape(28,28,1))
