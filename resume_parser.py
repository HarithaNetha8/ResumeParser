import pdfplumber
import docx
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Load skill keywords
with open("skills_list.txt") as f:
    SKILLS = [line.strip().lower() for line in f.readlines()]

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_skills(text):
    doc = nlp(text.lower())
    tokens = [token.text for token in doc]
    found_skills = set()
    for skill in SKILLS:
        if skill.lower() in tokens or skill.lower() in text.lower():
            found_skills.add(skill)
    return list(found_skills)

if __name__ == "__main__":
    # Example
    text = extract_text_from_pdf("sample_resume.pdf")
    skills = extract_skills(text)
    print(skills)
