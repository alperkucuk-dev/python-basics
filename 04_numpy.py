import numpy as np

image = np.array([
    [ 10,  20,  30,  40,  50],
    [ 60, 200, 210, 220,  70],
    [ 80, 230, 240, 250,  90],
    [100, 110, 120, 130, 140],
], dtype=np.uint8)

shape_image = image.shape
average_brightnes = image.mean()
max_bright_pixel = image.max()
min_bright_pixel = image.min()

crop = image[1:3 , 1:4]

txt = f"Shape of image is : {shape_image}, average brightness: {average_brightnes}, maximum bright pixel: {max_bright_pixel}, minimum bright pixel: {min_bright_pixel} "

print(txt)
print(crop)

mask = np.where(image > 128, 255,0)

print(mask)