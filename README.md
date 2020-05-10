# 15A_Generate_Mask_Depth_Dataset
This assignmnet is to create dataset of mask and depth datasets from foreground and background images

# 1.  Problem Statement

We need to generate custom dataset we  must have 100 background, 100x2 (including flip), and you randomly place the foreground on the background 20 times, you have in total 100x200x20 images. 

In total we MUST have:

    400k fg_bg images
    400k depth images
    400k mask images
    generated from:
     100 backgrounds
     100 foregrounds, plus their flips
     20 random placement on each background.
     
     
     We need to show the statistics of the generated images as well as create a gallery
     
# 2. Link ot Gdrive for the images
     
     https://drive.google.com/open?id=1o5hPttBP_x5GD37AFYJQ41rvJ9Xdb8n0
     
     The directory contains 10 zip files (batch1_images.zip,batch2_images.zip, batch3_images.zip, batch4_images.zip, batch5_images.zip, batch6_images.zip batch7_images.zip, batch8_images.zip, batch9_images.zip, batch10_images.zip)
     
     Each zip file has the following folders:
    
     
     fg_jpg : Foreground jpg images of size (80x80) with each image is uniquely numbered across batches e.g. fg_img_91.jpg
     bg_jpg : Background jpeg images of size (160x160) with each image is uniquely numbered  but repeated across batches e.g. bg_img_5.jpg
     mask_jpg: mask jpeg images of size (80x80) with each image is uniquely numbered  but repeated across batches e.g. mask_img_5.jpg
     fg_bg_jpg : Foreground images overlayed on background images of size (160x160) with each image is uniquely numbered as
     fg_bg_1_4_0_15 where the first digit 1 represents the foreground image id from which it is generated
      second digit 4 represents the background image id from which it is generated, 0 represents, this image is not flipped (if flipped it will have value 1), last digit 15 represents the sequence number (1-20)
      mask_black_jpg: Mask image overlayed on black background with each image is uniquely numbered as
     bg_mask_1_4_0_15 where the first digit 1 represents the foreground image id from which it is generated
      second digit 4 represents the background image id from which it is generated, 0 represents, this image is not flipped (if flipped it will have value 1), last digit 15 represents the sequence number (1-20)
      
      depth_fg_bg_jpg: JPG images created using the depth model prediction on fg_bg images. The convention for depth_fg_bg_jp is same as corresponding fg_bg_jpg image from which it is generated, only depth_ is prepended to image name.
      
# 3. Add your dataset statistics:
        Kinds of images : (fg, bg, fg_bg, masks, depth)
        Total images of each kind:
	fg : 100
	bg: 100
	mask: 100
	fg_bg: 400000
	depth: 400000
	mask overlaued on black background: 400000
	
        The total size of the dataset: 6 GB
        Mean/STD values: 
		
	ImageType : bg_jpg  Mean : 0.739088,  Std :  0.265235
        ImageType : depth_fg_bg_jpg  Mean : 0.776709,  Std :  0.312767
        ImageType : fg_bg_jpg  Mean : 0.727454,  Std :  0.275896
        ImageType : fg_jpg  Mean : 0.822849,  Std :  0.299034
        ImageType : mask_black_jpg  Mean : 0.084384,  Std :  0.275301
        ImageType : mask_jpg  Mean : 0.337507,  Std :  0.464947
      
      
 # 4. Explain how you created your dataset
     ## a. how were fg created with transparency
     
     We used GIMP tool to generate foreground images with transparency. The full steps with screenshots are givne in:     
     https://github.com/monimoyd/15A_Generate_Mask_Depth_Dataset/blob/master/ImageCreationSteps.pdf

     ## b. how were masks created for fgs
     
  Masks were created using GIP tool, Full steps with screenshots are given in
   https://github.com/monimoyd/15A_Generate_Mask_Depth_Dataset/blob/master/ImageCreationSteps.pdf
		

		
   ## c. how did you overlay the fg over bg and created 20 variants
     
     For each foreground image is overlayed randomly on each of the background image by using paste function of PIL library. We have chosen  (160x160) as dimension for background and (80x80) as dimension for foreground. While generating random position for 
     overlaying foreground on background, integer number is generated 20 times between 0 and 80 for both the x cordinate as well as y cordinate, using the function random.choice with  replace=False so that positions are not repeated. 
     
     In addition the each foreground image is horizonatlly flipped using function transpose from PIL library with option  PILImage.FLIP_LEFT_RIGHT and each of the flipped foreground image is also overlayed randomly on background image
     
     The  mask image corresponding to the foregorund image is overlayed on black background randomly but correpdoing position
     as the original foreground image is overlayed. Similary for flipped images the same process is repeated    
     
     The python script for generating overlay images is
     
     ![Script for generating fg bg iamges](/generate_fg_bg_images_jpg.py)
     
     It takes five arguments:
     
     argument1 : foreground images directory
     argument2: Background images directory
     argument3: Mask Images Directory
     argument4: Output directory for Overlayed foreground background image 
     argument5:  Output directory for Overlayed mask images on black backgournd
 

     
     
   ## d. how did you create your depth images? 
     
     The depth images are created using using the base notebook for depth model given modified. 
     
     - Changed code to process grey images by stacking 3 times 
     - For each batch, Iterate over images lying in fg_bg_jpg direcotry under the respective batch folders and store the images under depth_fg_bg_bng 
     - Used batch size as 128 and images are processed in a batch of 128 at a time 
     - Used plt.cla, plt.axis('off') and plt.clf so that Matplotlib saves the images faster
     
     The modified code is: ![Jupyter notebook for Dept hModel](/DenseDepth.ipynb)
     
 # 3. Show your dataset the way I have shown above in this readme     
     
     ## Python Code for generating gallery for  BackGround Scenary,ForeGround,coressponding Masks,ForeGround-Background,ForeGround-BackGround Mask and Depth Model Output images :

