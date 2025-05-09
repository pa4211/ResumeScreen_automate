import streamlit as st
import requests

st.title("Upload Multiple PDFs to n8n")

# Allow multiple PDF uploads
uploaded_files = st.file_uploader("Choose PDF files", type="pdf", accept_multiple_files=True)

if uploaded_files and st.button("Send to n8n"):
    webhook_url = "https://digitalrecruiter.app.n8n.cloud/webhook/3522c52c-8640-4d5d-b071-329d3aed4baf"  # Replace with your actual n8n webhook URL

    # Prepare files for multipart upload
    files = []
    for f in uploaded_files:
        files.append(
            ("files", (f.name, f, "application/pdf"))
        )

    # Send files to n8n webhook
    response = requests.post(webhook_url, files=files)

    # Show response from n8n
    st.subheader("n8n Response")
    st.write(response.text)