from PIL import Image
import glob

if __name__ == "__main__":
    import os
    path = './zarbis'
    os.chdir(path)
    tab_size = []
    allequal = True
    for file in glob.glob('*.png'):
        img = Image.open(file)
        width, height = img.size
        tab_size.append(height)
    
    previous_size = tab_size[0]
    for size in tab_size:
        if size != previous_size:
            allequal = False

    if allequal:
        print('everything image has the same height')
    else:
        print('there is change in height, please check the height of all the images')