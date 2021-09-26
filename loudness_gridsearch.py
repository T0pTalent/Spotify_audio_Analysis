#!/usr/bin/python

from gridsearch import grid_search
from tensorflow.keras.losses import *

# Hyper-parameters for Grid Search
layer_types = ['relu', 'linear']
layer_counts = [1, 3, 5]
neuron_counts = [250, 500, 750, 1000]
loss_functions = [MeanSquaredError()]

# Run grid search
if __name__ == "__main__":
    grid_search("loudness", layer_types, layer_counts, neuron_counts, loss_functions)
