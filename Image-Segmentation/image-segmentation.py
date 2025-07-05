import cv2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

file_path = 'landscape-test.jpg'
image = cv2.imread(filename=file_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pixels = image.reshape((-1, 3))

k = 4
kmeans = KMeans(n_clusters=k, random_state=24)
kmeans.fit(pixels)

segmented_image_gray = kmeans.cluster_centers_[kmeans.labels_]
segmented_image_gray = segmented_image_gray.reshape(image.shape).astype(np.uint8)

fig, axes = plt.subplots(1, 2)
axes[0].imshow(image)
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(segmented_image_gray)
axes[1].set_title(f'Segmented Image with {k=}')
axes[1].axis('off')

plt.show()