https://github.com/sudhakarmlal/EVA4/blob/master/Session14-15/GalleryUtil.ipynb


#### 1. Scenary or BackGround Images:

We have taken Home Images as background.Below is the gallery for the Home Images.A sample from the 100 backgrounds taken are shown below

![](https://github.com/sudhakarmlal/EVA4/blob/master/Session14-15/Images/BackGrnd.png)

#### 2. ForeGround Images:

Foreground images are also download.Below is the gallery for the same.A sample taken from the 100 foreground images are shown below

![](https://github.com/sudhakarmlal/EVA4/blob/master/Session14-15/Images/Foreground.png)

#### 3. Masked Images:

The Masked Images are generated for all the corresponding foreground images.A sample is taken for the 100 mask images  and are shown in the gallery below

![](https://github.com/sudhakarmlal/EVA4/blob/master/Session14-15/Images/Mask.png)

#### 4. ForeGround-BackGround Images:

A total of 400K ForeGround-BackGround Images are generated by Overlaying foreground over background.Foreground is overlayed over background at twenty different positions.And also corresponding flip images for the foreground are generated for these twenty different positions.Algother since for one foreground there are  40 images on a specific background.A total of  40*100*100 =400K ForeGround-BackGround Images are generated.

A sample of  foreground-background images are shown in the Gallery below:

![](https://github.com/sudhakarmlal/EVA4/blob/master/Session14-15/Images/foregroundbackground.png)


#### 5. ForeGround-BackGround Masked Images:
Similiar to the way the ForeGround-BackGround Images are generated by Overlaying Foreground over BackGround,The mask images are overlayed over the background.Since 20 different positions the Mask Images are overlayed and the corresponding  20 flipped images are also overlayed. So a total of 40*100*100(100 BackGround,100 ForeGround Images) i.e 400K masked images are generated.

A sample of  foreground-background masked images are shown in the gallery below:

![](https://github.com/sudhakarmlal/EVA4/blob/master/Session14-15/Images/ForgroundBackGround_Mask.png)


#### 6. Depth Model Output Images:

A total of  400K depth model images are generated as an output of the depth model.

The gallery for sample of these 400K images are found below:

![](https://github.com/sudhakarmlal/EVA4/blob/master/Session14-15/Images/Depth.png)

5.Design Choices and Issues faced

- We have decided to take grey images as it will take less computation 
- We have decided to keep 10 batches of images so as to easier manage. For each batch, a separate zip file is created which will have fg, bg, fg_bg, mask, depth_fg_bg, black_msk. This will help in training as unit can be trained independently
- We have faced issues with colab and many of people report their good account is disabled. So we decided to run it only our own laptop with GPU and as the dataset is split 10 times, it was easier to upload to google drive, each batch of image
- The depth model when applied was very slow. So we changed teh batch size to 128 and chunks of files processed were 128 at a time. Also Pyplot methods clf() and cla() were used so that images were saved faster




      
      
      
      
      
      
      
      
      
     
     
     
     
     
     
     
     
     
     
     
     
