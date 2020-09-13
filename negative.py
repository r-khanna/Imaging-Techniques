import PIL
from PIL import Image
import numpy as np




def negative_im(image):
    "' Converts PIL Image or numpy array into its negative'"
    
    if isinstance(image, (np.ndarray, np.generic)):
        return Image.fromarray(255 - image) 
    
    if isinstance(image, PIL.Image.Image):
        return image.point(lambda pix: 255-pix)
    
    else :
        raise ValueError('Variable type not PIL Image or numpy array')