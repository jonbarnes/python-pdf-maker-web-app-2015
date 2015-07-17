# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

###############################################################################
# Import Libraries
import time as time
import numpy as np
import scipy as sp
import pylab as pl
import Image
#
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import Ward

# <codecell>

###############################################################################
# Get SEM Data
#
#get the file path
tifPath = '/home/jon/Desktop/gsoc2014/semImages/'
tifFile = 'CML0615(13).tif'
tifPathAndFile = tifPath + tifFile
#
#import in the tif
im = Image.open(tifPathAndFile)
im.show()

# <codecell>

###############################################################################
#Check out the shape and size of the tif
imarray = np.array(im)
#
print imarray.shape
  #(44, 330)
print im.size
  #(330, 44)

# <codecell>

###############################################################################
#crop the tiff
box=(50, 50, 200, 200)
#
im_crop=im.crop(box)
#
im_crop.show()

###############################################################################
#reassign im
im = im_crop
imarray = np.array(im)
#
print imarray.shape
#
print im.size

# <codecell>

###############################################################################
# Convert Tif into "LENA"
lena = im

# <codecell>

###############################################################################
# Show Tiff
pl.figure(figsize=(5, 5))
pl.imshow(lena, cmap=pl.cm.gray)

pl.xticks(())
pl.yticks(())
pl.show()

# <codecell>

###############################################################################
# Generate data
#lena = sp.misc.lena()
# Downsample the image by a factor of 4
#lena = lena[::2, ::2] + lena[1::2, ::2] + lena[::2, 1::2] + lena[1::2, 1::2]
#X = np.reshape(lena, (-1, 1))

# <codecell>

X = np.reshape(lena, (-1, 1))

# <codecell>

print imarray.shape

# <codecell>

###############################################################################
# Define the structure A of the data. Pixels connected to their neighbors.
connectivity = grid_to_graph(*imarray.shape)

# <codecell>

###############################################################################
# Compute clustering
print "Compute structured hierarchical clustering..."
#
st = time.time()
#
n_clusters = 5  # number of regions
#
ward = Ward(n_clusters=n_clusters, connectivity=connectivity).fit(X)
label = np.reshape(ward.labels_, imarray.shape)
#
print "Elaspsed time: ", time.time() - st
print "Number of pixels: ", label.size
print "Number of clusters: ", np.unique(label).size

# <codecell>

###############################################################################
# Plot the results on an image
pl.figure(figsize=(5, 5))
pl.imshow(lena, cmap=pl.cm.gray)
#
for l in range(n_clusters):
    pl.contour(label == l, contours=1,
            colors=[pl.cm.spectral(l / float(n_clusters)), ])
#
pl.xticks(())
pl.yticks(())
#
pl.show()

# <codecell>


