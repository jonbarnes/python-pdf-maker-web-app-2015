
# coding: utf-8

# In[3]:

#Table of Contents

#Function 1
##Import in Image and Convert to Array

#Function 3
##Get subsection of Array

#Function 4
##ID grain boundries

#Function 5
#Make charts of grain boundries
##Make Countour Image, Make Label Image

#Function 6
##Get histograms for sizes of Grains

#Funtion  9
##Make PDF

#Function
##Go from importing image to making PDF

#Function 8
##mosaic across whole image


# In[22]:

#Function - Import in File and Convert to Array

def convertImageToArray(tifPath = '/home/jon/Desktop/gsoc2014/',tifFile = 'checkerboard.jpg'):

    # Import Libraries
    import Image

    global imageFileName
    imageFileName = tifFile
    
    #convert Path and File to one Link
    tifPathAndFile = tifPath + tifFile

    #Convert Image to Array
    global imFull
    imFull = Image.open(tifPathAndFile)
    print imFull


# In[23]:

convertImageToArray() 


# In[5]:

#Function - crop the tiff

def cropArray( cropBox = (0,0, 200,200) ,  saveFolder = '/home/jon/Desktop/gsoc2014/'):
    # Import Libraries
    import Image
    import numpy as np
    import pylab as pl

    global imFull
    arrayToCrop = imFull
    
    
    #grab imFull from Import Function

    #Crop the imFull image by the Box
    im_crop = arrayToCrop.crop(cropBox)

    #Convert the Crop Im into an Array
    global imarray
    imarray = np.array(im_crop)

    np.savetxt(saveFolder + 'imarrayCrop' + '.txt', imarray,  delimiter=" ", fmt="%s")
    #num.savetxt('test.txt', DAT, delimiter=" ", fmt="%s") 
    
    ############
    # Plot the crop bse image
    pl.figure(figsize=(5, 5))
    pl.imshow(imarray, cmap=pl.cm.gray)
    #
    pl.xticks(())
    pl.yticks(())
    #
    ##Save Image
    #croppedImage = 'croppedBSEimage'
    #
    #saved path and file and ext
    #figurePathNameContourExt = figurePath + figureNameContour + str(BoxIDNumber) + figureExt
    #
    #pl.savefig(figurePathNameContourExt)
    #
    pl.show()
    ###########


# In[5]:

cropArray() 


# In[6]:

#Grain Boundry function

def boundaryID( #arrayForBoundary = imarray , 
               numberOfGrains = 200 , 
               saveFolder = '/home/jon/Desktop/gsoc2014/'):

    # Import Libraries
    import time as time
    import numpy as np
    import scipy as sp
    import pylab as pl
    import Image
    
    import sklearn
    #
    from sklearn.feature_extraction.image import grid_to_graph
    from sklearn.cluster import Ward
    #
 
    global imarray
    
    #Main Inputs
    X = np.reshape(imarray, (-1, 1))
    global n_clusters
    n_clusters = numberOfGrains  # number of regions

    # Define the structure A of the data. Pixels connected to their neighbors.
    connectivity = grid_to_graph(*imarray.shape)

    # Compute clustering
    print "Compute structured hierarchical clustering..."
    #
    st = time.time()
    print st
    #

    #Do cool clustering stuff
    ward = Ward(n_clusters=n_clusters, connectivity=connectivity).fit(X)

    #Main output
    ##Can use for ID picture of grains and Contour Graph
    global label
    label = np.reshape(ward.labels_, imarray.shape)
    ##Save Arrays of Mineral ID and BSE Shade Value to TXT File
    
    #
    np.savetxt(saveFolder + 'labelArray' + '.txt', label, delimiter=" ", fmt="%s")
   
    
    #have an index number if do multiple boxes
    #np.savetxt(saveFolder + 'labelTest' + str(BoxIDNumber) + '.txt', label)
    #np.savetxt(saveFolder + 'imarrayTest' + str(BoxIDNumber) + '.txt', imarray)


# In[7]:

boundaryID(numberOfGrains = 9)


