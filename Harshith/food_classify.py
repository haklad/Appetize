# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 20:10:08 2019

@author: admin
"""

import numpy as np
import os
import time
from keras.applications.resnet50 import ResNet50
from keras.preprocessing import image
from keras.layers import GlobalAveragePooling2D, Dense, Dropout,Activation,Flatten

from keras_applications.imagenet_utils import _obtain_input_shape
from keras.applications.inception_v3 import preprocess_input
from keras_applications.imagenet_utils import decode_predictions

#from keras_applications.imagenet_utils import preprocess_input
#from keras_applications.imagenet_utils import _obtain_input_shape


from keras.layers import Input
from keras.models import Model
from keras.utils import np_utils
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

IMAGE_SIZE = 224

PATH = os.getcwd()

# Define data path
data_path = PATH + '/dataset/indian-food'
data_dir_list = os.listdir(data_path)

img_data_list=[]

for dataset in sorted(data_dir_list):
    img_list=os.listdir(data_path+'/'+ dataset)[:100]
    print ('Loaded the images of dataset-'+'{}\n'.format(dataset))
    for img in img_list:
        img_path = data_path + '/'+ dataset + '/'+ img 
        img = image.load_img(img_path, target_size=(IMAGE_SIZE, IMAGE_SIZE))
        x = image.img_to_array(img)
        x = preprocess_input(x)
        # print('Input image shape:', x.shape)
        img_data_list.append(x)
        
img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
print(img_data.shape)

# Define the number of classes
num_classes = 7
num_of_samples = (img_data.shape[0])
labels = np.ones((num_of_samples,), dtype='int64')

labels[:101]=0
labels[101:201]=1
labels[201:301]=2
labels[301:401]=3
labels[401:501]=4
labels[501:601]=5
labels[601:]=6

names = ['briyani', 'dhosa', 'gulab-jamun', 'jalebi', 'momo', 'samosa', 'tantoori-chicken']
# convert class Labels to one-hot encoding
Y = np_utils.to_categorical(labels, num_classes)

# Shuffle the dataset
x, y= shuffle(img_data, Y, random_state=2)
# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

model = ResNet50(weights='imagenet', include_top=False)


last_layer = model.output

# add a global spatial average pooling layer
x = GlobalAveragePooling2D()(last_layer)

# Add fully connected & dropout layers
x = Dense(512, activation='relu', name='fc-1')(x)
x = Dropout(0.5)(x)
x = Dense(256, activation='relu', name='fc-2')(x)
x = Dropout(0.5)(x)

# softmax layer for 5 classes
out = Dense(num_classes, activation='softmax', name='output_layer')(x)

custom_resnet_model2 = Model(model.input, outputs=out)

for layer in custom_resnet_model2.layers[:-10]:
    layer.trainable = False
    
custom_resnet_model2.layers[-1].trainable
                          
                           
custom_resnet_model2.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# training model
t=time.time()
hist = custom_resnet_model2.fit(X_train, y_train, batch_size=32, epochs=11, verbose=1, validation_data=(X_test, y_test))
print('Training time: %s secs' % (time.time() - t ))

(loss, accuracy) = custom_resnet_model2.evaluate(X_test, y_test, batch_size=10, verbose=1)
print('[INFO] loss = {:.4f}, accuracy: {:.4f}%'.format(loss, accuracy * 100))

custom_resnet_model2.save_weights('FIC-In-{C7}-{B32}-{E11}.h5', overwrite=True)

# Serialize model to JSON
model_json = custom_resnet_model2.to_json()
with open('FIC-In-{C7}-{B32}-{E11}.h5.json', 'w') as json_file:
    json_file.write(model_json)


import json
from keras.models import model_from_json, load_model

#custom_resnet_model2 = load_model('my_model3.h5')

import pandas as pd
import matplotlib.pyplot as plt



images = ['dhosa_115.jpg', 'briyani_122.jpg', 'momo_478.jpg']

#images = ['pizza.jpg']



for img in images:
    img_path = img
    #width, height = cv.GetSize(img_path)
    img = image.load_img(img_path, target_size=(100,100,3))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    print('Input image shape:', x.shape)

    preds = custom_resnet_model2.predict(x)
    custom_resnet_model2.summary()
    print('Image: ')
    plt.imshow(img)
    plt.show()
    print(preds)


    print('\nPrediction:', end='\n\n')
    preds = preds[0]
    prob_dist = []
    for i in range(len(preds)):
        prob_dist.append([names[i], preds[i]*100])
    df = pd.DataFrame(prob_dist, columns=['Class', 'Prob-percent'])
    print(df)
    print('--------------------------------------------------------------------------', end='\n\n\n')


