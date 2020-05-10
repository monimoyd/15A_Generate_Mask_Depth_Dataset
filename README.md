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
      
      
 # 4. Explain how you created your dataset
     ## a. how were fg created with transparency
     ## b.		how were masks created for fgs
		
		- Sooraj
		
     ## c. how did you overlay the fg over bg and created 20 variants
     
     For each foreground image is overlayed randomly on each of the background image by using paste function of PIL library. We have chosen  (160x160) as dimension for background and (80x80) as dimension for foreground. While generating random position for 
     overlaying foreground on background, integer number is generated 20 times between 0 and 80 for both the x cordinate as well as y cordinate, using the function random.choice with  replace=False so that positions are not repeated. 
     
     In addition the each foreground image is horizonatlly flipped using function transpose from PIL library with option  PILImage.FLIP_LEFT_RIGHT and each of the flipped foreground image is also overlayed randomly on background image
     
     Similarly,teh mask image corresponding to the foregorund image is overlayed on black background randomly but correpdoing position
     as the original foreground image is overlayed
     
     
     

     
     
     ## d. how did you create your depth images? 
     
     The depth model is created using 
      
      
      
      
      
      
      
      
      
     
     
     
     
     
     
     
     
     
     
     
     
