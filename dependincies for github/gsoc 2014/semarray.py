
# coding: utf-8

# In[ ]:

class semarray():
    

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def __init__(self,tifPath, tifFile):

        import os
        import Image
        import numpy as np
        
        #get just file name for later labels = importImageFileName
        #Name Scheme = Lab Code + Meteorite Number + SEM Moasic Number + file extension

        self.tifPathAndFile = tifPath + tifFile
        
        self.fileName = tifFile[:-4]
        
        importImageFileName, importImageFileExtension = os.path.splitext(tifFile)
        #print importImageFileName
        #print importImageFileExtension
        
        #cut off the 3 letters off the file
        self.ImageFileNameNumbers = importImageFileName[3:]

        #thin section lab code
        self.LabCode = importImageFileName[:3]

        #cut off the 3 letters off the file
        self.MeteoriteNumber = importImageFileName[3:-4]

        #SEM Mosaic number
        #cut off the 3 letters off the file
        self.SEMmosaicNumber = importImageFileName[-3:-1]   
        
        #Convert Image to Array
        self.ImagePointer = Image.open(self.tifPathAndFile)
        
        #convert Array to Martix
        self.ImageArray = np.asanyarray(self.ImagePointer)
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    ########################
    #CropBoxes
    def cropBoxes(self, boxWidth, boxHeight):     
    
        imFullWidth  = self.ImagePointer.size[0]
        imFullHeight = self.ImagePointer.size[1]

        boxCountWide = imFullWidth/boxWidth
        boxCountHeight = imFullHeight/boxHeight

        leftOverWidth = imFullWidth % boxWidth
        leftOverHeight = imFullHeight % boxHeight

        totalNUmberofFullBoxes =  (boxCountWide) * (boxCountHeight)
        totalNumberofBoxes = (boxCountWide+1) * (boxCountHeight+1)
    
        #Create variables for the box, and the array of different box values
        # (top letf corner, bottom right corner) .... (x1,y1  x2,y2)
        box = (0,0,0,0)

        #global boxArray
        boxArray = [0]*totalNumberofBoxes

        #Create index for moving through the boxArray
        indexRegular = 0

        #Create Large list of Boxes with their Cordinates

        #for the main boxes
        for y in range(boxCountHeight):
            for x in range(boxCountWide):
                box = (x*boxWidth, y*boxHeight,    boxWidth + x*boxWidth, boxHeight  + y*boxHeight )
                boxArray[indexRegular] = box 
                indexRegular += 1
                #print box 
       
        #for the left over bottom boxes
        indexBottom = totalNUmberofFullBoxes
        for x in range(boxCountWide):   
            box = (x*boxWidth, imFullHeight-leftOverHeight,    boxWidth + x*boxWidth, imFullHeight) 
            boxArray[indexBottom] = box 
            indexBottom += 1


        #for the left over side boxes
        indexSide = totalNUmberofFullBoxes + boxCountWide
        for y in range(boxCountHeight):
            box = (imFullWidth-leftOverWidth, y*boxHeight,    imFullWidth, boxHeight  + y*boxHeight )
            boxArray[indexSide] = box 
            indexSide += 1

        #bottom corner box
        boxInBottomCorner = (imFullWidth-leftOverWidth , imFullHeight-leftOverHeight, imFullWidth, imFullHeight)
        boxArray[totalNumberofBoxes-1] = boxInBottomCorner

        self.cropBoxes = boxArray
        self.totalNumberofcropBoxes = totalNumberofBoxes
        
        
        saveCropBoxArray =  '/home/jon/Desktop/gsoc2014/' + 'cropBoxArray' + self.fileName + "BOX"  + '.txt'
        np.savetxt(saveCropBoxArray , boxArray,  delimiter=" ", fmt="%s")
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #Function - crop the tiff
    def cropArrayCustom(self, cropBox,  saveFolder = '/home/jon/Desktop/gsoc2014/', boxNumberName = 'Custom'):
    
        import os
        import Image
        import numpy as np
        import pylab as pl
    
        #Crop the image array by the Box       
        self.cropImageCustom        = self.ImagePointer.crop(cropBox)
        self.cropImageAsArrayCustom = np.asanyarray(self.cropImageCustom )
        

        # SavedFolder / "imarrayCrop" + thin section info + "Box" + BoxNumber + .txt
        imArrayCropFileName = saveFolder + 'imarrayCrop' + self.fileName + "BOX" + boxNumberName + '.txt'
        np.savetxt(imArrayCropFileName , self.cropImageAsArrayCustom,  delimiter=" ", fmt="%s")
    
        ############
        # Plot the crop bse image
        pl.figure(figsize=(5, 5))
        pl.imshow(self.cropImageAsArrayCustom, cmap=pl.cm.gray)
        #
        pl.xticks(())
        pl.yticks(())
        #
        ##Save Image
 
        #
        #saved path and file and ext
        imArrayImageCropFileName = saveFolder + 'croppedImageFor' + self.fileName + "BOX" + boxNumberName + '.png'
        #
        pl.savefig(imArrayImageCropFileName)
        #
        #pl.show()
        ###########
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #Use - boxArray from createCropBoxes() on cropArray()
    def cropAllTheBoxes(self):
        self.cropBoxes(250,250)
        for boxNumber in range( self.totalNumberofcropBoxes):
            boxInUse = self.cropBoxes[boxNumber]
            self.cropArrayCustom(cropBox = boxInUse , boxNumberName = str(boxNumber) )
    #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

