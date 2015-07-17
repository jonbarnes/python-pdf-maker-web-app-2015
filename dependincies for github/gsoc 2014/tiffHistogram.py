# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import Image



#import in BSE Tiff file
tiffFile = ('/home/jon/Desktop/gsoc2014/semData2014/CML0615(13).tif')
im = Image.open(tiffFile)
#
tiffSize = im.size
print tiffSize

#Convert Tiff into Numpy Array
imarray = np.array(im)
tiffShape = imarray.shape
print tiffShape


####Get histogram data on Numpy array

#run histogram on image
tiffHistogram = im.histogram()
print tiffHistogram

#Get X and Y values for Hist into Bar
tiffHistSize = np.size(tiffHistogram)
tiffHistBarXVal = range(tiffHistSize)
tiffHistBarYVal = tiffHistogram

#create bar graph
plt.bar(tiffHistBarXVal,tiffHistBarYVal)

#label bar graph
plt.ylabel('Counts')
plt.xlabel('keV Bucket via Grey Scale Value count from BSE Image')
plt.title('BSE Tiff Histogram')

#show bar graph
plt.show()


##Cropped Histogram, remove first 2 and last 2
#Get X and Y values for Hist into Bar
tiffHistBarXValCrop = tiffHistBarXVal[3:-3]
#del tiffHistBarXValCrop[0:1:-3]

tiffHistBarYValCrop = tiffHistBarYVal[3:-3]
#del tiffHistBarYValCrop[0:1:-3]

print tiffHistBarXValCrop
print tiffHistBarYValCrop

#X Value Max and Min
histXMin = np.min(tiffHistBarXValCrop)
histXMax = np.max(tiffHistBarXValCrop)
#Y Value Max 
#Y Value Min = 0 
histYMax = np.max(tiffHistBarYValCrop)

#create bar graph
plt.bar(tiffHistBarXValCrop,tiffHistBarYValCrop)

#label bar graph
plt.ylabel('Counts')
plt.xlabel('keV Bucket via Grey Scale Value count from BSE Image')
plt.title('BSE Tiff Histogram, first and last 3 removed')
plt.axis([histXMin, histXMax, 0, histYMax])

#savefig
plt.savefig('BSE Tiff Histogram, first and last 3 removed.png')

#show bar graph
plt.show()

