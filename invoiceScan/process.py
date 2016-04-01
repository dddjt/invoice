import cv2 as cv
from scan.algofactory.ScanAlgoFactory import *

if __name__ == '__main__':
    #filename = 'pic/A/1.1500007-r.png'
    #filename = 'pic/A/1.150000002-r.png'
    #filename = 'pic/A/00021.png'
    #filename = 'pic/A/00022.png'
    #filename = 'pic/A/002300027.png'
    filename = 'pic/A/002300028.png'

    action = ScanAlgoFactory.scan('RunLen',filename,'DEFAULT')
    externalRects = action.doSplitAction()
    action.drawRectangle(externalRects)
    cv.imshow('ResultRect',action.srcImg)
    cv.waitKey(0)