#                   INTRODUCTION
#Python is a high-level object-oriented programming language.
# It was developed by Guido Van Rossum in 1989 and released in 1991.
# It is often called a batteries included language due to its complex standard library.
# The name python was taken from popular BBC comedy show of that time "Monty Python's Flying Circus"
#
#                   FEATURES OF PYTHON
# 1.Easy to learn and use - it has a simple structure and clearly defined structure,
# allowing the learners to pick up the language quickly.
# 2.Cross-platform - it can run on different OS such as windows or linux, making it portable.
# 3.Free and open source - python is freely available at official website
# It's open source hence the source code is publicly available
# 4.Object-oriented approach-  it uses an object-oriented approach that encapsulates code within objects.
# 5.Large Standard Library -  it provides various libraries for various tasks such as ML,web development and data analysis.
# 6. Memory management -  You don't need to assign the data type of the variable, When you assign some value to the variable it
# automatically allocates the memory to the variable at one runtime.
#
#                       USES OF PYTHON
# Used to develop desktop application
# Used to develop web Application
# Used in the field of Data Science, Machine Learning and Artificial Intelligence to analyze data, buld predictive models and make business decisions.
#Used in game development.
#
#                PYTHON FRAMEWORKS AND LIBRARIES
# For web development -  Django, Flask, CherryPy and Pyramid
# For GUI based applications - Tk, PyGTK, PyJs
# For Machine Learning - TensorFlow, PyTorch,Scikit,Matplotlib, SciPy
# For Mathematical computations - numpy and pandas
#
#                   BEST PYTHON IDEs
# Jupyter Notebook from Anaconda distribution
# Visual Studio Code from microsoft
# Pycharm
# Python IDLE
# Spyder Notebook
# Sublime text a text editor
#
#                     TOP COMPANIES USING PYTHON
# Netflix
# Google
# Quora
# Facebook
# Instagram
# Spotify
#
#                       INSTALLING PYTHON
# Download a python Interpreter in python.org - download latest
# After the installer is downloaded open it - installation window pops up
# Check the 2boxes for path and launcher then click on "install now"
# A window of "setup was successful appears" click on close.
# Check whether it was installed successfully by using this command in cmd "python --version"
# To run a basic command type "py" and press enter
# print("Hello World!") and press enter

#               TO INSTALL LIBRARIES OF PYTHON
# Make sure the latest pip is installed in your laptop type "pip --version" and press enter
# To upgrade pip use this command "python -m pip install --upgrade pip"
# Install numpy using this command "pip install numpy" and press enter wait until it's successfully downloaded
# To install scipy library "pip install scipy"
# To download and install pandas library "pip install pandas"
# To install matplotlib library "pip install matplotlib"
#
#              TO CHECK INSTALLED LIBRARIES
# Type "python" and press enter
#      "import numpy as  np" if it does not bring any error then its installed successfully.
# Create an array "a=np.array([[1,2,4],[5,7,9]],dtype='float')
#                 print("array created:\n",a)
#   import matplotlib and press enter to check if its installed successfully
#   import pandas and press enter to check if its installed successfully
#   import scipy and press enter to check if its installed successfully
#
#              ANACONDA
# It is a free and opensource distribution of python and R language
# Conda is a package manager system similar to pip in python.
#                    HOW TO DOWNLOAD ANACONDA
# Open the Browser search for "anaconda" and use the official website "www.anaconda.com"
# Click on download, choose the OS you're using.
# Double-click on the downloaded application file
# Installation window appears, click on "Just Me" and click on next
# Choose installation location or leave it as default and click on next
# Click on the first checkbox "Add Anaconda to my path environment" and click on install.
# After installation is complete click on next and next
# Uncheck the 2 boxes: Launch Anaconda navigator and Getting started with anaconda
# Click on Finish
# Launch anaconda prompt or navigator to check all you need.
#
#
#                                 VARIABLES IN PYTHON
#Python variables are containeers for storing data values
#We do not need to declare variables or data types before using them like in other programming languages
#Python is not statically types, a variable is created the moment we assign a value to it.
#A variable is a name given to a memory loctation
# car ="BMW" Here we have variable car having a value called BMW. The value is of type STRING because it is written withiin double quotes
#Variables can have values of multiple data types
#Python allows you to assign values to multiple variables in one line. 
#For example: x,y,z="BMW","Audi","Mercedes" ; Here we have assignes xyz to Audi,BMW and mercedes in one line.
#                               OBJECT REFERENCES IN PYTHON
#Python variable is a symbolic name that is a reference or pointer to an object
#Once an object is assigned to a variable, you can refer to the object by that name.
#Example1: a=50 here we are assigning an int value of 50 to a variable 'a'.. An assignment creates an integer object with a value of 50 and assigns a variable A to that object
#Example2: a=50 b=a Here we have assigned a variable A which has a value of 50 and then created another variable called B that has a value stored in A
#In the case above python does not create another variable,but creates a symbolic name or reference called B which points to the same object that A points to.
# Example3: a=50 b=100 Here python creates a new integer object with a value of 100 and B becomes a reference to it
#
#                                    RULES FOR PYTHON VARIABLES
#A variable name must start with a letter or the underscore character
#A variable cannot start with a number
#A variable name can only contain aplha-numeric characters and underscore(A-z,0-9 and _)
#Variable names are case-sensitive(date,Date and DATE are 3 different variables)
#There are several Techniques to write multi words variables:
#
