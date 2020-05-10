import matplotlib.pyplot as plt
from PIL import Image as PILImage
import numpy as np
import os
import shutil
import sys


## This file is used for generating the foregroung  over background images and created 20 variants
## another 20 variant for flipped foreground over backgound. In addition, correpsonging mask images 
## are overlayed on teh black background
## This file expects five arguments:
## argument1 : foregroung images directory
## argument2: Background images directory
## argument3: Mask Images Directory
## argument4: Output directory for Overlayed foreground background image 
## argument5:  Output directory for Overlayed mask images on black backgournd
    

no_of_image_per_fg_bg = 20


def get_file_list(path) :
    return  [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
	

fg_images_dir = sys.argv[1]
bg_images_dir = sys.argv[2]
mask_images_dir = sys.argv[3]

fg_bg_result_dir = sys.argv[4]
mask_black_result_dir = sys.argv[5]



fg_image_file_list = get_file_list(fg_images_dir)
bg_image_file_list = get_file_list(bg_images_dir)
mask_image_file_list = get_file_list(mask_images_dir)

if os.path.exists(fg_bg_result_dir) == True:
    shutil.rmtree(fg_bg_result_dir)

if os.path.exists(mask_black_result_dir) == True:
    shutil.rmtree(mask_black_result_dir)


os.makedirs(fg_bg_result_dir)
os.makedirs(mask_black_result_dir)

for bg_image_file in bg_image_file_list:
    for fg_image_file, mask_image_file in zip(fg_image_file_list, mask_image_file_list):
        bg_no = bg_image_file[bg_image_file.index("bg_img_") + len("bg_img_"):bg_image_file.index(".png")]
        fg_no = fg_image_file[fg_image_file.index("fg_img_") + len("fg_img_"):fg_image_file.index(".png")]
		
        non_flip_x_position_list = np.random.choice(range(0,80), no_of_image_per_fg_bg, replace=False).tolist()
        non_flip_y_position_list = np.random.choice(range(0,80), no_of_image_per_fg_bg, replace=False).tolist()
		
        #new_non_flip_x_position_list = [int(elem) for elem in non_flip_x_position_list ]
        #new_non_flip_y_position_list = [int(elem) for elem in non_flip_y_position_list ]
		
		
		
        #print(" non_flip_x_position_list: " + str(non_flip_x_position_list) + " , non_flip_x_position_list type:" + str(type(non_flip_x_position_list)))
        #print(" non_flip_y_position_list: " + str(non_flip_y_position_list) + " , non_flip_y_position_list type:" + str(type(non_flip_y_position_list)))
        fg_image_size = (80, 80)
        foreground_img = PILImage.open(fg_images_dir + "/" + fg_image_file)
        foreground_img = foreground_img.resize(fg_image_size, PILImage.ANTIALIAS).convert("RGBA")
		
        mask_img = PILImage.open(mask_images_dir + "/" +  mask_image_file)
        mask_img = mask_img.resize(fg_image_size, PILImage.ANTIALIAS).convert("RGBA")
		
        
 
        #for non_flip_x_position, non_flip_y_position in enumerate(zip(non_flip_x_position_list,non_flip_y_position_list)):
        for i, (non_flip_x_position, non_flip_y_position) in enumerate(zip(non_flip_x_position_list, non_flip_y_position_list)): 		
            fg_bg_image_file = fg_bg_result_dir + "/fg_bg_" + str(fg_no) + "_" + str(bg_no) + "_" + "0_" + str(i+1) + ".png"
            background_img = PILImage.open(bg_images_dir + "/" + bg_image_file)
            #background_img.paste(foreground_img, (non_flip_x_position, non_flip_y_position), foreground_img)
            #print(" non_flip_x_position : " + str(non_flip_x_position) + " non_flip_x_position type : " + str(type(non_flip_x_position)))
            #print(" non_flip_y_position : " + str(non_flip_y_position) + " non_flip_y_position type : " + str(type(non_flip_y_position)))
            background_img.paste(foreground_img, (non_flip_x_position, non_flip_y_position), foreground_img)
            #background_img.paste(foreground_img, (20, 60), foreground_img)
            #background_img.save(fg_bg_image_file,"JPEG")
            background_img.save(fg_bg_image_file,"PNG")
			
            mask_black_image_file = mask_black_result_dir + "/bg_mask_" + str(fg_no) + "_" + str(bg_no) + "_" + "0_" + str(i+1) + ".jpg"
            black_img = PILImage.new('RGB', (160, 160), (0, 0, 0))
            black_img.paste(mask_img, (non_flip_x_position, non_flip_y_position),mask_img)
            black_img.save(mask_black_image_file, "PNG")

        flip_x_position_list = list(np.random.choice(range(0,80), no_of_image_per_fg_bg, replace=False).tolist())
        flip_y_position_list = list(np.random.choice(range(0,80), no_of_image_per_fg_bg, replace=False).tolist())
        fg_image_size = (80, 80)
        foreground_img = PILImage.open(fg_images_dir + "/" + fg_image_file)
        fg_flip_img  = foreground_img.transpose(PILImage.FLIP_LEFT_RIGHT)
        fg_flip_img = fg_flip_img.resize(fg_image_size, PILImage.ANTIALIAS).convert("RGBA")
        mask_img = PILImage.open(mask_images_dir + "/" +  mask_image_file)
        mask_flip_img  = mask_img.transpose(PILImage.FLIP_LEFT_RIGHT)
        mask_flip_img = mask_flip_img.resize(fg_image_size, PILImage.ANTIALIAS).convert("RGBA")		
        

        for i, (flip_x_position, flip_y_position)  in enumerate(zip(flip_x_position_list, flip_y_position_list)): 
            fg_bg_image_file = fg_bg_result_dir + "/fg_bg_" + str(fg_no) + "_" + str(bg_no) + "_" + "1_" + str(i+1) + ".png"
            background_img = PILImage.open(bg_images_dir + "/" + bg_image_file)
            background_img.paste(fg_flip_img, (flip_x_position, flip_y_position),fg_flip_img)
            background_img.save(fg_bg_image_file,"PNG")
			
            black_flip_image_file = mask_black_result_dir  + "/bg_mask_" + str(fg_no) + "_" + str(bg_no) + "_" + "1_" + str(i+1) + ".jpg"
            black_img = PILImage.new('RGB', (160, 160), (0, 0, 0))
            black_img.paste(mask_flip_img, (flip_x_position, flip_y_position),mask_flip_img)
            black_img.save(black_flip_image_file, "JPEG")

			
	