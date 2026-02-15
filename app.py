import os
import pandas as pd
import streamlit as st

def train_model():
    file_path = "data.csv"  # change this to your actual filename

    # Check if file exists
    if not os.path.exists(file_path):
        st.error(
            f"❌ CSV file not found at: {file_path}\n"
            f"Current working directory: {os.getcwd()}\n"
            "Make sure the file is included in your repo or placed in the correct folder."
        )
        return None

    # Load the data
    data = pd.read_csv(file_path)

    # --- your training logic here ---
    # Example placeholder:
    model = "trained_model_placeholder"
    return model

# Streamlit app entry point
def main():
    st.title("Green Barrier App")

    model = train_model()
    if model is not None:
        st.success("✅ Model trained successfully!")
    else:
        st.warning("⚠️ Model training skipped because data file is missing.")

if __name__ == "__main__":
    main()
