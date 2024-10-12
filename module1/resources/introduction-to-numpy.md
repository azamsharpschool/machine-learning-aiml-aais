# Introduction to Numpy 

NumPy, short for Numerical Python, is a powerful library for numerical computing in Python. It provides support for arrays, matrices, and many mathematical functions to operate on these data structures. This tutorial will introduce you to the basics of NumPy, including array creation, operations, and some common functions.

## Installation

Before we start, you need to have NumPy installed. You can install it using pip:

```bash
pip install numpy
```

## Importing NumPy

To use NumPy, you need to import it into your Python script:

```python
import numpy as np
```

It's common practice to import NumPy with the alias `np`.

## Using Mini Conda 

When using Conda environment, you can use the conda install command install the package. 

```
conda install numpy  
```

## Creating Arrays

### 1. From Lists

You can create a NumPy array from a Python list using the `np.array()` function:

```python
import numpy as np

my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)
```

### 2. From Scratch

NumPy provides several functions to create arrays from scratch:

- `np.zeros(shape)`: Creates an array of the given shape filled with zeros.
- `np.ones(shape)`: Creates an array of the given shape filled with ones.
- `np.full(shape, fill_value)`: Creates an array of the given shape filled with the specified value.
- `np.eye(N)`: Creates an N x N identity matrix.
- `np.arange(start, stop, step)`: Creates an array with values ranging from `start` to `stop` with a given `step`.
- `np.linspace(start, stop, num)`: Creates an array with `num` evenly spaced values between `start` and `stop`.

Examples:

```python
zeros_array = np.zeros((3, 3))
ones_array = np.ones((2, 2))
full_array = np.full((2, 3), 7)
identity_matrix = np.eye(4)
arange_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)

print(zeros_array)
print(ones_array)
print(full_array)
print(identity_matrix)
print(arange_array)
print(linspace_array)
```

## Array Operations

### 1. Arithmetic Operations

NumPy arrays support element-wise arithmetic operations:

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
```

### 2. Universal Functions (ufuncs)

NumPy provides many mathematical functions that operate element-wise:

```python
a = np.array([1, 2, 3, 4])

print(np.sqrt(a))
print(np.exp(a))
print(np.sin(a))
print(np.log(a))
```

### 3. Aggregation Functions

NumPy offers several aggregation functions to compute summaries of arrays:

```python
a = np.array([1, 2, 3, 4, 5])

print(np.sum(a))
print(np.mean(a))
print(np.std(a))
print(np.min(a))
print(np.max(a))
```

## Indexing and Slicing

NumPy arrays can be indexed and sliced similarly to Python lists:

```python
a = np.array([1, 2, 3, 4, 5])

print(a[0])      # First element
print(a[-1])     # Last element
print(a[1:3])    # Slicing from index 1 to 2
print(a[:3])     # Slicing from start to index 2
print(a[2:])     # Slicing from index 2 to end
```

For multi-dimensional arrays, indexing is done with a tuple of indices:

```python
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(b[0, 0])   # First element of the first row
print(b[1, 2])   # Third element of the second row
print(b[:, 1])   # Second column
print(b[1, :])   # Second row
```

## Reshaping Arrays

You can change the shape of an array using the `reshape()` method:

```python
a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape((2, 3))
print(b)
```

## Array Concatenation and Splitting

### 1. Concatenation

You can concatenate arrays using `np.concatenate()`, `np.vstack()` (vertical stack), and `np.hstack()` (horizontal stack):

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

concat_array = np.concatenate((a, b))
vstack_array = np.vstack((a, b))
hstack_array = np.hstack((a, b))

print(concat_array)
print(vstack_array)
print(hstack_array)
```

### 2. Splitting

You can split arrays using `np.split()`, `np.vsplit()`, and `np.hsplit()`:

```python
a = np.array([1, 2, 3, 4, 5, 6])

split_array = np.split(a, 3)
print(split_array)

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vsplit_array = np.vsplit(b, 3)
hsplit_array = np.hsplit(b, 3)

print(vsplit_array)
print(hsplit_array)
```

## Conclusion

This tutorial covered the basics of NumPy, including array creation, operations, indexing, slicing, reshaping, and concatenation. NumPy is a vast library with many more functions and capabilities. As you get more comfortable with these basics, you can explore more advanced features such as broadcasting, linear algebra operations, and more.

For more detailed information, you can refer to the [official NumPy documentation](https://numpy.org/doc/). Happy coding!