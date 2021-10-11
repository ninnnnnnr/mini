import os
from pathlib import Path

path_to_orig_img = input('Absolute path for directories with images: ')
path_to_orig_img = os.path.normpath(path_to_orig_img)
# 'C:\Python_work\tyres_photos.sample\tyres_photos'
# 'C:\Python_work\django\src\media\tyres'

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
GIF = []
FOLDERS = []
UNKNOWN = set()
OTHER = []
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "GIF": GIF
}


def get_extension(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ("JPEG", "JPG", "PNG", "GIF"):
                scan(item)
            continue

        extension = get_extension(item.name)
        new_name = folder / item.name
        if extension:
            try:
                current_container = REGISTERED_EXTENSIONS[extension]
                EXTENSION.add(extension)
                current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(new_name)


search_folder = Path(path_to_orig_img)
scan(search_folder)
list_origin_images = JPEG_IMAGES + JPG_IMAGES + PNG_IMAGES + GIF


#delete image in input path
for img in list_origin_images:
    os.remove(str(img))


