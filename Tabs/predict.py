"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Lung Cancer Detection.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("Gender", int(df["GENDER"].min()), int(df["GENDER"].max()))
    B = st.slider("Age", int(df["AGE"].min()), int(df["AGE"].max()))
    C= st.slider("Smoking", int(df["SMOKING"].min()), int(df["SMOKING"].max()))
    D = st.slider("Yellowness of Fingers", int(df["YELLOW_FINGERS"].min()), int(df["YELLOW_FINGERS"].max()))
    E = st.slider("Anxiety", int(df["ANXIETY"].min()), int(df["ANXIETY"].max()))
    F = st.slider("Chronic Diseases", int(df["CHRONIC_DISEASE"].min()), int(df["CHRONIC_DISEASE"].max()))
    G = st.slider("Fatigue", int(df["FATIGUE"].min()), int(df["FATIGUE"].max()))
    H = st.slider("Allergy", int(df["ALLERGY"].min()), int(df["ALLERGY"].max()))
    I = st.slider("Wheezing", int(df["WHEEZING"].min()), int(df["WHEEZING"].max()))
    J = st.slider("Alcohol Consumption", int(df["ALCOHOL_CONSUMING"].min()), int(df["ALCOHOL_CONSUMING"].max()))
    K = st.slider("Coughing", int(df["COUGHING"].min()), int(df["COUGHING"].max()))
    L = st.slider("Shortness of Breath", int(df["SHORTNESS_OF_BREATH"].min()), int(df["SHORTNESS_OF_BREATH"].max()))
    M = st.slider("Swallowing Difficulties", int(df["SWALLOWING_DIFFICULTY"].min()), int(df["SWALLOWING_DIFFICULTY"].max()))
    N = st.slider("Chest Pain", int(df["CHEST_PAIN"].min()), int(df["CHEST_PAIN"].max()))

    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J,K,L,M,N]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.08 
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get Lung Cancer!!")
        else:
            st.success("The person is relatively safe from Lung Cancer")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
