from dataclasses import replace
from nltk.sentiment import SentimentIntensityAnalyzer
from scipy import rand
sia = SentimentIntensityAnalyzer()
my_day = input()
score = sia.polarity_scores(my_day)
print(score)
# {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.4404}

from PIL import Image, ImageEnhance
import random


img_neu = Image.open("vines1.png")
img_neu = img_neu.resize((250,250))

from PIL import Image, ImageEnhance
collage = Image.new("RGB", (2500,2500), (255,255,255))

img_pos = Image.open("f11.png")
img_pos = img_pos.resize((250,250))

img_neg = Image.open("f22.png")
img_neg = img_neg.resize((250,250))

c=0.7
row = [i for i in range (10)]
column = [j for j in range(10)]

random_row_pos = random.choices(row, k = int(score['pos']*100))
random_column_pos = random.choices(column, k = int(score['pos']*100))

random_row_neg = random.choices(row, k = int(score['neg']*100))
random_column_neg = random.choices(column, k = int(score['neg']*100))

print(random_column_pos)
print(random_row_pos)

for i in range(0, 2500, 250):
    for j in range(0, 2500, 250):
        
        temp = random.randint(0,100)
        if temp < 25:
            rot_image = img_neu.rotate(90)
            collage.paste(rot_image, (j,i))
        elif temp < 50:
            rot_image = img_neu.rotate(180)
            collage.paste(rot_image, (j,i))
        elif temp < 75:
            rot_image = img_neu.rotate(270)
            collage.paste(rot_image, (j,i))
        else:
            collage.paste(img_neu, (j,i))
            

for i in range(0, len(random_row_pos)):
    new_img = img_pos
    temp = random.randint(0,100)
    if temp < 25:
        new_img = img_pos.rotate(90)
        # collage.paste(rot_image, (j,i))
    elif temp < 50:
        new_img = img_pos.rotate(180)
        # collage.paste(rot_image, (j,i))
    elif temp < 75:
        new_img = img_pos.rotate(270)
        # collage.paste(rot_image, (j,i))
    collage.paste(new_img, (random_column_pos[i]*250, random_row_pos[i]*250))

c = 0.7
for i in range(0, len(random_row_neg)):
    # new_img = colour.enhance(0)
    collage.paste(img_neg, (random_column_neg[i]*250, random_row_neg[i]*250))

collage.show()