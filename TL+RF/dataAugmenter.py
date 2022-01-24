import cv2
import  os
import numpy as np
import random

from scipy import rand

class DataAugmenter:

    angles = [45,135,225,315]

    def __init__(self,srcPath,imgName) -> None:
        self.srcPath = srcPath
        self.img = cv2.imread(srcPath+imgName)
            
        self.imgH,self.imgW= self.img.shape[:2]
        self.imgname = imgName.split('.')[0]
        print(self.imgname)
        self.rotate()
        self.verticalFlip()
        self.horizontalFlip()
        self.zoom()
    

    def rotate(self):
        count = 0
        for angle in self.angles:
            rotMat = cv2.getRotationMatrix2D((int(self.imgW/2), int(self.imgH/2)), angle, 1)
            img = cv2.warpAffine(self.img, rotMat, (self.imgW, self.imgH))
            cv2.imwrite(f'{self.srcPath}/{self.imgname}_rot-{count}.png',img)
            count+=1
    
    def horizontalFlip(self):
        horFlip = cv2.flip(self.img,1)
        cv2.imwrite(f'{self.srcPath}/{self.imgname}_horFlip.png',horFlip)
    
    def verticalFlip(self):
        vertFlip =  cv2.flip(self.img,0)
        cv2.imwrite(f'{self.srcPath}/{self.imgname}_vertFlip.png',vertFlip)

    def zoom(self):
        zoomValue = np.random.random()
        
        value = np.random.random()
        
        h_taken = int(value*self.imgH)
        w_taken = int(value*self.imgW)
        h_start = random.randint(0, self.imgH-h_taken)
        w_start = random.randint(0, self.imgW-w_taken)
        zoomed = self.img[h_start:h_start+h_taken, w_start:w_start+w_taken, :]
        zoomed = cv2.resize(zoomed, (self.imgH, self.imgW), cv2.INTER_CUBIC)
        cv2.imwrite(f'{self.srcPath}/{self.imgname}_zoomed.png',zoomed)
        
        

basePath = '/Volumes/Windows/BreastCancerDataset/Converted/Training'

# os.remove('/Volumes/Windows/BreastCancerDataset/Converted/Training/.DS_Store')

trainPaths = os.listdir(basePath)



for classes in trainPaths:
    imagelist = os.listdir(basePath+"/"+classes)
    for image in imagelist:
        if image.split('.')[1]=="png":
            aug = DataAugmenter(f'{basePath}/{classes}/',image)

# zoomed,og = aug.zoom()
# aug.rotate()
# cv2.imshow("G1",zoomed)
# cv2.imshow("G2",og)
# cv2.waitKey(0)
        
