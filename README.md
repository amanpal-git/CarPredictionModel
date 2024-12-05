# Car Price Prediction using Linear Regression and Streamlit

![appStreamlit-GoogleChrome2024-12-0601-56-21-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/eaea1120-3e1a-4eb2-b5f8-eccf44d7d626)
---

## Introduction
This project focuses on predicting car prices using a Linear Regression model, with the additional feature of a user-friendly web interface built with **Streamlit**. The app allows users to input car details (such as car name, company, year, kilometers driven, and fuel type) and receive an estimated price prediction based on a trained model. The project also includes an animated GIF of a car for a visually interactive experience.

The machine learning model for predicting car prices is trained using a dataset loaded from a CSV file, and the model is serialized using `pickle` for easy deployment.

## Project Features
- **Interactive Web Interface**: Built with Streamlit, the app allows users to input car details and get an estimated car price prediction.
- **Car Animation**: A car animation GIF is embedded on the left side of the web app for a more engaging user experience.
- **Price Prediction**: The app uses a pre-trained Linear Regression model to predict car prices based on user inputs.
- **Data Preprocessing**: Data is cleaned and processed before training the model.
- **Model Deployment**: The trained model is saved using `pickle` for deployment in the web app.

## Code Structure
The code is divided into several sections, each with a specific purpose:

### Importing Libraries and Loading Data
```python
import pandas as pd
import numpy as np
import pickle
import streamlit as st 
```
# Load the car dataset from a CSV file
car = pd.read_csv('Cleaned car.csv')

## Running the Code

Make sure you have Python installed on your system.

1. Install the required libraries:
    ```bash
    pip install pandas numpy scikit-learn streamlit
    ```

2. Download the CSV file containing the car data and specify the correct file path in the code.

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

The code will load the dataset, preprocess the data, train a Linear Regression model, and evaluate its performance. You can then use the trained model to make price predictions for new data.

## Results

The app provides the predicted car price based on the input features. It also displays a car animation GIF for an enhanced user experience.

## Future Enhancements

- Experiment with other machine learning models to improve prediction accuracy.
- Add more input features (e.g., car condition, location, etc.) for better predictions.
- Deploy the app on a cloud platform like Heroku or AWS to make it publicly accessible.
