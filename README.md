# Earthquake

## Objective:

Accurate and early detection of earthquakes is of critical importance in formulating an effective response. Hundreds of thousands of humans are in a constant state of danger due to living in areas vulnerable to earthquakes. The problem is compounded if the area experiences constant low magnitude earthquakes that, although does not pose danger to human lives, present a challenge in evaluating the potential danger of the earthquake. Generally, an earthquake of magnitude less than 4 does not constitute a danger. However, a higher magnitude earthquake demands an immediate response. The current detection system generally evaluates the earthquake magnitudes correctly in roughly 90% of the time, however, the response time is not quick enough.

## Preprocessing:

The script data_extraction.py is responsible for taking the raw data and transforming them into an input for the machine learning algorithm. 24 features were extracted from each wavefunction and fed to the neural network based on various aspects of the wavefunction. Noise was separated from the real earthquake as well to make sure quality input is added to the model.

## Data Understanding and Modeling:

Over 300,000 wavefunctions were used to train a neural network and predict the order of earthquake magnitude. 24 features were extracted from each wavefunction and fed to the neural network. Based on the large size of the database (>10 GB), it can be provided per request. The data generally gathered from the USGS.

## Metrics Discussion and Refinement:

For this work, I have decided to go with a fully connected neural network. There are many aspects of the network that could affect the performance. I have examined the effect of number of layers (3,5, and 10 layers gave similar accuracies), beta and L2 normalization (0.1, 0.001, and 0.0001 where the latter was the most critical), and lastly, the distribution between split of input data with earthquakes and no-earthquake. I found an evenly split is best.

## Evaluation:

The most important metric in evaluating the performance of the model is accuracy of predciting the earthquake magnitude. Accuracy >85% is required since the peroormance will be similar to existing methods, however, the algorithm should be much quicker in that aspect. Based on the trained dataset, the model predicts for a new wavefunction if an earthquake will happen or not. The testing accuracy is indeed >85%.

### Libraries needed:

numpy, h5py, matplotlib, and tensorflow

## data_extraction.py:
script used to extract features based on a wavefuction

## NN.py:
script used to train and test the neural network

## Model Robustness and Limitations:

The model so far can predict an earthquake with 90% accuracy. The prediction does not give an exact number, but a range (<3, 4-5, >5). This is a limitaiton since ideally the model should predict exactly the magnitude of the earthquake. Other possibility to improve the model is by using an alternative archeticture, for example, a 1-D convolutional neural network. I believe we have reached close to the limit of a fully connected network based on varying many parameters and finding near-optimal solution.
