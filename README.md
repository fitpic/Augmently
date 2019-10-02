# 🖼️💥 Augmently  :
An Open Source library for Data Augmentation for image classification.\
Flip, Square crop & resisze your images, and add Salt and Pepper Noise.\
&nbsp;
# 📁Note On Folder Format:
Currently the library works only for image grouped each in their own class folder.
#### For example:
        ──My_animal_images_folder
            ├── Dogs
            │   ├── dog_img_1.jpg
            │   ├── dog_img_2.jpg
            │   ├── ...
            │   └── dog_img_n.jpeg
            ├── Cats
            ├── ...
            └── Elephants   
&nbsp;

# ⭐Start Using it:

Download the Augmently folder and place it in your project folder.
Then in your desired file write:

        from augmently.augmently import create_resized_cropped_square_class_images, create_salt_and_pepper_class_images, create_salt_and_pepper_class_images
        
        
# 🤖 The Functions:
&nbsp;
## 🔲 Crop to Square Size - create_resized_cropped_square_class_images()

### What it does:  
Creates a new folder with your images both resized and cropped to the square image length of your choice

### Arguments: 
image_data_path  (String) , output_path (string), square_length (Number)

### Example Usage:

    create_resized_cropped_square_class_images_in_new_folder("Desktop/image_folder", "Desktop/image_folder_square_resized_224pixels", 224 )

&nbsp;
&nbsp;
&nbsp;
## 🧂Salt and Pepper Noise - create_salt_and_pepper_class_images()

### What it does:  
Creates a new folder with your images with your desired amount of salt and pepper noise pixels added to your images

### Arguments: 
image_data_path (String) , output_path (String) , noise_amount (Number)

### Example Usage:

    create_salt_and_pepper_class_images_in_new_folder("Desktop/image_folder", "Desktop/image_folder_salt_pepper_0.05", 0.05 )


&nbsp;
&nbsp;
&nbsp;

## ↔️ Flip images - create_flipped_class_images()

### What it does:  
Creates a new folder with your images flipped

### Arguments: 
image_data_path (String) , output_path (string)

### Example Usage:

    create_flipped_class_images_in_new_folder("Desktop/image_folder", "Desktop/image_folder_flipped")