# In[7]:

#Function 5
#Make charts of grain boundries
##Make Countour Image, Make Label Image

def grainBoundaryImages(saveFolder = '/home/jon/Desktop/gsoc2014/', 
                        figureNameContour = 'ContourImage', figureNameLabel = 'LabelImage'):

    # Import Libraries
    import pylab as pl
    
    global imarray
    global n_clusters
    global label

    ##################
    # Plot the reasign grain results of image
    pl.figure(figsize=(5, 5))
    pl.imshow(label, 
              cmap=pl.cm.gray)
    #
    pl.xticks(())
    pl.yticks(())
    #
    #saved path and file and ext
    figurePathNameShadeExt = saveFolder + figureNameLabel + '.png'
    #figurePathNameShadeExt = figurePath + figureNameShade + str(BoxIDNumber) +  figureExt
    #
    pl.savefig(figurePathNameShadeExt)
    pl.show()
    ##################
    
    
    ##############
    # Plot the contour results of image
    pl.figure(figsize=(5, 5))
    pl.imshow(imarray, 
              cmap=pl.cm.gray)
    #
#    for l in range(n_clusters):
#        pl.contour(label == l, 
#                   contours = 1)
#                   colors= [pl.cm.spectral( l / float(n_clusters) ), ]   )
    #
    pl.xticks(())
    pl.yticks(())
    #
    #saved path and file and ext
    figurePathNameContourExt = saveFolder + figureNameContour + '.png'
    #figurePathNameContourExt = saveFolder + figureNameContour + str(BoxIDNumber) + figureExt
    #
    pl.savefig(figurePathNameContourExt)
    #
    pl.show()
    ##############
 


# In[9]:

grainBoundaryImages() 


# In[8]:

#Function 6 Histograms
#Function 7 Scatter Plots
#Function 8 - Function 6 + 7

def grainBoundarySize(saveFolder = '/home/jon/Desktop/gsoc2014/', 
                        figureHistName = 'GrainSizeHist'):
    
    # Import Libraries
    import numpy as np
    import pylab as pl
    #import Image


    ##################
    #Histogram of BSE values for Cropped area  

    #run histogram on image
    global label
    tiffHistogram = label.histogram()
    
    #Get X and Y values for Hist into Bar
    tiffHistSize = np.size(tiffHistogram)
    
    
    tiffHistBarXVal = range(tiffHistSize)
    tiffHistBarYVal = tiffHistogram
    
    #create bar graph
    pl.bar(tiffHistBarXVal,tiffHistBarYVal)

    #label bar graph
    pl.ylabel('Counts')
    pl.xlabel('keV Bucket via Grey Scale Value count from BSE Image')
    
    
    #saved path and file and ext
    figurePathNameHistExt = saveFolder  + figureHistName +  '.png'
    #figurePathNameShadeExt = figurePath + figureNameShade + str(BoxIDNumber) +  figureExt
    #
    pl.savefig(figurePathNameHistExt)

    #show bar graph
    pl.show()
    ##################


# In[34]:

grainBoundarySize()


# In[ ]:

def grainBoundaryScatter(saveFolder = '/home/jon/Desktop/gsoc2014/', 
                        figureNameScatter = 'ScatterImage'): 
    
    import numpy as np
    import pylab as pl
    #import Image
    
    global label
    global imarray
    
    ##Scatter Plot of BSE Values for each Mineral group
    ##################
    #Resize Arrays into 1D, so can combine
    
    cellCountLabel = np.size(label)
    cellCountIMArray = np.size(imarray)
    labelArrayReshape = np.reshape(label, (cellCountLabel) )
    imarrayArrayReshape = np.reshape(imarray, (cellCountIMArray) )
    #
    x = labelArrayReshape
    y = imarrayArrayReshape
    #
    pl.figure();
    #
    pl.scatter(x, y)
    #
    global n_clusters
    pl.axis([0, n_clusters, 0, 300])
    #
    pl.ylabel('BSE 256 Values')
    pl.xlabel('Mineral ID Number')
    #
    
    #saved path and file and ext 
    figurePathNameScatterExt = saveFolder + figureNameScatter +  '.png'
    #figurePathNameShadeExt = figurePath + figureNameShade + str(BoxIDNumber) +  figureExt
    
    pl.show()
    ####################################    


