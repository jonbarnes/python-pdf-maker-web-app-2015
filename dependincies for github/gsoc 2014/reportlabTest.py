# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

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

####Canvas stuff
canvas = canvas.Canvas("jonsTestForm.pdf", pagesize=letter)
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
canvas.drawString(30,750,'Cascade Meteorite Lab')
canvas.drawString(30,735,'Scanning Electron Microscope Analysis')
#
##Info on the image
#
canvas.drawString(300,750, "Backscatter Electron Image from " + "CML0615(13)")
canvas.line(280,747,580,747)
#
canvas.drawString(400,730, "Created by " + "Jon Barnes")
canvas.line(380,727,580,727)
#
canvas.drawString(400,710, "Created on " + "June 18 2014")
canvas.line(380,707,580,707)
#

#### BSE Tiff Image
#Image of BSE Tiff
bseTif = '/home/jon/Desktop/gsoc2014/semData2014/CML0615(13).tif'
canvas.drawImage(bseTif, 50, 400, width=10*cm, height=10*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,400, "BSE Image of CML0615(13)")

#### BSE Tiff Image Histogram
#Image of BSE Histogram
bseHist = '/home/jon/Desktop/BSEHistogramFirstLast3Removed.png'
canvas.drawImage(bseHist, 400, 400, width=7*cm, height=7*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(400,400, "BSE Histogram from CML0615(13)")

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
bseContour = '/home/jon/Desktop/cropped bse image.png'
canvas.drawImage(bseContour, 50, 500, width=10*cm, height=10*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,500, "BSE Image subsection of CML0615(13)")
#
##BSE Hist
bseHistCrop = '/home/jon/Desktop/bseDistOfCrop.png'
canvas.drawImage(bseHistCrop, 350, 600, width=7*cm, height=7*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(350,600, "BSE Histogram from")
canvas.drawString(350,590, "CML0615(13) Cropped Area")

############
####Layer 2 - Countour and Heat Map
############
#
## BSE Tiff Contours
#Image of BSE Tiff
bseContour = '/home/jon/Desktop/testContour.png'
canvas.drawImage(bseContour, 50, 300, width=10*cm, height=10*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,300, "BSE Image Contours for")
canvas.drawString(50,290, "subsection of CML0615(13)")
canvas.drawString(50,280, "Using 200 Clusters")
#
#
#### BSE Tiff BSE Mineral Heat Map
#Image of BSE Mineral Heat Map
bseMineralShade = '/home/jon/Desktop/testShade.png'
canvas.drawImage(bseMineralShade, 350, 300, width=7*cm, height=7*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(350,300, "BSE Shaded map from subsection of CML0615(13)")


############
####Layer 3 - Hist of Size and Boxplot of Values
############
#### Histogram of Sizes of Mineral Group
bseMineralShade = '/home/jon/Desktop/pixelSizeOfMineralGroups.png'
canvas.drawImage(bseMineralShade, 50, 100, width=7*cm, height=7*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(50,100, "Histogram of Sizes of Mineral Group")
#
#
#### Boxplot of BSE values for Mineral Group
bseMineralShade = '/home/jon/Desktop/Scatter Plot of BSE values for Mineral Groups.png'
canvas.drawImage(bseMineralShade, 350, 100, width=7*cm, height=7*cm, preserveAspectRatio=True)
#Label Image
canvas.drawString(350,100, "Scatter Plot of BSE values for Mineral Group" )
canvas.drawString(350,90, "Hope to turn into Boxplot Later")
#
#

##Save the Page, make new page
canvas.showPage()
print 'writing page 2'

####Save the PDF
canvas.save()

# <codecell>


