#!/usr/bin/env python
# encoding: utf-8
import json
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify

app = Flask(__name__)
model = tf.keras.models.load_model('model/model.h5')


@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'OK'})


@app.route('/predict', methods=['POST'])
def predict():
    param = json.loads(request.data)
    tokens = param['data'].split(",")
    image = np.array([int(i) for i in tokens])
    image = image.reshape((1, -1)) / 255.0
    predictions = model.predict(image)
    # Generate arg maxes for predictions
    classes = np.argmax(predictions, axis=1)
    return jsonify({'predicted': str(classes[0])})
