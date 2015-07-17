# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

# Import Libraries
import time as time
import numpy as np
import scipy as sp
import pylab as pl
import Image
#
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import Ward


# Get SEM BSE Tiff Data
tiffFile = ('/home/jon/Desktop/gsoc2014/semData2014/CML0615(13).tif')
im = Image.open(tiffFile)
im.show()


# Get SEM Data
#
#get the file path
#tifPath = '/home/jon/Desktop/gsoc2014/semImages/'
#tifFile = 'CML0615(13).tif'
#tifPathAndFile = tifPath + tifFile
#
#import in the tif
#imFull = Image.open(tifPathAndFile)
#imFull.show()

imFull  = Image.open(tiffFile)

[xmax, ymax] = imFull.size
print xmax
print ymax

#crop the tiff
#x1, y1, x2, y2
#starts in bottom left corner and works to upper right corner
#for starts x1 = 0 , y1 = 0  END xN = max, yN = max
#while x < xmax , while y < ymax ; increase x by 250, increase y by 250 For roughly 50 images
x1 = 0
y1 = 0
x2 = 250
y2 = 250
box=(x1, y1, x2, y2)
#
im_crop=imFull.crop(box)
#
im_crop.show()

#reassign im
im = im_crop
imarray = np.array(im)

# Convert Tif into "LENA"
lena = im

X = np.reshape(lena, (-1, 1))

# Define the structure A of the data. Pixels connected to their neighbors.
connectivity = grid_to_graph(*imarray.shape)

# Compute clustering
print "Compute structured hierarchical clustering..."
#
st = time.time()
#
n_clusters = 200  # number of regions
#
ward = Ward(n_clusters=n_clusters, connectivity=connectivity).fit(X)
label = np.reshape(ward.labels_, imarray.shape)

# Path names for images
#
#saved file path
figurePath = '/home/jon/Desktop/'
#saved file ext
figureExt = '.png'

############
# Plot the crop bse image
pl.figure(figsize=(5, 5))
pl.imshow(lena, cmap=pl.cm.gray)
#
pl.xticks(())
pl.yticks(())
#
#saved file name
figureNameContour = 'cropped bse image'
#
#saved path and file and ext
figurePathNameContourExt = figurePath + figureNameContour + figureExt
#
pl.savefig(figurePathNameContourExt)
#
pl.show()
###########


##############
# Plot the contour results of image
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
#saved file name
figureNameContour = 'testContour'
#
#saved path and file and ext
figurePathNameContourExt = figurePath + figureNameContour + figureExt
#
pl.savefig(figurePathNameContourExt)
#
pl.show()


######

# Plot the reasign grain results of image
pl.figure(figsize=(5, 5))
pl.imshow(label, cmap=pl.cm.gray)
#
pl.xticks(())
pl.yticks(())
#
#saved file name
figureNameShade = 'testShade'
#
#saved path and file and ext
figurePathNameShadeExt = figurePath + figureNameShade + figureExt
#
pl.savefig(figurePathNameShadeExt)
pl.show()

# <codecell>

import matplotlib.pyplot as plt

####Histogram of label
labelHist = np.histogram(label, bins = range(200) )
#print labelHist
#plt.hist(label)
#plt.show()

#Get X and Y values for Hist into Bar
#labelHistSize = np.size(labelHist)
labelHistBarXVal = labelHist[1]
labelHistBarYVal = labelHist[0]
#
labelHistBarXVal = labelHistBarXVal[1:]
#

plt.bar(labelHistBarXVal,labelHistBarYVal)

#label bar graph
plt.ylabel('Counts')
plt.xlabel('Mineral ID number')
plt.title('Pixel Size of Mineral Groups')


plt.savefig('pixelSizeOfMineralGroups.png')
#show bar graph
plt.show()

# <codecell>

#########
#run histogram on image
tiffHistogram = im.histogram()

