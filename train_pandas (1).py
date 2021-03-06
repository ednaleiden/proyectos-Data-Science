# -*- coding: utf-8 -*-
"""train pandas

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LlrEPrVOgwG72S3DOEhMp_A-0RPbOF6e
"""

import numpy as np
import pandas as pd 
import os
import matplotlib.pyplot as plt

train_data=pd.read_csv("preprocessed_train_data.csv")
train_data.head()

type(train_data)

train_data

plt.pie(train_data["MSSubClass"].value_counts())
plt.show()

plt.pie(train_data["LotFrontage"].value_counts())
plt.show()

plt.pie(train_data["YearBuilt"].value_counts()),(train_data["OverallQual"].value_counts()),(train_data["MSSubClass"].value_counts())
plt.show()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
train_data["LotArea"] = le.fit_transform(train_data["LotArea"])

columns = train_data[["Id",	"MSSubClass",	"LotFrontage","LotArea"	,"OverallQual",	"OverallCond","YearBuilt","YearRemodAdd"]]