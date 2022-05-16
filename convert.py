from PIL import Image
import os

list_of_files = os.listdir()
positive = [i for i in list_of_files if 'hap' in  i]
negative = [i for i in list_of_files if 'sad' in i]
neutral = [i for i in list_of_files if 'neu' in i]

for i in positive:
    img_pos = Image.open(i)
    img_pos = img_pos.resize((250,250))
    img_pos = img_pos.save(i + '_c'+'.png')

for i in negative:
    img_pos = Image.open(i)
    img_pos = img_pos.resize((250,250))
    img_pos = img_pos.save(i + '_c'+'.png')

for i in neutral:
    img_pos = Image.open(i)
    img_pos = img_pos.resize((250,250))
    img_pos = img_pos.save(i + '_c'+'.png')