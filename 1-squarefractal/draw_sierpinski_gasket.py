from PIL import Image, ImageDraw
import numpy as np
import copy

#Makes an image size 2n * n
n = 1500
img = Image.new( 'RGB', (2*n, 2*n), (50, 50, 50)) #
draw = ImageDraw.Draw(img)

#dict1 is the dictionary pairing coefficients (minus 1) with coordinate pair
#dict2 is a temporary dictionary used to prevent IO errors.
dict1 = {(0,):(n, 0.1*n)}
depth = 5
for i in range(depth):
    r = 400 * 0.5 ** i
    dict2 = copy.deepcopy(dict1)
    for key in dict1.keys():
        # twist = len(key)% 4 - 1
        if len(key) == i+1:
            dict2[key + (-1,)] = (dict2[key][0]+r, dict2[key][1])
            dict2[key + (0,)] = (dict2[key][0], dict2[key][1]+ r*np.sqrt(3))
            dict2[key + (1,)] = (dict2[key][0]-r, dict2[key][1])

    dict1 = copy.deepcopy(dict2)

for key in dict1:
    thickness = 10
    (x,y) = dict1[key]

    #Draws lines between all vertices
    # if len(key) <= depth:
    #     (xn1, yn1) = dict1[key + (-1,)]
    #     (x0, y0) = dict1[key + (0,)]
    #     (x1, y1) = dict1[key + (1,)]
    #     draw.line((x,y, xn1,yn1), width = thickness, fill = "blue")
    #     draw.line((x,y, x0,y0), width = thickness, fill = "red")
    #     draw.line((x,y, x1,y1), width = thickness, fill = "green")



    #Comment/Uncomment this to draw vertices of random color
    color = (np.random.randint(256), np.random.randint(256), np.random.randint(256))
    draw.ellipse((x - thickness, y - thickness, x + thickness, y + thickness), fill=color)

#Saves / Shows Image
#img.save("C:\\Users\\Eduardo Zamora\\Pictures\\dots.png")
img.show()
