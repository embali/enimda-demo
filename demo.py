from os import listdir
from os.path import join, isfile
import time

from PIL import Image

from enimda import ENIMDA


SOURCE_CLEAR_PATH = './images/source/clear'         # Sources without border
SOURCE_BORDERED_PATH = './images/source/bordered'   # Bordered sources

DETECTED_CLEAR_PATH = './images/detected/clear'         # No border results
DETECTED_BORDERED_PATH = './images/detected/bordered'   # Bordered results


# Source files - clear and bordered, sorted alphabetically
source_clear_files = sorted(_ for _ in listdir(SOURCE_CLEAR_PATH)
                            if isfile(join(SOURCE_CLEAR_PATH, _)))
source_bordered_files = sorted(_ for _ in listdir(SOURCE_BORDERED_PATH)
                               if isfile(join(SOURCE_BORDERED_PATH, _)))


SIZE = 300      # Resize to 300px
RAND = 0.05     # Use 5 percent of all columns

# Process bordered images
rate = 0
for index, name in enumerate(source_bordered_files):
    im = Image.open(join(SOURCE_BORDERED_PATH, name))
    w, h = im.size
    w, h = (int(SIZE * w / h), SIZE) if w > h else (SIZE, int(SIZE * h / w))
    im = im.resize((w, h))
    em = ENIMDA(image=im)
    t = time.time()
    em.scan(rand=RAND, fast=True)
    t = time.time() - t
    rate += int(em.has_borders)
    em.outline()
    em.image.save(join(DETECTED_BORDERED_PATH, name))
    print(t, index, name, em.has_borders, em.borders)

print(rate / len(source_bordered_files))

# Process clear images
rate = 0
for index, name in enumerate(source_clear_files):
    im = Image.open(join(SOURCE_CLEAR_PATH, name))
    w, h = im.size
    w, h = (int(SIZE * w / h), SIZE) if w > h else (SIZE, int(SIZE * h / w))
    im = im.resize((w, h))
    em = ENIMDA(image=im)
    t = time.time()
    em.scan(rand=RAND, fast=True)
    t = time.time() - t
    rate += int(em.has_borders)
    em.outline()
    em.image.save(join(DETECTED_CLEAR_PATH, name))
    print(t, index, name, em.has_borders, em.borders)

print(rate / len(source_clear_files))
