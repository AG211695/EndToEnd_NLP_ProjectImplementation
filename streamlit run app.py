import streamlit as st
from hateSpeechClassification.pipeline.train_pipeline import TrainPipeline
from hateSpeechClassification.pipeline.prediction_pipeline import PredictionPipeline
from hateSpeechClassification.exception import CustomException
import sys

# Streamlit UI configuration
st.title('Hate Speech Classification App')

# Define the text input and prediction button
text = st.text_input("Enter text for prediction:")

if st.button('Predict'):
    if text:
        try:
            # Initialize the prediction pipeline
            prediction_pipeline = PredictionPipeline()
            result = prediction_pipeline.run_pipeline(text)
            st.write(f"Prediction Result: {result}")
        except Exception as e:
            st.error(f"Error occurred during prediction: {e}")
    else:
        st.warning("Please enter some text.")

# Add a section to run the training pipeline
if st.button('Run Training'):
    try:
        # Initialize and run the training pipeline
        train_pipeline = TrainPipeline()
        train_pipeline.run_pipeline()
        st.success("Training successful!")
    except Exception as e:
        st.error(f"Error occurred during training: {e}")

