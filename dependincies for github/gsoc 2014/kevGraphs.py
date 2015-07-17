
# coding: utf-8

# In[ ]:

class kevGraphs():
    

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def __init__(self,foldername = "/home/jon/Desktop/gsoc2014/",
                 filename = "VC-Raney-im-cube.raw", 
                 width=256, height = 200, channels = 1024):

        import matplotlib.pyplot as plt
        import numpy as np
        
        self.foldername = foldername
        self.filename = filename
        self.dataCubePathAndFile = foldername + filename 
        self.fileNamePlain = filename [:-4]
        
        self.width = width
        self.height = height
        self.channels = channels
        
        fileobj = open(self.dataCubePathAndFile, 'rb')
        data = np.fromfile(fileobj,dtype = np.uint8)
        data = np.reshape(data,(self.width, self.height, self.channels) )
        self.data = data

        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #kev bar graph for a point
    def averageKevPoint( self, pixelX = 1, pixelY = 1):
        
        import matplotlib.pyplot as plt
        import numpy as np

        kevValues = self.data[pixelX,pixelY] 

        plt.plot(  kevValues  )
        plt.title('KeV Energy Hits for SEM EDS Pixel' + "X" + str(pixelX) + "Y" + str(pixelY))
        plt.xlabel('kev level')
        plt.ylabel('hit count')
        plt.xlim(0,1050)

        savekevbartest = self.foldername + "kevEDSbarTest"                             + self.filename[:-4]                             + "X" + str(pixelX) + "Y" + str(pixelY)                             + ".png"
        plt.savefig( savekevbartest )
        plt.show() 
    
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #kev scatter graph with error for a row
    def  averageKevRow(self, studyRow = 10):

        import numpy as np
        import matplotlib.pyplot as plt

        dataRowOne = self.data[:,studyRow]

        rowData = np.zeros( (256, self.channels) )

        for pixelCell in range(256):
            rowData[pixelCell] = dataRowOne[pixelCell]

        #Min
        rowMIN =  np.min(rowData, axis=0)
        #Max
        rowMAX = np.max(rowData, axis=0)
        #Mean
        rowMEAN =  np.mean(rowData, axis=0)
        #STD
        rowSTD = np.std(rowData, axis=0)

        rowBuckets = np.array( range(0, 1024, 1) )

        x = rowBuckets
        y = rowMEAN

        #Graph the Mean keV EDS values of the Mineral and the STD as error bar
        errors = rowSTD 

        plt.plot(x, y, marker='o', color='b')

        plt.errorbar(x, rowSTD, yerr=errors, fmt='', color='b')

        plt.title('Mean keV EDS Values of Row'+str(studyRow))
        plt.xlabel('keV bucket')
        plt.ylabel('Count')
        plt.xlim(0,1050)

        savelabelBSEMeanSorted = '/home/jon/Desktop/gsoc2014/' + "kev-eds-values-for-row-" +str(studyRow) + ".png"
        plt.savefig( savelabelBSEMeanSorted )

        plt.show()
        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #kev scatter graph with error for a row
    def  averageKevCol( self, studyCol = 10):
        import numpy as np
        import matplotlib.pyplot as plt

        colData = np.zeros( (self.height,self.channels) )

        ###pull out row from data cube
        dataColOne = self.data[:][studyCol]

        for pixelCell in range(self.height):
            colData[pixelCell] = dataColOne[pixelCell]

        #Min
        colMIN =  np.min(colData, axis=0)
        #Max
        colMAX = np.max(colData, axis=0)
        #Mean
        colMEAN =  np.mean(colData, axis=0)
        #STD
        colSTD = np.std(colData, axis=0)

        colBuckets = np.array( range(0, 1024, 1) )

        x = colBuckets
        y = colMEAN


        #Graph the Mean keV EDS values of the Mineral and the STD as error bar
        errors = colSTD 

        plt.plot(x, y, marker='o', color='b')

        plt.errorbar(x, colSTD, yerr=errors, fmt='', color='b')

        plt.title('Mean keV EDS Values of Col'+str(studyCol))
        plt.xlabel('keV bucket')
        plt.ylabel('Count')
        plt.xlim(0,1050)

        savelabelBSEMeanSorted = '/home/jon/Desktop/gsoc2014/' + "kev-eds-values-for-col-" +str(studyCol) + ".png"
        plt.savefig( savelabelBSEMeanSorted )

        plt.show()
        
        
        
        
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #kev scatter graph with error for a row
    def  averageKevBox( self,
                        x1 = 10, y1 = 10,
                        x2 = 100, y2 = 100):

        import numpy as np
        import matplotlib.pyplot as plt

        boxWidth = np.array( range(x1, x2, 1) )
        boxHeight = np.array( range(y1, y2, 1) )

        numberOfPixels = (x2-x1) * (y2-y1)

        boxDataZeros = np.zeros( (numberOfPixels,self.channels) )

        buckets = np.array( range(0, 1024, 1) )

        boxData = np.zeros( (numberOfPixels,self.channels) )

        counter = 0
        for row in boxWidth:
            for col in boxHeight:
                boxData[counter] = self.data[row,col]
                counter += 1

        for pixelNumber in range(numberOfPixels):
            boxDataZeros[pixelNumber] = boxData[pixelNumber]

        #Min
        boxMIN =  np.min(boxDataZeros, axis=0)
        #Max
        boxMAX = np.max(boxDataZeros, axis=0)
        #Mean
        boxMEAN =  np.mean(boxDataZeros, axis=0)
        #STD
        boxSTD = np.std(boxDataZeros, axis=0)

        x = buckets
        y = boxMEAN

        #Graph the Mean keV EDS values of the Mineral and the STD as error bar
        errors = boxSTD 

        plt.plot(x, y, marker='o', color='b')

        plt.errorbar(x, boxSTD, yerr=errors, fmt='', color='b')

        plt.title('Mean keV EDS Values of Sample Box '                   + "(" + str(x1) + "," + str(y1) + ")"                   + " to "                    + "(" + str(x2) + "," + str(y2) + ")" )
        plt.xlabel('keV bucket')
        plt.ylabel('Count')
        plt.xlim(0,1050)

        savelabelBSEMeanSorted = '/home/jon/Desktop/gsoc2014/' + "kev-eds-values-for-box-" + "(" + str(x1) + "," + str(y1) + ")"  "to"  "(" + str(x2) + "," + str(y2) + ")"   + ".png"

        plt.savefig( savelabelBSEMeanSorted )

        plt.show()

        
        

    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>       
    #kev scatter graph with error for all
    def  averageKevAll( self):

        import numpy as np
        import matplotlib.pyplot as plt


        dataAllMean = np.zeros( (self.height,self.channels) )
        dataAllStd  = np.zeros( (self.height,self.channels) )

        colData = np.zeros( (self.height,self.channels) )
        for col in range( self.height ):
            colData = np.zeros( (self.height,self.channels) )
            dataColOne = self.data[:][col]

            for pixelCell in range(self.height):
                colData[pixelCell] = dataColOne[pixelCell]

            #Mean
            colMEAN =  np.mean(colData, axis=0)
            dataAllMean[ col ] = colMEAN 
            #STD
            colSTD = np.std(colData, axis=0)
            dataAllStd[ col ] = colSTD


        buckets = np.array( range(0, 1024, 1) ) 

        dataAllStdErr = np.std(dataAllStd, axis=0)

        dataAllMeanY = np.mean(dataAllMean, axis=0)

        x = buckets
        y = dataAllMeanY

        #Graph the Mean keV EDS values of the Mineral and the STD as error bar
        errors = dataAllStdErr

        plt.plot(x, y, marker='o', color='b')

        plt.errorbar(x, colSTD, yerr=errors, fmt='', color='b')

        plt.title('Mean keV EDS Values of Whole Image')
        plt.xlabel('keV bucket')
        plt.ylabel('Count')
        plt.xlim(0,1050)

        savelabelBSEMeanSorted = '/home/jon/Desktop/gsoc2014/classesFolders/' + "kev-eds-values-for-all-image" + ".png"
        plt.savefig( savelabelBSEMeanSorted )

        plt.show()

