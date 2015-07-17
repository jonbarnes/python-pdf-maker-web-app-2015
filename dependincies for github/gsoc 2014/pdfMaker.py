
# coding: utf-8

# In[1]:

#PDF Function

def pdfFunctionLoop(author = 'Jon Barnes' ,
                lab = 'Cascade Meteorite Lab'  ,
                savedFileName = 'pdfTestLoop1'):

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
    ## Header Info : Meteorite lab, Thin Section, User, Date
    ##Lab the Data is From
    canvas.drawString(30,750,lab)
    canvas.drawString(30,735,'Scanning Electron Microscope Analysis')
    #
    canvas.drawString(400,730, "Created by " + author) 
    canvas.line(380,727,580,727)
    #
    canvas.drawString(400,710, "Created on " + time.asctime( time.localtime(time.time()) ))
    canvas.line(380,707,580,707)
    #
    #### BSE Tiff Image
    #Image of BSE Tiff
    bseMainFile = '/home/jon/Desktop/gsoc2014/CML0615(13).tif'
    canvas.drawImage(bseMainFile, 50, 100, width=15*cm, height=15*cm, preserveAspectRatio=True)
    canvas.drawString(100,100, "Back Scatter Electron (BSE) Image of Metorite thin section CML0615 ;")
    canvas.drawString(100,80, "mosaic image 13, CML0615(13). Grey scale shows average density.")
    canvas.drawString(100,60, "Lighter spots are heavier then darker spots.")
    #
    ##Save the Page, make new page
    canvas.showPage()
    print 'writing page 1'

    
    bsePNGpath = '/home/jon/Desktop/gsoc2014/'
    
    bsePNGfile = "croppedImageForCML0615(13)BOX"
    bsePNG = bsePNGpath + bsePNGfile
    
    bseCROPpngFile = "output"
    bseCROPpng = bsePNGpath + bseCROPpngFile
    
    bseNumber = 1
    
    fileExt = ".png"
    
    for i in range(62):
        canvas.drawString(400,400, "this is page 1+" + str(i))
        
        #### BSE Tiff Image
        #Image of BSE Tiff
        bseWholeFile = bsePNG + str(bseNumber) + fileExt
        canvas.drawImage(bseWholeFile, 50, 400, width=10*cm, height=10*cm, preserveAspectRatio=True)
        
        #Label Image
        bsePNGfileWhole = bsePNGfile + str(bseNumber)
        canvas.drawString(50,400, "BSE Image of " + bsePNGfileWhole)
        
        #### BSE Crop Tiff Image
        #Image of BSE Tiff
        bseCROPWholeFile = bseCROPpng + str(bseNumber) + fileExt
        canvas.drawImage(bseCROPWholeFile, 400, 400, width=5*cm, height=5*cm, preserveAspectRatio=True)
        
        #Label Image
        bsePNGfileWhole = bsePNGfile + str(bseNumber)
        canvas.drawString(400,400, "Crop Location in BSE Image of " + bseCROPWholeFile)
        
        bseNumber += 1
        
        print "writting page " + str(i) 
        canvas.showPage()
        
    print 'done'
    ####Save the PDF
    canvas.save()




# In[ ]:



