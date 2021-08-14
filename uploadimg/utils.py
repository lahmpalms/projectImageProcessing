from django.db import models
from itertools import count
import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape
from numpy.lib.type_check import _imag_dispatcher, imag
from skimage import data
from skimage.morphology.grey import closing, white_tophat
from skimage.util import img_as_ubyte
from skimage import io
from skimage.morphology import erosion, dilation, opening, closing, white_tophat
from skimage.morphology import black_tophat, skeletonize, convex_hull_image
from skimage.morphology import disk
from PIL import Image



def plot_comparison(original, filtered, filter_name):
        fig, (ax1, ax2) = plt.subplots(ncols=2, figsize = (8, 4), sharex = True, sharey=True)
        ax1.imshow(original, cmap = plt.cm.gray)
        ax1.set_title('original')
        ax1.axis('off')
        ax2.imshow(filtered, cmap = plt.cm.gray)
        ax2.set_title(filter_name)
        ax2.axis('off')

        return
def cvtImage(image) :
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  #np.ascontiguousarray(image)
        lower_blue = np.array([110, 50, 50])
        upper_blue = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        return mask

def bitwise(mask, frame):
        res = cv2.bitwise_and( frame, frame, mask=mask )

        return res

def calPixelWhite(hull1):
        count_white = np.sum(hull1 == 1)

        return (count_white)
def Calculate(image):
        image= cv2.imread(image)
        image = np.asarray(image)#np.full((100,80,3), 12, np.uint8)  #overload because np.array
        frame = image
        mask = cvtImage(image)
        res = bitwise(mask, frame)
        hourse = cv2.subtract(255, mask)
        hull1 = convex_hull_image(hourse == 0)
        value = calPixelWhite(hull1)


        return value



