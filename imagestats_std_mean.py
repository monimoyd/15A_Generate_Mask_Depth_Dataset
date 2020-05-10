import cv2
import os
import numpy as np
currentDirectory = os.getcwd()
print(currentDirectory)
arr = os.listdir()
print(arr)

class RunningMeanStd:
    def __init__(self, data=None):
        if data is not None:
            data = np.atleast_2d(data)
            self.mean = np.mean(data)
            self.std  = np.std(data)
            self.nobservations = 1
            self.ndimensions   = 1
        else:
            self.nobservations = 0

    def GetStats(self, data):
        if self.nobservations == 0:
            self.__init__(data)
        else:
            data = np.atleast_2d(data)
            newmean = np.mean(data)
            newstd  = np.std(data)
            m = self.nobservations * 1.0
            n = 1 # single image update

            tmp = self.mean
            self.mean = m/(m+n)*tmp + n/(m+n)*newmean
            self.std  = m/(m+n)*self.std**2 + n/(m+n)*newstd**2 +\
                        m*n/(m+n)**2 * (tmp - newmean)**2
            self.std  = np.sqrt(self.std)
            self.nobservations += n

#--------------------------------------- Batchwise statistics ------
MeanStdObj = RunningMeanStd()
MeanofImages = []
StdOfImages = []
#for batch in ['batch3_images','batch4_images'] :
for batch in ['batch1','batch2', 'batch3','batch4', 'batch5', 'batch6', 'batch7', 'batch8', 'batch9', 'batch10'] :
    print("Batch -------" + batch + "-------")
    for folder  in ['bg_jpg','depth_fg_bg_jpg','fg_bg_jpg','fg_jpg','mask_black_jpg','mask_jpg'] :
        indir = batch + "/" + folder
        # print(" ---- Directory -- " + folder)
        batchindx = 0
        for subdir, dirs, files in os.walk(indir):
            for file in files :
                frame = cv2.imread(os.path.join(subdir, file))
                frame = frame/255
                MeanStdObj.GetStats(frame)

            # print("Mean = {MeanStdObj.mean , MeanStdObj.std)
            print("ImageType : %s  Mean : %3f,  Std : % 3f" %( folder,MeanStdObj.mean, MeanStdObj.std)) 
            MeanofImages.append(MeanStdObj.mean)
            StdOfImages.append(MeanStdObj.std)
            MeanStdObj.mean =0
            MeanStdObj.std=0
            MeanStdObj.nobservations=0

print("Mean ", MeanofImages)
print ("Std ", StdOfImages)
batchindx=0
tyindxstart=0
typeindx=tyindxstart
# 6 types
for folder  in ['bg_jpg','depth_fg_bg_jpg','fg_bg_jpg','fg_jpg','mask_black_jpg','mask_jpg']:
    
    MeanI =0
    StdI=0
    #for batch in ['batch3_images','batch4_images'] : #10 batches
    for batch in ['batch1','batch2', 'batch3','batch4', 'batch5', 'batch6', 'batch7', 'batch8', 'batch9', 'batch10'] : #10 batches	
        MeanI  += MeanofImages[typeindx]
        StdI  += StdOfImages[typeindx]
        typeindx+6
    MeanI =MeanI/10
    StdI = StdI/10
    tyindxstart=tyindxstart+1
    typeindx=tyindxstart
    print("Category : %s  Mean : %3f,  Std : % 3f" %( folder,MeanI,StdI)) 

#--------------------------------------- Overall Statistics ------

# MeanStdObj = RunningMeanStd()
# MeanStdObj.mean =0
# MeanStdObj.std=0
# MeanStdObj.nobservations=0
# for batch in ['batch3_images','batch4_images'] :
#     print("Batch -------" + batch + "-------")
#     for folder  in ['bg_jpg','depth_fg_bg_jpg','fg_bg_jpg','fg_jpg','mask_black_jpg','mask_jpg'] :
#         indir = batch + "/" + folder
#         # print(" ---- Directory -- " + folder)
#         batchindx = 0
#         for subdir, dirs, files in os.walk(indir):
#             for file in files :
#                 frame = cv2.imread(os.path.join(subdir, file)) 
#                 frame = frame/255
#                 MeanStdObj.GetStats(frame)

# print(" Mean : %3f,  Std : % 3f" %( MeanStdObj.mean, MeanStdObj.std)) 

