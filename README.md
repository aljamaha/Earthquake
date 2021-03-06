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

Although the testing accuracy is high, it was challenging to further improve the model. The feature extraction (getting 24 information from each wavefunction), might not have been adequate to sufficiently describe the model. A neural network that takes the input from a full wavefunction might be more appropriate since there is no loss of information in such cases. 

### Libraries needed:

numpy, h5py, matplotlib, and tensorflow

## data_extraction.py:
script used to extract features based on a wavefuction

## NN.py:
script used to train and test the neural network

## Model Robustness and Limitations:

The model so far can predict an earthquake with 90% accuracy. The prediction does not give an exact number, but a range (<3, 4-5, >5). This is a limitaiton since ideally the model should predict exactly the magnitude of the earthquake. Other possibility to improve the model is by using an alternative archeticture, for example, a 1-D convolutional neural network. I believe we have reached close to the limit of a fully connected network based on varying many parameters and finding near-optimal solution.

As mentioned earlier, the model could be improved by dealing with the input as a full wavefunction instead of reducing it into a 24 parameter input. It could also be improved by using a principal component analysis, where instead of 24 features, the most important features are used.

## Conclusion:

A fully connected neural network was trained to predict earthquake mangitude based on >300,000 wavefuctions as in input. Each wavefunction was converted into a 24 parameter input based on various features. The neural network was finely tuned and resulted in 90% accuracy of test data.
