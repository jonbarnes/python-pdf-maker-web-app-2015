# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

####################
#PY File for Mineral Boundry ID Based on BSE Image
#Created by Jon Barnes
#Last Modified: 19 June 2014
#This is Open Source Software
#
#These functions help to build the Images 
#for the PDF File of BSE Anaylsis
############
#
#
#
######List of Functions Included
#
#
#def mineralGroupID(NumberOfClusters)
####Does many things;
# 1)Output: Show the snipet of the BSE Image
# 2)internal thinking: Mineral Boundry ID Based on BSE Image
# 3)Output: Show Contours of Mineral Boundry
# 4)Output: Show a shaded picture for the Mineral Groups
# 5)Output: Output to TXT file the arrays for Label and BSE values of Snipet
#
# 6)Then it shifts gears and creates histograms and scatterplots about the data
######List of Functions Included
#
###Create a Scatter plot for range of BSE Values FOR Mineral ID 
#def mineralBSEScatter(GraphName)
#
###Create a Histogram of the BSE Grey Scale Values
###Histogram of BSE Values for Full Image
#def bseHistFull(GraphName)
###Histogram for the Cropped BSE Image
#def bseHistCrop(GraphName)
####################




def mineralGroupIDMultiBox(SuperBox, NumberOfClusters, BoxIDNumber):
    
    ######Step 1 - Import Libraries
    # Import Libraries
    import time as time
    import numpy as np
    import scipy as sp
    import pylab as pl
    import Image
    #
    from sklearn.feature_extraction.image import grid_to_graph
    from sklearn.cluster import Ward
    #

    
    
    ######Step 2 - Import in Data
    # Get SEM BSE Tiff Data
    #tiffFile = ('/home/jon/Desktop/gsoc2014/semData2014/CML0615(13).tif')
    #imFull  = Image.open(tiffFile)
    #
    # Get the file path
    tifPath = '/home/jon/Desktop/gsoc2014/semData2014/'
    tifFile = 'CML0615(13).tif'
    tifPathAndFile = tifPath + tifFile
    imFull = Image.open(tifPathAndFile)
    

    
    ###crop the tiff
    #Crop the imFull image by the Box
    im_crop = imFull.crop(SuperBox)

    
    #Convert the Crop Im into an Array
    im = im_crop
    imarray = np.array(im)
    
    
    
    
    ########Step 3 - Do  Mineral Grain Boundry ID
    #Have to do this, not sure why
    X = np.reshape(im, (-1, 1))

    # Define the structure A of the data. Pixels connected to their neighbors.
    connectivity = grid_to_graph(*imarray.shape)

    # Compute clustering
    print "Compute structured hierarchical clustering..."
    #
    st = time.time()
    #
    n_clusters = NumberOfClusters  # number of regions
    #
    ward = Ward(n_clusters=n_clusters, connectivity=connectivity).fit(X)
    label = np.reshape(ward.labels_, imarray.shape)

    
    
    
    
    
    
    ##########Step 4 - Path and File Ext of what to Save
    # Path names for images
    #
    #saved file path
    figurePath = '/home/jon/Desktop/figuresOfMany/'
    #saved file ext
    figureExt = '.png'

    
    
    
    
    
    ######Step 5 - Make Plots/Figures of Results
    ##A) Creates Following Figures
    # 1) Picture of Cropped BSE in GreyScale
    # 2) Histogram of BSE values for Cropped area
    # 3) Plot the contour results of image
    # 4) Plot the reasign grain results of image
    # 5) NEED TO MAKE SCATTER PLOT of Mineral Grain Size !!!!!!!!!
    # 6) Scatter Plot of BSE Values for each Mineral group
    #
    # B)Export the data to TXT
    # 1)Export Label and BSE Value to TXT
    
    ############
    # Plot the crop bse image
    pl.figure(figsize=(5, 5))
    pl.imshow(im, cmap=pl.cm.gray)
    #
    pl.xticks(())
    pl.yticks(())
    #
    #saved file name
    figureNameContour = 'croppedBSEimage'
    #
    #saved path and file and ext
    figurePathNameContourExt = figurePath + figureNameContour + str(BoxIDNumber) + figureExt
    #
    pl.savefig(figurePathNameContourExt)
    #
    pl.show()
    ###########

    
    ##################
    ###Histogram of BSE values for Cropped area  
    #########
    #run histogram on image
    tiffHistogram = im.histogram()

    #Get X and Y values for Hist into Bar
    tiffHistSize = np.size(tiffHistogram)
    #
    tiffHistBarXVal = range(tiffHistSize)
    tiffHistBarYVal = tiffHistogram

    #create bar graph
    pl.bar(tiffHistBarXVal,tiffHistBarYVal)

    #label bar graph
    pl.ylabel('Counts')
    pl.xlabel('keV Bucket via Grey Scale Value count from BSE Image')

    #saved file name
    figureNameShade = 'testShade'
    #
    #saved path and file and ext
    figurePathNameShadeExt = figurePath + figureNameShade + str(BoxIDNumber) +  figureExt
    #
    pl.savefig(figurePathNameShadeExt)

    #show bar graph
    plt.show()
    ##################
    
    

    ##############
    # Plot the contour results of image
    pl.figure(figsize=(5, 5))
    pl.imshow(im, cmap=pl.cm.gray)
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
    figurePathNameContourExt = figurePath + figureNameContour + str(BoxIDNumber) + figureExt
    #
    pl.savefig(figurePathNameContourExt)
    #
    pl.show()
    ##############


    ##################
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
    figurePathNameShadeExt = figurePath + figureNameShade + str(BoxIDNumber) +  figureExt
    #
    pl.savefig(figurePathNameShadeExt)
    pl.show()
    ##################
 
    
    
    ####################################
    ##Scatter Plot of BSE Values for each Mineral group
    ##################
    #Resize Arrays into 1D, so can combine
    labelArrayReshape = np.reshape(label, (62500) )
    imarrayArrayReshape = np.reshape(imarray, (62500) )
    #
    x = labelArrayReshape
    y = imarrayArrayReshape
    #
    pl.figure();
    #
    pl.scatter(x, y)
    #
    pl.ylabel('Pixel Counts')
    pl.xlabel('Mineral ID Number')
    #
    #saved file name
    figureNameShade = 'mineralPixelSize'
    #
    #saved path and file and ext
    figurePathNameShadeExt = figurePath + figureNameShade + str(BoxIDNumber) +  figureExt
    #
    pl.show()
    ####################################
    
    
    

    ####################################
    ##Scatter Plot of BSE Values for each Mineral group
    ##################
    #Resize Arrays into 1D, so can combine
    labelArrayReshape = np.reshape(label, (62500) )
    imarrayArrayReshape = np.reshape(imarray, (62500) )
    #
    x = labelArrayReshape
    y = imarrayArrayReshape
    #
    pl.figure();
    #
    pl.scatter(x, y)
    #
    pl.axis([0, 200, 0, 300])
    #
    pl.ylabel('BSE 256 Values')
    pl.xlabel('Mineral ID Number')
    #
    #saved file name
    figureNameShade = 'mineralBSEValues'
    #
    #saved path and file and ext
    figurePathNameShadeExt = figurePath + figureNameShade + str(BoxIDNumber) +  figureExt
    #
    pl.show()
    ####################################

    
    

    
    
    #####Step 6 - Save Arrays of Mineral ID and BSE Shade Value to TXT File
    np.savetxt(figurePath + 'labelTest' + str(BoxIDNumber) + '.txt', label)
    np.savetxt(figurePath + 'imarrayTest' + str(BoxIDNumber) + '.txt', imarray)
    

    
