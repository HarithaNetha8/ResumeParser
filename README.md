# ResumeParser
Python-based Resume Parsing tool using NLP for extracting structured data (skills, education, experience) from PDF, DOCX, and TXT resumes.
# 📄 ResumeParser

An AI-powered **Resume Parsing Tool** built with Python that extracts structured information such as **Name**, **Email**, **Phone Number**, **Skills**, **Education**, and **Experience** from resumes in PDF, DOCX, and TXT formats.

---

## 🚀 Features
- Extracts key candidate details from resumes.
- Supports multiple file formats (PDF, DOCX, TXT).
- Uses **Natural Language Processing (NLP)** for accurate parsing.
- Easy to integrate into recruitment or HR systems.
- REST API support for automated parsing.

---

## 🛠️ Tech Stack
- **Python**
- **Flask** (API backend)
- **NLTK / spaCy** (Natural Language Processing)
- **PyMuPDF / pdfplumber** (PDF reading)
- **python-docx** (DOCX reading)

---

---

## ⚙️ Installation & Setup
1. **Clone the Repository**
   ```bash
   git clone https://github.com/HarithhaNetha8/ResumeParser.git
   cd ResumeParser

2. **Create Virtual Environment**

python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows


3. **Install Dependencies**

pip install -r requirements.txt


4. **Run the Application**

python app.py


5. **Access the App**

Open browser → http://127.0.0.1:5000


📤 **Uploading Resumes**

Navigate to the web app.

Upload a .pdf, .docx, or .txt file.

View parsed results instantly.


📦**API Usage**

Endpoint: /parse_resume
Method: POST
Parameters: resume_file (form-data)
Response: JSON with parsed details.
