
# Miniconda and Jupyter Notebook Installation Instructions 

- Download Miniconda from [here](https://docs.anaconda.com/free/miniconda/index.html)
- Create a folder with the name of your choice, anywhere on your machine. For our case we will call it ai_project 
- Go into the ai_project folder and run ``` conda create --prefix ./env pandas numpy matplotlib jupyter ```. This will create an environment in the ai_project folder. 
- Run the command ``` conda env list ```. This will list all the available environments on your system. You should see an environment dedicated to your project folder. 
- Enable your environment by running ``` conda activate /Users/azamsharp/Desktop/ai_project/env ```
- You can launch Jupyter notebook by running ``` jupyter notebook ``` from without your project folder. 


