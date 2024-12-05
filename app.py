import streamlit as st
import pandas as pd
import pickle

st.title("🚗 Car Price Prediction")

# Add spacing using HTML
st.markdown("<br>", unsafe_allow_html=True) 

st.markdown("""
    <style>
    /* Ensure the button is aligned to the right and below all inputs */
    .stButton {
        display: flex;
        justify-content: flex-end;
        margin-top: 20px;  /* Adds spacing from the inputs */
        width: 600px;
        height: 20px;
        font-size: 18px;
        color: red; 
    }
    </style>
""", unsafe_allow_html=True)


#Reading dataset
car= pd.read_csv('Cleaned car.csv')

# Create columns for layout
col_left, spacer,col_right = st.columns([5, 0.5, 5])

# HTML for embedding the Lottie animation
lottie_html = """<script src="https://unpkg.com/@dotlottie/player-component@2.7.12/dist/dotlottie-player.mjs" type="module"></script>
<dotlottie-player src="https://lottie.host/c966713b-b2ac-4a0c-a3d6-e9302940bede/wLdgYMHMyr.lottie" background="transparent" speed="1" style="width: 300px; height: 300px" loop autoplay></dotlottie-player>"""

with col_left:
    # Embed Lottie animation with HTML
    st.components.v1.html(lottie_html, height=300)

with col_right:
    car = pd.read_csv('Cleaned car.csv')

    car_name = st.selectbox('Select a car', car['name'].unique())
    company = st.selectbox('Select company', car['company'].unique())
    kms_driven = st.number_input('Kms driven')
    fuel_type = st.selectbox('Fuel Type', car['fuel_type'].unique())    
    year = st.slider('Select the Purchase Year', min_value=int(car['year'].min()), 
                     max_value=int("2024"), value=int(car['year'].min()))
    
with open("model.pkl","rb") as model_file:
    model = pickle.load(model_file)


if st.button('Predict'):    
    input_data = model.predict(pd.DataFrame([[car_name,company,year,kms_driven,fuel_type]], columns=['name','company','year','kms_driven','fuel_type']))
    prediction_value = round(input_data[0], 2)

    st.write(f"Estimate Price: {prediction_value}")


