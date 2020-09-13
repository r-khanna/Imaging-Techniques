import PIL
from PIL import Image
import numpy as np


def contrast_stretch(image, low=0, high =255):
    "' Stretches pixel value range between low to high of a RGB PIL Image or numpy array '"
    "' Returns PIL Image object'"
    
    im = image
    if isinstance(im, PIL.Image.Image):
        im = np.array(image)
    
    if isinstance(im, (np.ndarray, np.generic)):
        im_ = np.zeros(im.shape)
        for i in range(3):
            im_min = im[:,:,i].min()
            im_max = im[:,:,i].max()

            im_[:,:,i] = ((im[:,:,i] - im_min)/(im_max - im_min))*(high - low) 

        return Image.fromarray(im_.astype(np.uint8))
    
    else :
        raise ValueError('Variable type not PIL Image or numpy array')