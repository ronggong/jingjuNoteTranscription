import os, sys
from os import listdir
from os.path import isfile, join, splitext
import matplotlib.pyplot as plt
import numpy as np
import collections
from scipy.stats import norm

sys.path.append(join(os.path.dirname(os.path.realpath(__file__)),'src'))

import musicXMLparser

scoreFolder = '/Users/gong/Documents/MTG document/Jingju arias/Scores/'
onlyfiles = [f for f in listdir(scoreFolder) if isfile(join(scoreFolder, f))]

intervals_total = []
for filename in onlyfiles:
    filenameRoot, fileExtension = splitext(filename)
    if fileExtension == '.xml':
        intervals = musicXMLparser.getIntervals(join(scoreFolder, filename))
        intervals_total += intervals

'''
# find unique elements
intervalsSet    = set(intervals_total)
intervalsUnique = list(intervalsSet)

intervalsFreq = {}
# construct the dictionary
for iu in intervalsUnique:
    intervalsFreq[iu] = 0

# fill the dictionary
for iu in intervalsUnique:
    for ii in intervals_total:
        if iu == ii:
            intervalsFreq[iu] += 1

# sort the dictionary by keys
oIntervalsFreq = collections.OrderedDict(sorted(intervalsFreq.items()))

# keys and values
interFreqKeys   = oIntervalsFreq.keys()
interFreqValues = oIntervalsFreq.values()

# fit intervals to norm distribution
interMean, interStd = norm.fit(intervals_total)
interX              = range(min(interFreqKeys),max(interFreqKeys)+1)
interPdf            = norm.pdf(interX,interMean,interStd)

print oIntervalsFreq
print interFreqKeys
print np.array(interFreqValues)/float(sum(interFreqValues))
print interPdf

plt.stem(interFreqKeys,np.array(interFreqValues)/float(sum(interFreqValues)))
plt.plot(interX,interPdf,'k')
plt.xlabel("Interval")
plt.ylabel("Frequency")
plt.show()

# print intervals_total

# bins = np.linspace(-10,10,21)
# plt.hist(intervals_total,bins)
# plt.title("Intervals Histogram")
'''

