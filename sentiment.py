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


from PIL import Image, ImageEnhance
collage = Image.new("RGB", (2500,2500), (255,255,255))

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
        image_list = ['neu1.png','neu2.png','neu3.png','neu4.png', 'neu5.png', 'neu6.png', 'neu7.png']
        img_neu = Image.open(random.choice(image_list))
        img_neu = img_neu.resize((250,250))
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
        img_neu.close()

for i in range(0, len(random_row_pos)):
    image_list = ['fh1.png','fh2.png','fh3.png','fh4.png']
    img_pos = Image.open(random.choice(image_list))
    img_pos = img_pos.resize((250,250))
    temp = random.randint(0,100)
    if temp < 25:
        img_pos = img_pos.rotate(90)
    elif temp < 50:
        img_pos = img_pos.rotate(180)
    elif temp < 75:
        img_pos = img_pos.rotate(270)
    collage.paste(img_pos, (random_column_pos[i]*250, random_row_pos[i]*250))
    img_pos.close()

c = 0.7
for i in range(0, len(random_row_neg)):
    image_list = ['fs1.png']
    img_neg = Image.open(random.choice(image_list))
    img_neg = img_pos.resize((250,250))
    temp = random.randint(0,100)
    if temp < 25:
        img_neg = img_neg.rotate(90)
    elif temp < 50:
        img_neg = img_neg.rotate(180)
    elif temp < 75:
        img_neg = img_neg.rotate(270)
    collage.paste(img_neg, (random_column_neg[i]*250, random_row_neg[i]*250))
    img_neg.close()

collage.show()