# In[ ]:

grainBoundaryScatter()


# In[ ]:

def grainBoundaryStatsImages(saveFolderSuper = '/home/jon/Desktop/gsoc2014/', 
                        figureHistNameSuper = 'GrainSizeHist', figureNameScatterSuper = 'ScatterImage'):
    
    grainBoundarySize(saveFolder = saveFolderBoth, 
                        figureHistName = figureHistNameSuper)
    
    grainBoundaryScatter(saveFolder = saveFolderBoth, 
                        figureNameScatter = figureNameScatterSuper)


# In[12]:

grainBoundaryStatsImages()


# In[9]:

#Function - Do A Whole bunch
#Run the function for Multiple Boxes

def makeCropBoxes(xStepSize = 250,
                  yStepSize = 250,
                  numberOfBoxesX = 4,
                  numberOfBoxesY = 4,
                  numberOfBoxesTotal = 16 ):


    #Create variables for the box, and the array of different box values
    box = (0,0,0,0)
    
    global boxArray
    boxArray = [0]*numberOfBoxesTotal 

    #Create index for moving through the boxArray
    index = 0

    #Create Large list of Boxes with their Cordinates
    for y in range(numberOfBoxesY):
        for x in range(numberOfBoxesX):
            box = (x*xStepSize, y*yStepSize,    xStepSize + x*xStepSize, yStepSize + y*yStepSize)
            boxArray[index] = box 
            index += 1
            #print box    

#needs work
def useBoxes():
    #Step through through the Boxes 
    ##Will need larger function of functions
    for index in range(16):
        mineralGroupIDMultiBox(boxArray[index],200, index)


# In[14]:

makeCropBoxes()


# In[31]:

#PDF Function

