from sklearn.cluster import KMeans
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
from typing import Dict,List

COLORS = {
    'RED':[255,0,0],
    'GREEN': [0, 128, 0],
    'BLUE': [0, 0, 255],
    'YELLOW': [255, 255, 0],
    "LIME":[0,255,0],
    'CYAN/AQUA':[0,225,225],
    'MAGENTA':[255,0,255],
    'SILVER':[192,192,192],
    'GRAY':[128,128,128],
    'MAROON':[128,0,0],
    'OLIVE':[128,128,0],
    'PURPLE':[128,0,128],
    'NAVY':[0,0,128],
    'WHITE':[255,255,255],
    'BLACK':[0,0,0]

}


def predictcolorlabels(img,box,corlor_rgb:Dict[str,List[int]]=COLORS,threshold=60,number_of_colors=8):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    image = img[int(box[1]):int(box[3]),int(box[0]):int(box[2])].copy()
    modified_image = image.reshape(image.shape[0]*image.shape[1], 3)

    clf = KMeans(n_clusters = number_of_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)
    counts = dict(sorted(counts.items()))

    center_colors = clf.cluster_centers_
    # ordered_colors = [center_colors[i] for i in counts.keys()]
    # rgb_colors = [center_colors[i] for i in counts.keys()]

    colors_in_image = {}
    for item,values in corlor_rgb.items():
        colors_CIE_lab = rgb2lab(np.uint8(np.asarray([[values]])))

        for i in range(number_of_colors):
            curr_color = rgb2lab(np.uint8(np.asarray([[center_colors[i]]])))
            diff = deltaE_cie76(colors_CIE_lab, curr_color)

            if diff < threshold:
                if colors_in_image.get(item):
                    colors_in_image[item] = min(colors_in_image[item],diff)
                else:
                    colors_in_image[item] = diff

    if len(colors_in_image):
        return min(colors_in_image,key=colors_in_image.get)
    else:
        return None
