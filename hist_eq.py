import PIL
from PIL import Image
import numpy as np



def hist_eq(image, high=255):
    im = image
    if isinstance(im, PIL.Image.Image):
        im = np.array(image)
    
    if isinstance(im, (np.ndarray, np.generic)):
        for i in range(3):
            channel = im[:,:,i]
            hist, bins = np.histogram(channel,bins = np.arange(257))
            prob = (np.cumsum(hist))/(channel.shape[0]*channel.shape[1])
            new = prob*high
            mapping = lambda pix: new[int(pix)]
            im[:,:,i] = np.vectorize(mapping)(channel)
            
        
        return Image.fromarray(im.astype('uint8'))
    
    else :
        raise ValueError('Variable type not PIL Image or numpy array')