def pdfFunction(author = 'Jon Barnes' ,
                lab = 'Cascade Meteorite Lab'  ,
                savedFileName = 'pdfTest1'):

    ####Import in Libraries
    #
    from reportlab.pdfgen import canvas
    #
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.pagesizes import landscape
    #
    from reportlab.platypus import Image
    #
    from reportlab.lib.units import cm

    #
    import time

    global imageFileName
    global n_clusters

    print 'start'

    ####Canvas stuff
    canvas = canvas.Canvas(savedFileName + ".pdf", pagesize=letter)
    #
    canvas.setLineWidth(.3)
    #
    canvas.setFont('Helvetica', 12)



    ########################
    #Page 1
    ##Layer 1 - Header Info : Meteorite lab, Thin Section, User, Date
    ########################


    ############
    #Layer 1 - Header Info : Meteorite lab, Thin Section, User, Date
    ############
    #
    ##Lab the Data is From
    canvas.drawString(30,750,lab)
    canvas.drawString(30,735,'Scanning Electron Microscope Analysis')
    #
    ##Info on the image
    #
    canvas.drawString(300,750, "Backscatter Electron Image from " + imageFileName)
    canvas.line(280,747,580,747)
    #
    canvas.drawString(400,730, "Created by " + author) 
    canvas.line(380,727,580,727)
    #
    canvas.drawString(400,710, "Created on " + time.asctime( time.localtime(time.time()) ))
    canvas.line(380,707,580,707)
    #

    #### BSE Tiff Image
    #Image of BSE Tiff
    #bseTif = '/home/jon/Desktop/gsoc2014/semData2014/CML0615(13).tif'
    #canvas.drawImage(bseTif, 50, 400, width=10*cm, height=10*cm, preserveAspectRatio=True)
    #Label Image
    canvas.drawString(50,400, "BSE Image of " + imageFileName)

    #### BSE Tiff Image Histogram
    #Image of BSE Histogram
    #bseHist = '/home/jon/Desktop/BSEHistogramFirstLast3Removed.png'
    #canvas.drawImage(bseHist, 400, 400, width=7*cm, height=7*cm, preserveAspectRatio=True)
    #Label Image
    canvas.drawString(400,400, "BSE Histogram from " + imageFileName)

    ##Save the Page, make new page
    canvas.showPage()
    print 'writing page 1'


    ########################
    #Page 2
    ##Layer 1 - Crop BSE and BSE Hist
    ##Layer 2 - Countour and Heat Map
    ##Layer 3 - Hist of Size and Boxplot of Values
    ########################

    ############
    ####Layer 1 - Crop BSE and BSE Hist
    ############
    #
    ## BSE Cropped Image
    #Image of BSE Tiff cropped
    #bseContour = '/home/jon/Desktop/cropped bse image.png'
    #canvas.drawImage(bseContour, 50, 500, width=10*cm, height=10*cm, preserveAspectRatio=True)
    #Label Image
    canvas.drawString(50,500, "BSE Image subsection of " + imageFileName)
    #
    ##BSE Hist
    #bseHistCrop = '/home/jon/Desktop/bseDistOfCrop.png'
    #canvas.drawImage(bseHistCrop, 350, 600, width=7*cm, height=7*cm, preserveAspectRatio=True)
    #Label Image
    canvas.drawString(350,600, "BSE Histogram from")
    canvas.drawString(350,590, imageFileName + " Cropped Area")

    ############
    ####Layer 2 - Countour and Heat Map
    ############
    #
    ## BSE Tiff Contours
    #Image of BSE Tiff
    #bseContour = '/home/jon/Desktop/testContour.png'
    #canvas.drawImage(bseContour, 50, 300, width=10*cm, height=10*cm, preserveAspectRatio=True)
    #Label Image
    canvas.drawString(50,300, "BSE Image Contours for")
    canvas.drawString(50,290, "subsection of " + imageFileName)
    canvas.drawString(50,280, "Using " + str(n_clusters) + " number of grains")
    #
    #
    #### BSE Tiff BSE Mineral Heat Map
    #Image of BSE Mineral Heat Map
    #bseMineralShade = '/home/jon/Desktop/testShade.png'
    #canvas.drawImage(bseMineralShade, 350, 300, width=7*cm, height=7*cm, preserveAspectRatio=True)
    #Label Image
    canvas.drawString(350,300, "BSE Shaded map from subsection of " + imageFileName)


    ############
    ####Layer 3 - Hist of Size and Boxplot of Values
    ############
    #### Histogram of Sizes of Mineral Group
    #bseMineralShade = '/home/jon/Desktop/pixelSizeOfMineralGroups.png'
    #canvas.drawImage(bseMineralShade, 50, 100, width=7*cm, height=7*cm, preserveAspectRatio=True)
    #Label Image
    canvas.drawString(50,100, "Histogram of Sizes of Mineral Group")
    #
    #
    #### Boxplot of BSE values for Mineral Group
    #bseMineralShade = '/home/jon/Desktop/Scatter Plot of BSE values for Mineral Groups.png'
    #canvas.drawImage(bseMineralShade, 350, 100, width=7*cm, height=7*cm, preserveAspectRatio=True)
    #Label Image
    canvas.drawString(350,100, "Scatter Plot of BSE values for Mineral Group" )
    canvas.drawString(350,90, "Hope to turn into Boxplot Later")
    #
    #

    ##Save the Page, make new page
    canvas.showPage()
    print 'writing page 2'
    
    
    
    
    print 'done'

    ####Save the PDF
    canvas.save()





# In[32]:

pdfFunction()


# In[11]:

def fromImageToPDF():
    
    #Input in the Image to work with
    convertImageToArray() 
    
    #Crop the Image into a managable chunk
    cropArray() 
    
    #get grain boundries of image
    boundaryID(numberOfGrains = 9)
    
    #get pictures of defined grains
    grainBoundaryImages() 
    
    #make multiple crop boxes for looping
    makeCropBoxes()
    
    #export to a PDF
    pdfFunction()


# In[21]:

fromImageToPDF()


# In[ ]:



