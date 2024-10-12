
### Exercise: Building a Simple Convolutional Neural Network (CNN) for Handwritten Digit Recognition

**Objective**: 
In this exercise, you will build a basic Convolutional Neural Network (CNN) using Python and TensorFlow/Keras to recognize handwritten digits from the MNIST dataset.

**Prerequisites**:
- Basic knowledge of Python programming
- Understanding of neural networks and deep learning concepts
- Familiarity with TensorFlow/Keras

**Dataset**: MNIST Handwritten Digits

### Step-by-Step Guide:

#### Step 1: Setup and Imports
- Install TensorFlow if you haven't already using the command `pip install tensorflow`.
- Import the necessary libraries for the exercise.

#### Step 2: Load and Preprocess the Data
- Load the MNIST dataset.
- Reshape and normalize the data to fit the model requirements.
- One-hot encode the labels for the output layer.

#### Step 3: Build the Basic CNN Model
- Define a CNN model using the Sequential API from Keras.
- Add the following layers:
  - **Convolutional Layer**: Extracts features from the input image.
  - **Max Pooling Layer**: Reduces the spatial dimensions of the feature maps.
  - **Flatten Layer**: Converts the 2D feature maps into a 1D feature vector.
  - **Fully Connected (Dense) Layer**: Maps the extracted features to the output classes.
  - **Output Layer**: Produces the final classification.

#### Step 4: Compile the Model
- Compile the model using an appropriate optimizer, loss function, and evaluation metric.

#### Step 5: Train the Model
- Train the model on the training data using the `fit` method.
- Validate the model using the test data.

#### Step 6: Evaluate the Model
- Evaluate the model's performance on the test data.
- Print out the test loss and accuracy.

#### Step 7: Make Predictions
- Use the trained model to make predictions on the test data.
- Visualize some of the predictions along with the actual labels.

### Exercise Deliverables:
1. **Code Implementation**: Submit your Python code for the entire process from data loading to evaluation.
2. **Model Performance**: Report the model's test accuracy and loss.
3. **Predictions Visualization**: Provide visualizations of at least 5 test samples along with their predicted and actual labels.

### Additional Challenges:
- Experiment with different architectures by adding more layers or changing the number of filters in the convolutional layers.
- Implement data augmentation to improve the model's performance.
- Save and load the trained model using `model.save()` and `tf.keras.models.load_model()`.

By completing this simplified exercise, you will gain practical experience in building and training a basic CNN for image recognition tasks using TensorFlow/Keras.