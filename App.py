import streamlit as st
import pickle
import joblib

def main():
    st.markdown("<h1 style='text-align: center; color:white;'>Health Insurance Cost Prediction</h1>", unsafe_allow_html=True)

    st.image('https://emerj.com/wp-content/uploads/2018/10/predictive-analytics-in-healthcare-current-applications-and-trends-3.jpg')

    with open('gradient_boosting_regressor_model (1)', 'rb') as f:
        model = joblib.load(f)
    

    age = st.slider('Enter Your Age', 18, 100)

    sex_mapping = {'Male': 1, 'Female': 0}
    sex = st.selectbox('Sex', ('Male', 'Female'))
    sex = sex_mapping[sex]

    bmi = st.number_input("Enter Your BMI Value")

    children = st.selectbox('Enter Number of Children', (0, 1, 2, 3, 4))

    smoker_mapping = {'Yes': 1, 'No': 0}
    smoker = st.selectbox('Smoker', ('Yes', 'No'))
    smoker = smoker_mapping[smoker]

    region_mapping = {'Southwest': 1, 'Southeast': 2, 'Northwest': 3, 'Northeast': 4}
    region = st.selectbox('Enter Your Region', ('Southwest', 'Southeast', 'Northwest', 'Northeast'))
    region = region_mapping[region]

    if st.button('Predict'):
        predicted_cost = model.predict([[age, sex, bmi, children, smoker, region]])

        st.balloons()
        st.success('Your Insurance Cost is {}'.format(round(predicted_cost[0], 2)))


if __name__ == '__main__':
    main()
