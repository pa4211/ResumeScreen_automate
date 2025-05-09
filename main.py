#import streamlit as st
#import requests

#uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
#if uploaded_file is not None:
 #   if st.button("Submit"):
  #      files = {"data": (uploaded_file.name, uploaded_file, "application/pdf")}
   #     response = requests.post("", files=files)
    #    st.write("n8n response:", response.text)

import streamlit as st
import requests
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Streamlit UI
st.title("Extract Text from PDF and Send to n8n")
uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    if st.button("Submit"):
        # Extract text from PDF
        extracted_text = extract_text_from_pdf(uploaded_file)

        # Replace with your actual n8n webhook URL
        webhook_url = "https://digitalrecruiter.app.n8n.cloud/webhook/3b3ac9c1-929b-49b4-b384-85f80cc09ae3"  # <-- Update this

        # Send extracted text to n8n
        response = requests.post(webhook_url, json={"text": extracted_text})

        # Display results
        st.subheader("Extracted Text")
        st.text_area("PDF Content", extracted_text, height=300)

        st.subheader("n8n Response")
        st.write(response.text)
