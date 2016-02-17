from music21 import *

def getIntervals(xmlFile):
    '''
    get intervals
    :param xmlFile:
    :return:
    '''
    xmlScore = converter.parse(xmlFile)
    xmlScore.show()

    p = xmlScore[2]

    p = p.flat.notes

    for pp in p.elements:
        if pp.duration.isGrace:
            p.remove(pp)

    intervals = []
    for ii in range(len(p)-1):
        intervals.append(interval.notesToChromatic(p[ii],p[ii+1]).semitones)

    return intervals

# sAlt.show() # show first 5 measures