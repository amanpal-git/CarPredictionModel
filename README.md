# Car Price Prediction using Linear Regression

## Introduction
This project focuses on predicting car prices using a Linear Regression model. The code provided here leverages Python libraries such as Pandas, NumPy, and scikit-learn for data preprocessing, modeling, and evaluation. The dataset used for training and testing the model is loaded from a CSV file.

## Code Structure
The code is divided into several sections, each with a specific purpose:

### Importing Libraries and Loading Data
```python
import pandas as pd
import numpy as np

# Load the car dataset from a CSV file
car = pd.read_csv('C:/Users/thero/jupyterFiles/Cleaned car.csv')
```

# Data Preprocessing
In this section, the data is preprocessed to prepare it for modeling. Columns relevant to the prediction task are selected, and categorical variables are one-hot encoded.

# Hyperparameter Tuning
The code also includes a section for hyperparameter tuning. It runs the model with different random states and selects the best-performing model based on the R-squared score.

# Making Predictions
Finally, you can use the trained model to make predictions for new data. Here's an example:
```
new_data = pd.DataFrame([['Mahindra XUV500','Mahindra',2016,4000,'Petrol']], columns=['name','company','year','kms_driven','fuel_type'])
predictions = pipeline.predict(new_data)
print(predictions)
```
# Running the Code
Make sure you have Python installed on your system.  
Install the required libraries using pip install pandas numpy scikit-learn.   
Download the CSV file containing the car data and specify the correct file path in the code.   
Run the code in your preferred Python environment (e.g., Jupyter Notebook, VSCode, or any IDE).     
The code will load the dataset, preprocess the data, train a Linear Regression model, and evaluate its performance. You can then use the trained model to make price predictions for new data.  


# Results
The code provides two evaluation metrics for the model: Mean Squared Error (MSE) and R-squared (R2) score. These metrics can be used to assess the model's accuracy in predicting car prices.

Feel free to modify the code, dataset, or model parameters to further improve the prediction accuracy or explore different machine learning techniques.
