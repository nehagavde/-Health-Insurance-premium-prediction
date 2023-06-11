import streamlit as st
import joblib
from PIL import Image

def main():
    st.set_page_config(page_title="Welcome To Insurance Premium Predictor", layout="wide")

    
    #st.markdown("<h1 style='text-align: center; color:white;'>Welcome To Insurance Premium Predictor</h1>", unsafe_allow_html=True)
    st.title("Welcome To Insurance Premium Predictor")

    #img = Image.open('https://emerj.com/wp-content/uploads/2018/10/predictive-analytics-in-healthcare-current-applications-and-trends-3.jpg')
    #st.image(img)
    #st.image(img, use_column_width=False, caption='', width=1300)
    #st.image('https://emerj.com/wp-content/uploads/2018/10/predictive-analytics-in-healthcare-current-applications-and-trends-3.jpg')
    url = 'https://emerj.com/wp-content/uploads/2018/10/predictive-analytics-in-healthcare-current-applications-and-trends-3.jpg'
    response = requests.get(url)
    response.raise_for_status()
    # Save the downloaded image locally
    filename = 'image.jpg'
    with open(filename, 'wb') as file:
        file.write(response.content)

    # Open the saved image
    img = Image.open(filename)


    # Define the desired height
    desired_height = 200

    # Calculate the proportional width based on the desired height
    proportional_width = int((desired_height / float(img.size[1])) * img.size[0])

    # Resize the image
    resized_image = img.resize((proportional_width, desired_height))

    # Display the resized image
    st.image(resized_image, caption='Resized Image', use_column_width=True)

    model = joblib.load('model_gradient_boosting_regressor (1)')
    # model = joblib.load('model_random_forest_regression')

    age = st.slider('Enter Age&nbsp; Of&nbsp; The&nbsp; Customer', 18, 100)

    sex = st.selectbox('Select&nbsp; Gender&nbsp; Of&nbsp; The&nbsp; Customer', ('Male', 'Female'))
    if sex == 'Male':
        sex = 1
    else:
        sex = 0

    bmi = st.number_input("Enter&nbsp;BMI&nbsp; Value&nbsp; Of&nbsp; The&nbsp; Customer")

    children = st.selectbox('Enter&nbsp; Number&nbsp; Of&nbsp; The&nbsp; Children', (0, 1, 2, 3, 4))

    # Add multiple <br> tags for a larger gap
    st.markdown("<br> ", unsafe_allow_html=True)

    smoker = st.selectbox('Select&nbsp; Type&nbsp; Of&nbsp; The&nbsp; Customer&nbsp; (Smoker)', ('Yes', 'No'))
    if smoker == 'Yes':
        smoker = 1
    else:
        smoker = 0

    region = st.selectbox('Select&nbsp; Region&nbsp; Of&nbsp; The&nbsp; Customer', ('Southwest', 'Southeast', 'Northwest', 'Northeast'))
    if region == 'Southwest':
        region = 1
    elif region == 'Southeast':
        region = 2
    elif region == 'Northwest':
        region = 3
    else:
        region = 4

    if st.button('Predict'):
        pred = model.predict([[age, sex, bmi, children, smoker, region]])

        st.balloons()
        st.success('Your Insurance Cost is {}'.format(round(pred[0], 2)))


if __name__ == '__main__':
    main()
