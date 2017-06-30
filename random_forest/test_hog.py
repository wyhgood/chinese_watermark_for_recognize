import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

from skimage.feature import hog
from skimage import data, color, exposure



#tmp = data.astronaut()
im = Image.open('./target.jpg')
tmp = np.asarray(im)
image = color.rgb2gray(tmp)

print(type(tmp))
print(type(image))
print(len(image))


fd, hog_image = hog(image, orientations=9, pixels_per_cell=(16, 16),
                    cells_per_block=(3, 3), visualise=True)

print(hog_image.shape)
#print(hog_image[510])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Input image')
ax1.set_adjustable('box-forced')

# Rescale histogram for better display
hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 0.02))
print(type(hog_image_rescaled))

ax2.axis('off')
ax2.imshow(hog_image_rescaled, cmap=plt.cm.gray)
ax2.set_title('Histogram of Oriented Gradients')
ax1.set_adjustable('box-forced')
plt.show()
