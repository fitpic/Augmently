# Crop to Square and resize
# import inbuilt libs
import os
from os import listdir
from os.path import isfile, join
import stat

# pip dependancies
import cv2 # opencv-python
from PIL import Image # Pillow
import numpy as np # numpy


def crop_to_square(im):
    im = Image.fromarray(im)
    width, height = im.size   # Get dimensions

    # Make square using smallest side
    if(width > height):
        new_width = height
        new_height = height
    else: 
        new_width = width
        new_height = width

    # centre the image
    left = (width - new_width)/2
    top = (height - new_height)/2
    right = (width + new_width)/2
    bottom = (height + new_height)/2

    # Crop the center of the image
    im = im.crop((left, top, right, bottom))
    
    return im


def resize_to_shape(im, square_length):
    dim = (square_length, square_length)
    resized = cv2.resize(np.array(im), dim, interpolation = cv2.INTER_AREA)

    return resized

def create_resized_cropped_square_class_images_in_new_folder(image_data_path, output_path, square_length):
    
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    if not os.path.exists(image_data_path):
        print("input image data folder does not exist!")
        return

    for file in os.listdir(image_data_path):
         if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                print("Please format your image date folder to cotntain folders of the classes with class images inside")
                return

    for direc in os.walk(image_data_path):
        class_folder = direc[0]
        if(class_folder != image_data_path):
            for img_name in listdir(class_folder):
                if not img_name.startswith(".") and (img_name.endswith('.png') or img_name.endswith('.jpg') or img_name.endswith('.jpeg')):

                    class_img = class_folder.split("/")[-1]
                    class_folder = image_data_path+"/"+ class_img
                    output_class_folder = output_path +"/"+ class_img
                    if not os.path.exists(output_class_folder):
                        os.mkdir(output_class_folder)

                    path = class_folder + '/' + img_name
                    img = np.array(Image.open(path))
                    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    new_img_path = output_class_folder + '/'+ img_name

                    square_crop_img = resize_to_shape( crop_to_square(img), square_length)
                    new_square_crop_img_path = output_class_folder + '/'+str(square_length)+"_squareCrop" + img_name 

                    cv2.imwrite(new_img_path, img)
                    cv2.imwrite(new_square_crop_img_path, square_crop_img)



# SALT AND PEPPER

def sp_noise(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def create_salt_and_pepper_class_images_in_new_folder (image_data_path, output_path, noise_amount):
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    if not os.path.exists(image_data_path):
        print("input image data folder does not exist!")
        return

    for file in os.listdir(image_data_path):
         if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                print("Please format your image date folder to cotntain folders of the classes with class images inside")
                return

    for direc in os.walk(image_data_path):
        class_folder = direc[0]
        if(class_folder != image_data_path):
            for img_name in listdir(class_folder):
                if not img_name.startswith(".") and (img_name.endswith('.png') or img_name.endswith('.jpg') or img_name.endswith('.jpeg')):

                    class_img = class_folder.split("/")[-1]
                    class_folder = image_data_path+"/"+ class_img
                    output_class_folder = output_path +"/"+ class_img
                    if not os.path.exists(output_class_folder):
                        os.mkdir(output_class_folder)

                    path = class_folder + '/' + img_name
                    img = np.array(Image.open(path))
                    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    new_img_path = output_class_folder + '/'+ img_name

                    salt_pepper_img = np.array(sp_noise(img,noise_amount))
                    new_salt_pepper_img_path = output_class_folder + '/'+"salt_pepper_" + img_name 

                    cv2.imwrite(new_img_path, img)
                    cv2.imwrite(new_salt_pepper_img_path, salt_pepper_img)


# IMAGE FLIPS

def has_hidden_attribute(filepath):
    return bool(os.stat(filepath).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)

def create_flipped_class_images_in_new_folder (image_data_path, output_path):
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    if not os.path.exists(image_data_path):
        print("input image data folder does not exist!")
        return

    for file in os.listdir(image_data_path):
         if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                print("Please format your image date folder to cotntain folders of the classes with class images inside")
                return

    for direc in os.walk(image_data_path):
        class_folder = direc[0]
        if(class_folder != image_data_path):
            for img_name in listdir(class_folder):
                if not img_name.startswith(".") and (img_name.endswith('.png') or img_name.endswith('.jpg') or img_name.endswith('.jpeg')):

                    class_img = class_folder.split("/")[-1]
                    class_folder = image_data_path+"/"+ class_img
                    output_class_folder = output_path +"/"+ class_img
                    if not os.path.exists(output_class_folder):
                        os.mkdir(output_class_folder)

                    path = class_folder + '/' + img_name
                    img = np.array(Image.open(path))
                    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    new_img_path = output_class_folder + '/'+ img_name


                    flipped_img = np.array(np.fliplr(img))
                    new_flipped_img_path = output_class_folder + '/'+"flipped" + img_name 

                    cv2.imwrite(new_img_path, img)
                    cv2.imwrite(new_flipped_img_path, flipped_img)
            
