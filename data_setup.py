import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report

# map_categories_all = {
#     'vhigh': 4, 'high': 3, 'med': 2, 'low': 1,
#     '2': 2, '3': 3, '4': 4, '5more': 5,
#     'small': 1, 'med': 2, 'big': 3,
#     'more': 5, 'unacc':0, 'acc':1, 'good':2, 'vgood':3
# }

map_categories_non_dep = {
    'vhigh': 4, 'high': 3, 'med': 2, 'low': 1,
    '2': 2, '3': 3, '4': 4, '5more': 5,
    'small': 1, 'med': 2, 'big': 3,
    'more': 5
}

def integer_mapping(data):
    # if (map == 'all'):
    #     for i in data.columns:
    #         data[i] = data[i].map(map_categories_all)
    #     return data
    # else:
    for i in data.columns[:-1]:
        data[i] = data[i].map(map_categories_non_dep)
    return data

def integer_training_setup(data):
    X = data.drop('class',axis=1)
    y = data['class']

    return train_test_split(X, y, test_size=0.2, random_state=302)


def oneHotEncoder_setup(data):
    encoder = OneHotEncoder()
    X = encoder.fit_transform(data.drop('class',axis=1))
    y = data['class']

    return train_test_split(X, y, test_size=0.2, random_state=302)
