# Earthquake

## Objective:

Accurate and early detection of earthquakes is of critical importance in formulating an effective response. Hundreds of thousands of humans are in a constant state of danger due to living in areas vulnerable to earthquakes. The problem is compounded if the area experiences constant low magnitude earthquakes that, although does not pose danger to human lives, present a challenge in evaluating the potential danger of the earthquake. Generally, an earthquake of magnitude less than 4 does not constitute a danger. However, a higher magnitude earthquake demands an immediate response. The current detection system generally evaluates the earthquake magnitudes correctly in roughly 90% of the time.

## Data Understanding and Modeling:

Over 300,000 wavefunctions were used to train a neural networ and predict the order of earthquake magnitude. 24 features were extracted from each wavefunction and fed to the neural network.

## Evaluation:

Based on the trained dataset, the model predicts for a new wavefunction if an earthquake will happen or not. The testing accuracy is >85%.


### Libraries needed:

numpy, h5py, matplotlib, and tensorflow

## data_extraction.py:
script used to extract features based on a wavefuction

## NN.py:

script used to train the neural network
