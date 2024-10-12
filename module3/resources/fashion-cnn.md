### Exercise: Classifying Clothing Items with CNN on Fashion MNIST

#### Objective
Implement a Convolutional Neural Network (CNN) to classify clothing items in the Fashion MNIST dataset and visualize the model's predictions alongside the actual labels.

#### Steps

1. **Setup and Import Libraries**
   - Import the necessary libraries such as TensorFlow, Keras, and Matplotlib.

2. **Load the Fashion MNIST Dataset**
   - Use TensorFlow to load the Fashion MNIST dataset.
   - Split the dataset into training and testing sets.

3. **Preprocess the Data**
   - Normalize the pixel values of the images (scale them to a range of 0 to 1).
   - Reshape the data to fit the input shape of the CNN.

4. **Build the CNN Model**
   - Create a sequential model with the following layers:
     - A `Conv2D` layer with 32 filters, a kernel size of (3, 3), and ReLU activation.
     - A `MaxPooling2D` layer to reduce dimensionality.
     - Another `Conv2D` layer with 64 filters and a similar structure.
     - A flattening layer to prepare the data for dense layers.
     - One or two `Dense` layers, with the final layer using softmax activation for multi-class classification.

5. **Compile the Model**
   - Use the SGD optimizer and the sparse categorical crossentropy loss function. Track accuracy as a metric.

6. **Train the Model**
   - Fit the model on the training data, specifying the number of epochs and batch size.

7. **Evaluate the Model**
   - Assess the model's performance on the test dataset and print the test accuracy.

8. **Make Predictions**
   - Use the trained model to make predictions on the test dataset.

9. **Visualize Predictions**
   - Select a few images from the test set and visualize them alongside their predicted and actual labels using Matplotlib.

