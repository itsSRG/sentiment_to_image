from nltk.sentiment import SentimentIntensityAnalyzer
from scipy import rand
from PIL import Image
import random
import os

def paste_specific(random_row, random_column, list_of_img_name):
    for i in range(0, len(random_row)):
        image_list = list_of_img_name
        img_pos = Image.open(random.choice(image_list))
        img_pos = img_pos.resize((250,250))
        temp = random.randint(0,100)
        if temp < 25:
            img_pos = img_pos.rotate(90)
        elif temp < 50:
            img_pos = img_pos.rotate(180)
        elif temp < 75:
            img_pos = img_pos.rotate(270)
        collage.paste(img_pos, (random_column[i]*250, random_row[i]*250))
        img_pos.close()

list_of_files = os.listdir()
positive = [i for i in list_of_files if 'hap' in  i]
negative = [i for i in list_of_files if 'sad' in i]
neutral = [i for i in list_of_files if 'neu' in i]

sia = SentimentIntensityAnalyzer()
my_day = input()
score = sia.polarity_scores(my_day)
print(score)
# {'neg': 0.0, 'neu': 0.0, 'pos': 1.0, 'compound': 0.4404}

from PIL import Image, ImageEnhance
collage = Image.new("RGB", (2500,2500), (255,255,255))

c=0.7
row = [i for i in range (10)]
column = [j for j in range(10)]

random_row_neu = [i for j in range (10) for i in range (10)]
random_column_neu = [j for j in range (10) for i in range (10)]
# print(random_row_neu)
# print(random_column_neu)
random_row_pos = random.choices(row, k = int(score['pos']*100))
random_column_pos = random.choices(column, k = int(score['pos']*100))

random_row_neg = random.choices(row, k = int(score['neg']*100))
random_column_neg = random.choices(column, k = int(score['neg']*100))

# print(random_column_pos)
# print(random_row_pos)

paste_specific(random_row=random_row_neu, random_column=random_column_neu, list_of_img_name=neutral)
paste_specific(random_row=random_row_pos, random_column=random_column_pos, list_of_img_name=positive)
paste_specific(random_row=random_row_neg, random_column=random_column_neg, list_of_img_name=negative)


collage.show()