#Get X and Y values for Hist into Bar
tiffHistSize = np.size(tiffHistogram)
#
tiffHistBarXVal = range(tiffHistSize)
tiffHistBarYVal = tiffHistogram

#create bar graph
plt.bar(tiffHistBarXVal,tiffHistBarYVal)

#label bar graph
plt.ylabel('Counts')
plt.xlabel('keV Bucket via Grey Scale Value count from BSE Image')
plt.title('BSE Tiff Histogram for Croped Area')


plt.savefig('bseDistOfCrop.png')

#show bar graph
plt.show()

# <codecell>

####Boxplot for BSE values for Mineral groups
from pylab import *


#####Convert fake data to real data!!!!!!!!!!!!!!
#use minearl Id numbers (label) and BSE 256 values (imarray)
#print label
#print imarray
#for each number in the 'label' have a list of 'imarray' values
#print np.shape(label)
#print np.shape(imarray)
#
labelReshape = np.reshape(label,(62500,1))
#print np.shape(labelReshape)
#
imarrayReshape = np.reshape(imarray,(62500,1))
#print np.shape(imarrayReshape)
#
labelBSEValue = np.column_stack( (labelReshape, imarrayReshape) )
#print labelBSEValue 
print np.shape(labelBSEValue)
#

###Create a 200 x 200 Matrix to fill with these values
zerosTwoHundredSquare = np.zeros( shape=(200,201) )
print np.shape(zerosTwoHundredSquare)
#
for i in range(200):
    zerosTwoHundredSquare[i,0] = i
#
print zerosTwoHundredSquare
#####

####
print '\n' + 'Line Break Between Empty Matrix and Filled' + '\n'
####

###Fill the 200x200 matrix with valus
#for i in range(np.size(labelBSEValue)):
# i is the row number of the 2D array
# j is the mineral ID number

counter = 1
for matrixCell in range(200):
   #counter = 1
   for mineralID in range(200):
        if labelBSEValue[matrixCell,0] == mineralID: 
            zerosTwoHundredSquare[mineralID,counter] = labelBSEValue[matrixCell,1]
            #
            #print counter
            counter += 1

print zerosTwoHundredSquare[198]

###Duplicate  zerosTwoHundredSquare to remove Zeros
noZeros = np.zeros( shape=(200,201) )
for arrayRow in range(200):
    noZeros[arrayRow] = zerosTwoHundredSquare[arrayRow]
print noZeros
#
#
#Convert from array to List
noZerosList = (0)*200
for arrayRow in range(200):
    noZerosList[arrayRow] = noZeros[arrayRow].tolist()
print noZerosList

# <markdowncell>

# for matrixCell in range(200):
#    for mineralID in range(200):
#         counter = 1
#         if labelBSEValue[matrixCell,0] == mineralID:
#             print 'mineral ID is ' + str( mineralID ) + ' and ' + 'BSE is ' + str( labelBSEValue[matrixCell,1] )
#             zerosTwoHundredSquare[mineralID,counter] = labelBSEValue[matrixCell,1]
#             counter += 1
#             
# print zerosTwoHundredSquare

# <codecell>

####
# fake up some data
spread= rand(50) * 100
center = ones(25) * 50
flier_high = rand(10) * 100 + 100
flier_low = rand(10) * -100
#
data =concatenate((spread, center, flier_high, flier_low), 0)
####

#####
#Fake data for multiple box plots
spread= rand(50) * 100
center = ones(25) * 40
flier_high = rand(10) * 100 + 100
flier_low = rand(10) * -100
d2 = concatenate( (spread, center, flier_high, flier_low), 0 )
data.shape = (-1, 1)
d2.shape = (-1, 1)
#
data = [data, d2, d2[::2,0]]
######

# basic plot
boxplot(data)

#label bar graph
plt.ylabel('BSE 256 Values')
plt.xlabel('Mineral ID Number')
plt.title('Boxplot of BSE values for Mineral Groups')


plt.savefig('Boxplot of BSE values for Mineral Groups.png')

#show bar graph
plt.show()

# <codecell>


