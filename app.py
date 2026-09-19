import streamlit as st
import pandas as pd
from PIL import Image
import pytesseract
import re

# Tesseract location
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Page settings
st.set_page_config(
    page_title="TimeTableX",
    page_icon="📅",
    layout="wide"
)

# Title
st.title("📅 TimeTableX")
st.write("Convert printed bus timetables into digital data.")

st.divider()

# Upload section
st.header("📷 Upload Timetable")

uploaded_file = st.file_uploader(
    "Choose a timetable image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Timetable",
        use_container_width=True
    )

    st.success("Timetable uploaded successfully!")

    # Extract button
    if st.button("🔍 Extract Timetable"):

        with st.spinner("Reading timetable..."):

            # OCR
            text = pytesseract.image_to_string(image)

        st.success("Text extraction completed!")

        # Find all time values
        times = re.findall(r'\b\d{1,2}:\d{2}\b', text)

        # Create table
        timetable = pd.DataFrame({
            "No.": range(1, len(times) + 1),
            "Departure Time": times
        })

        # Display table
        st.subheader("🕐 Detected Timings")

        st.dataframe(
            timetable,
            use_container_width=True,
            hide_index=True
        )
        