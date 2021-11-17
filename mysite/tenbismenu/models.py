from django.db import models

# # Create your models here.

import json


path = '/data.json'
f = open('data.json')
data = json.load(f)
# # for cat in data['Data']['categoriesList']:
# #     print(cat['categoryName'])
z=2

# # class Data(models.Model):
