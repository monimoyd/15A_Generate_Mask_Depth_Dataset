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
     
     
     fg_jpg : Foreground jpg images of size (160x160) with each image is uniquely numbered across batches e.g. fg_img_91.jpg
     bg_jpg : Background jpeg images of size (160x160) with each image is uniquely numbered  but repeated across batches e.g. bg_img_5.jpg
     fg_bg_jpg : Foreground images overlayed on background images of size (160x160) with each image is uniquely numbered as
     fg_bg_1_4_0_15 where the first digit 1 represents the foreground image id from which it is generated
      second digit 4 represents the background image id from which it is generated, 0 represents, this image is not flipped (if flipped it will have value 1), last digit 15 represents the sequence number (1-20)
      mask_black_jpg: Mask image overlayed on black background with each image is uniquely numbered as
     bg_mask_1_4_0_15 where the first digit 1 represents the foreground image id from which it is generated
      second digit 4 represents the background image id from which it is generated, 0 represents, this image is not flipped (if flipped it will have value 1), last digit 15 represents the sequence number (1-20)
      
      
      
      
      
     
     
     
     
     
     
     
     
     
     
     
     
