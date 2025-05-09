import streamlit as st
import requests
import fitz  # PyMuPDF for PDF text extraction
import io

st.title("Upload JD and Resumes to n8n")

# Upload JD PDF (only one allowed)
jd_file = st.file_uploader("Upload JD PDF", type="pdf", accept_multiple_files=False)

# Upload multiple Resume PDFs
resume_files = st.file_uploader("Upload Resume PDFs", type="pdf", accept_multiple_files=True)

if jd_file and resume_files and st.button("Send to n8n"):
    webhook_url = "https://digitalrecruiter.app.n8n.cloud/webhook/c1aebe67-c21e-4f9c-893c-3fcca86cc771"
    # --- 1. Extract text from JD PDF using PyMuPDF ---
    jd_bytes = jd_file.read()
    jd_text = ""
    with fitz.open(stream=jd_bytes, filetype="pdf") as doc:
        for page in doc:
            jd_text += page.get_text()

    # --- 2. Prepare form data and files ---
    data = {
        "jd_text": jd_text  # Send JD text as a form field
    }

    files = []
    for f in resume_files:
        # Read file bytes
        f_bytes = f.read()
        # Rewind the file buffer
        f.seek(0)
        files.append(
            ("resumes", (f.name, io.BytesIO(f_bytes), "application/pdf"))
        )

    # --- 3. Send to webhook ---
    response = requests.post(webhook_url, data=data, files=files)

    # Show response
    st.subheader("n8n Response")
    st.write(response.text)
