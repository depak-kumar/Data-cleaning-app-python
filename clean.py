import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Streamlit app title
st.title("Data Cleaning App")
st.image("https://th.bing.com/th/id/OIP.W72c5UTd-QdbRX4Q2dZ4owHaEK?pid=ImgDet&rs=1")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the original data
    st.subheader("Original Data")
    st.write(df)

     # Data Cleaning Options
    st.sidebar.subheader("Data Cleaning Options")
     # Option: Remove Missing Values
    if st.sidebar.checkbox("Remove Missing Values"):
        df.dropna(inplace=True)
        st.write("Missing values removed.")

    # Option: Remove Duplicates
    if st.sidebar.checkbox("Remove Duplicates"):
        df.drop_duplicates(inplace=True)
        st.write("Duplicates removed.")

    # Option: Data Summary
    if st.sidebar.checkbox("Data Summary"):
        st.subheader("Data Summary")
        st.write(df.describe())
   

    # Option: Toggle to Show DataFrame After Cleaning
    show_cleaned_data = st.sidebar.toggle("Show DataFrame After Cleaning")

    # Option: Delete Specific Columns
    if st.sidebar.checkbox("Delete Specific Columns"):
        st.sidebar.write("Select columns to delete:")
        columns_to_delete = st.sidebar.multiselect("Columns", df.columns)

        if columns_to_delete:
            # Drop the selected columns
            df.drop(columns=columns_to_delete, inplace=True)
            st.write("Selected columns deleted.")

    # Option: Label Encoding for Categorical Columns
    if st.sidebar.checkbox("Label Encoding for Categorical Columns"):
        categorical_columns = df.select_dtypes(include=['object']).columns
        selected_column = st.sidebar.selectbox("Select a categorical column for encoding", categorical_columns)

        if selected_column:
            label_encoder = LabelEncoder()
            df[selected_column] = label_encoder.fit_transform(df[selected_column])
            st.write(f"{selected_column} encoded.")

    # Rest of the data cleaning options (e.g., remove missing values, remove duplicates) go here.

    # Option: Download Cleaned Data
    if st.sidebar.button("Download Cleaned Data"):
        cleaned_data = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Download Cleaned Data",
            cleaned_data,
            "cleaned_data.csv",
            key="download-cleaned-data",
        )

    # Display the cleaned data if the toggle is on
    if show_cleaned_data:
        st.subheader("Cleaned Data")
        st.write(df)

# Provide instructions to the user
st.sidebar.markdown(
    """
    **Instructions:**
    1. Upload a CSV file using the file uploader on the left.
    2. Select data cleaning options from the sidebar.
    3. Use the toggle switch to display or hide the cleaned data.
    4. Download the cleaned dataset if desired.
    """
)
st.header("Made By DEEPAK KUMAR ")

