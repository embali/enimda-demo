from os import listdir
from os.path import join, isfile
import time

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
COLUMNS = 100   # Use 100 columns at maximum
FAST = True     # Fast or precise scan


# Process bordered images
rate = 0
for index, name in enumerate(source_bordered_files):
    em = ENIMDA(fp=join(SOURCE_BORDERED_PATH, name), size=SIZE)
    t = time.time()
    borders = em.scan(columns=COLUMNS, fast=FAST)
    t = time.time() - t
    rate += int(any(borders))
#    em.outline()
#    em.save(fp=join(DETECTED_BORDERED_PATH, name))
    print(t, index, name, any(borders), borders)
print(rate / len(source_bordered_files))

# Process clear images
rate = 0
for index, name in enumerate(source_clear_files):
    em = ENIMDA(fp=join(SOURCE_CLEAR_PATH, name), size=SIZE)
    t = time.time()
    borders = em.scan(columns=COLUMNS, fast=FAST)
    t = time.time() - t
    rate += int(any(borders))
#    em.outline()
#    em.save(fp=join(DETECTED_CLEAR_PATH, name))
    print(t, index, name, any(borders), borders)
print(rate / len(source_clear_files))
