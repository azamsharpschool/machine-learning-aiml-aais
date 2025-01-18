### Exercise: Training a Neural Network on the Fashion MNIST Dataset

#### Objective:
In this exercise, you will build, compile, and train a neural network to classify images from the Fashion MNIST dataset using TensorFlow and Keras. This exercise will help you understand the basics of neural networks, data preprocessing, and model evaluation.

#### Steps to Complete:

1. **Import Necessary Libraries**
    - Ensure you have TensorFlow installed (`pip install tensorflow` if not).
    - Import TensorFlow and Keras.

2. **Load and Explore the Dataset**
    - Load the Fashion MNIST dataset.
    - Examine the shapes of the training and testing datasets.
    - Plot a few images to understand what the dataset looks like.

3. **Normalize the Data**
    - Normalize the pixel values of the images to be between 0 and 1.

4. **Build the Neural Network Model**
    - Define a Sequential model.
    - Add a Flatten layer to convert each 28x28 image to a 784-element array.
    - Add a Dense layer with 128 neurons and ReLU activation.
    - Add another Dense layer with 10 neurons and softmax activation.

5. **Compile the Model**
    - Use the Adam optimizer.
    - Use sparse categorical cross-entropy as the loss function.
    - Track accuracy as a metric.

6. **Train the Model**
    - Fit the model on the training data.
    - Choose an appropriate number of epochs.

7. **Evaluate the Model**
    - Evaluate the trained model on the test data.
    - Print the loss and accuracy.

8. **Make Predictions**
    - Use the trained model to make predictions on the test data.
    - Display a few test images along with their predicted and true labels.