####################
####################
####################
####################
#Switching over to histograms and scatterplots
####################
####################
####################
####################
    


def mineralBSEScatter(GraphName):
    
    #Import in Libraries
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    #Import in Arrays from exported TXT files
    labelArray = np.loadtxt( '/home/jon/Desktop/labelTest.txt' , dtype='float', delimiter=None,)
    imarrayArray = np.loadtxt( '/home/jon/Desktop/imarrayTest.txt' , dtype='float', delimiter=None,)
    #
    #Resize Arrays into 1D, so can combine
    labelArrayReshape = np.reshape(labelArray, (62500) )
    imarrayArrayReshape = np.reshape(imarrayArray, (62500) )
    #
    x = labelArrayReshape
    y = imarrayArrayReshape
    #
    plt.figure();
    #
    plt.scatter(x, y)
    #
    plt.axis([0, 200, 0, 300])
    #
    plt.ylabel('BSE 256 Values')
    plt.xlabel('Mineral ID Number')
    plt.title(GraphName)
    #
    plt.savefig( GraphName + '.png' )
    #
    plt.show()
    #
    return




def bseHistFull(GraphName):
    #Import Libraries
    import numpy as np
    import matplotlib.pyplot as plt
    import Image
    #
    #
    # Get SEM BSE Tiff Data
    tiffFile = ('/home/jon/Desktop/gsoc2014/semData2014/CML0615(13).tif')
    imFull  = Image.open(tiffFile)
    #
    
    #########
    #run histogram on image
    tiffHistogram = imFull.histogram()

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
    plt.title(GraphName)


    plt.savefig( GraphName + '.png')

    #show bar graph
    plt.show()
    
    return


# <codecell>

####################
####################
#Run the function for Multiple Boxes
#
####Create the Boxes to move through the Image

#Create variables for the box, and the array of different box values
box = (0,0,0,0)
boxArray = [0]*16

#Create index for moving through the boxArray
index = 0

for y in range(4):
    for x in range(4):
        box = (x*250, y*250, 250 + x*250, 250 + y*250)
        boxArray[index] = box 
        index += 1
        #print box    

#Step through through the Boxes
for index in range(16):
    mineralGroupIDMultiBox( boxArray[index] ,200, index)
####################
####################

