import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/parse_resume"

# Inject custom CSS
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 36px;
            color: #2c3e50;
            font-weight: bold;
            padding-bottom: 10px;
        }
        .upload-box {
            border: 2px dashed #4CAF50;
            padding: 20px;
            border-radius: 10px;
            background-color: white;
            text-align: center;
        }
        .skills-container {
            margin-top: 20px;
        }
        .skill-badge {
            display: inline-block;
            background-color: #4CAF50;
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            margin: 4px;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<div class='main-title'>📄 AI Resume Parser</div>", unsafe_allow_html=True)
st.write("Upload your resume to extract skills using AI & NLP.")

# Upload box
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

# Skill extraction
if uploaded_file is not None:
    with st.spinner("Extracting skills..."):
        response = requests.post(API_URL, files={"file": uploaded_file})
    if response.status_code == 200:
        skills = response.json().get("skills", [])
        if skills:
            st.success("✅ Skills extracted successfully!")
            st.markdown("<div class='skills-container'>", unsafe_allow_html=True)
            for skill in skills:
                st.markdown(f"<span class='skill-badge'>{skill}</span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning("No skills found in the resume.")
    else:
        st.error(f"Error: {response.json().get('error')}")
