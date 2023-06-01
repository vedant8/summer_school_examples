import numpy as np

path = "SourceListA.txt"
path = "SourceListB.txt"
path = "SourceListC.txt"
path = "SL_TeVCat.txt"
path = "HAWC_Cat.txt"
print(path)

a = np.loadtxt(path,dtype=[('name',np.unicode_, 256), ('ra',float),
    ('dec',float)])

minra = min( a['ra'] )
maxra = max( a['ra'] )
print('ra range (%.2f, %.2f)' % (minra, maxra))

mindec = min( a['dec'] )
maxdec = max( a['dec'] )
print('dec range (%.2f, %.2f)' % (mindec, maxdec))

