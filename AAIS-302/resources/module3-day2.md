# Walkthrough for Day 2: Introduction to Matplotlib

This guide will walk beginners through five activities focused on basic visualizations and customization using Matplotlib.

---

## **Activity 1: Creating Basic Plots**
### Objective:
Learn how to create a simple line plot with Matplotlib.

### Steps:
1. Import Matplotlib:
   ```python
   import matplotlib.pyplot as plt
   ```

2. Create a small numerical dataset:
   ```python
   data = [1, 2, 3, 4]
   ```

3. Plot the dataset:
   ```python
   plt.plot(data)
   ```

4. Display the plot:
   ```python
   plt.show()
   ```

### Expected Outcome:
A basic line plot with data points `[1, 2, 3, 4]` connected by lines.

---

## **Activity 2: Adding Labels and Titles**
### Objective:
Enhance the basic plot by adding titles and labels for better readability.

### Steps:
1. Use the same code from Activity 1 to create a basic plot.

2. Add labels and a title:
   ```python
   plt.title('My First Line Plot')
   plt.xlabel('X-axis Label')
   plt.ylabel('Y-axis Label')
   ```

3. Display the plot with the new labels and title:
   ```python
   plt.show()
   ```

### Expected Outcome:
A line plot with a title at the top and labels for both the x-axis and y-axis.

---

## **Activity 3: Customizing Plot Styles**
### Objective:
Explore Matplotlib's built-in styles to customize the appearance of your plots.

### Steps:
1. View available styles:
   ```python
   print(plt.style.available)
   ```

2. Choose and apply a style, such as `ggplot`:
   ```python
   plt.style.use('ggplot')
   ```

3. Recreate the plot from Activity 2 using the chosen style.

4. Try different styles like `seaborn` or `dark_background`:
   ```python
   plt.style.use('seaborn')
   ```

### Expected Outcome:
The plot will adopt the chosen style, changing the background, gridlines, and overall appearance.

---

## **Activity 4: Multiple Lines on the Same Plot**
### Objective:
Learn to plot multiple datasets with distinct line styles and colors.

### Steps:
1. Define two datasets:
   ```python
   data1 = [1, 2, 3, 4]
   data2 = [4, 3, 2, 1]
   ```

2. Plot both datasets on the same graph:
   ```python
   plt.plot(data1, label='Data 1', linestyle='-', color='blue')  # Solid line
   plt.plot(data2, label='Data 2', linestyle='--', color='red')  # Dashed line
   ```

3. Add a legend to differentiate the lines:
   ```python
   plt.legend()
   ```

4. Display the plot:
   ```python
   plt.show()
   ```

### Expected Outcome:
A graph with two lines, one solid blue and the other dashed red, and a legend indicating which line corresponds to which dataset.

---

## **Activity 5: Saving Plots**
### Objective:
Save your visualizations as image files for later use.

### Steps:
1. Recreate any plot from the previous activities.

2. Save the plot as a file:
   ```python
   plt.savefig('my_plot.png')  # Save as a PNG file
   ```

3. Save the plot in a different format (e.g., PDF):
   ```python
   plt.savefig('my_plot.pdf')
   ```

4. Check your working directory to confirm the files were saved.

### Expected Outcome:
The plot will be saved as an image or PDF file in the specified location.

---

## **Final Notes**
- Experiment with different datasets and styles to get comfortable with Matplotlib.
- Use the `plt.show()` command to view your plots after making changes.
- Combine activities to create more detailed and polished visualizations.

Enjoy exploring Matplotlib!