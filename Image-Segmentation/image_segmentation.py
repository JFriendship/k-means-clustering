import cv2
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

def segment_image(file_name=None, k=4):
    if file_name:
        image = cv2.imread(filename='static/uploads/' + file_name)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pixels = image.reshape((-1, 3))

        kmeans = KMeans(n_clusters=k, random_state=24)
        kmeans.fit(pixels)

        segmented_image_gray = kmeans.cluster_centers_[kmeans.labels_]
        segmented_image_gray = segmented_image_gray.reshape(image.shape).astype(np.uint8)

        image = Image.fromarray(segmented_image_gray)
        image.save("static/processed/" + file_name)

        return True
    else:
        print('ERROR!')
        return False