from PIL import Image
import os
import glob


# for add watermark on right position
def size_img(input_image_path):
    image = Image.open(input_image_path)
    size = image.size
    return size


# watermark function
def watermark_photo(input_image_path,
                    output_image_path,
                    watermark_image_path, position):
    base_image = Image.open(input_image_path)
    if base_image.mode == "CMYK":
        base_image = base_image.convert("RGB")
    watermark = Image.open(watermark_image_path)
    base_image.paste(watermark, position, mask=watermark)
    # base_image.show()
    base_image.save(output_image_path, format='png')


path_to_orig_img = os.path.abspath(input('Absolute path for directories with original images: '))
# 'C:\Python_work\tyres_photos.sample\tyres_photos'
path_to_logo = os.path.abspath(input('Absolute path for logo images: '))
# # 'C:\Python_work\\tyres_photos.sample\logo.png'
path_to_save = os.path.abspath(input('Input absolute path for folder images save: '))
# # 'C:\Python_work\tyres_photos.sample\gotovo'


# create list for path images
list_origin_images = glob.glob(path_to_orig_img + '/**/*.*', recursive=True)


#create path to new directory
list_images_with_logo = []
list_new_folders = []
for img in list_origin_images:
    img = os.path.relpath(img, start=path_to_orig_img)
    img = os.path.join(path_to_save, img)
    list_images_with_logo.append(img)
    new_folder = os.path.dirname(img)
    list_new_folders.append(new_folder)


# add watermark on image
for img, path_save, path_new_folder in zip(list_origin_images, list_images_with_logo, list_new_folders):
    size_image = size_img(img)
    x = size_image[0]
    y = size_image[1]
    os.makedirs(path_new_folder, exist_ok=True)
    watermark_photo(img, path_save, path_to_logo, position=(x - 141, y - 29))


