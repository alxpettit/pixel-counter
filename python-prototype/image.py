#!/usr/bin/env python3
from PIL import Image
Image.MAX_IMAGE_PIXELS = int(1024*1024*1024)                                    

#target_colors = [[[154, 217, 234], 0], [[63, 71, 204], 0], [[239, 227, 175], 0]]
target_colors = [[[255, 255, 255], 0],
[[0, 0, 255], 0],
[[0, 200, 200], 0],
[[255, 255, 0], 0],
[[0, 100, 0], 0],
[[255, 0, 255], 0],
[[0, 255, 255], 0],
[[0, 255, 0], 0],
[[255, 100, 0], 0],
[[0, 200, 0], 0],
[[255, 0, 0], 0],
[[0, 70, 0], 0],
[[200, 200, 0], 0],
[[200, 200, 200], 0],
[[150, 150, 150], 0]]

# if `b` is within `within` of `a` in either direction, return true
# else return false
def proximate(a, b, within):
    for i in range(b-within, b+within):
        if a == i:
            return True
    return False

pic = Image.open('map1.jpg')
rgbpic = pic.convert('RGB')

WITHIN_VALUE = 5
range_3 = range(3)
matching = 0

print("Starting values: ")
for target_color in target_colors:
    print(str(target_color[0]) + ": " + str(target_color[1]))

for pixel in rgbpic.getdata():
    for target_color in target_colors:
        matching = 0
        for i in range_3:
            if proximate(pixel[i], target_color[0][i], WITHIN_VALUE):
                matching += 1
        if matching == 3:
            target_color[1] += 1

print("Ending values: ")
for target_color in target_colors:
    print(str(target_color[0]) + ": " + str(target_color[1]))

