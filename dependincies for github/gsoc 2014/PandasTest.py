# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# <codecell>

#Import in Arrays from exported TXT files
labelArray = np.loadtxt( '/home/jon/Desktop/labelTest.txt' , dtype='float', delimiter=None,)
imarrayArray = np.loadtxt( '/home/jon/Desktop/imarrayTest.txt' , dtype='float', delimiter=None,)
#
#Resize Arrays into 1D, so can combine
labelArrayReshape = np.reshape(labelArray, (62500) )
imarrayArrayReshape = np.reshape(imarrayArray, (62500) )

# <codecell>

x = labelArrayReshape
y = imarrayArrayReshape
#
plt.figure();
#
plt.scatter(x, y, s=20, c='b', marker='o', cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None)
#
plt.ylabel('BSE 256 Values')
plt.xlabel('Mineral ID Number')
plt.title('Scatter Plot of BSE values for Mineral Groups')
#
plt.savefig('Scatter Plot of BSE values for Mineral Groups.png')
#
plt.show()

# <codecell>

#Convert the 1D Arrays into Sieres
s = pd.Series(imarrayArrayReshape, labelArrayReshape)
s

# <codecell>

df = pd.DataFrame(s)
df = df.sort()
df.head()

# <codecell>

plt.figure();
#
bp = df.boxplot()
#
plt.show()

# <codecell>

####Create large DataFrame for sorting
dfMineralIDSort = pd.DataFrame(np.random.randn(500,200))
dfMineralIDSort

# <codecell>

#####Example of 5 Boxplots from Random
df = pd.DataFrame(np.random.randn(10,5))

plt.figure();

bp = df.boxplot()

plt.show()

# <codecell>

#####Example of 200 Boxplots from Random
#Boxplots For 200 different Mineral Groups
dfLarger = pd.DataFrame(np.random.randn(10,200))
#
plt.figure();
#
bp = dfLarger.boxplot()
#
plt.show()

# <codecell>


