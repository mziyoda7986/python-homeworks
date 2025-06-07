import numpy as np
from PIL import Image

img_np = np.array(Image.open('birds.jpg'))

def flip_image(img):
    hor = np.fliplr(img)
    ver = np.flipud(img)
    return hor, ver

def add_noise(img, noise_lev=25):
    noise = np.random.randint(-noise_lev, noise_lev+1, img.shape, dtype='int16')
    noisy_img = img.astype('int16') + noise
    noisy_img = np.clip(noisy_img, 0, 255).astype('uint8')
    return noisy_img

def brighten_channels(img, value=40):
    bright_img = img.astype('int16') + value
    bright_img = np.clip(bright_img, 0, 255).astype('uint8')
    return bright_img


def apply_mask(img, x1=100, y1=100):
    masked_img = img.copy()
    y2, x2, _ = img.shape
    y = y2 // 2 - y1 // 2
    x = x2 // 2 - x1 // 2
    masked_img[y:y+y1, x:x+x1] = [0, 0, 0]  
    return masked_img

h, v = flip_image(img_np)
Image.fromarray(h).save('flipped_horizontal.jpg')
Image.fromarray(v).save('flipped_vertical.jpg')

noisy = add_noise(img_np, 60)
Image.fromarray(noisy).save('noisy.jpg')

bright = brighten_channels(img_np, 50)
Image.fromarray(bright).save('brightened.jpg')

masked = apply_mask(img_np, 200, 200)
Image.fromarray(masked).save('masked.jpg')