# main.py

def main():
    print("Welcome to the AI Resume Analyzer & Job Recommender Project!")
    print("This project will help analyze resumes and suggest job roles based on skills.")

if __name__ == "__main__":
    main()
print("✅ AI Resume Analyzer Project started successfully!")

import os
import fitz  # PyMuPDF

def extract_text_from_pdf(file_path):
    if not os.path.exists(file_path):
        return "File not found."

    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_skills(text):
    # Simple list of common tech & soft skills (can be extended)
    skills_list = [
        "python", "java", "c++", "machine learning", "deep learning", "data analysis",
        "communication", "teamwork", "problem solving", "sql", "excel", "power bi",
        "tensorflow", "pytorch", "pandas", "numpy", "html", "css", "javascript"
    ]

    text = text.lower()
    found_skills = [skill for skill in skills_list if skill in text]
    return found_skills


if __name__ == "__main__":
    print("Welcome to the AI Resume Analyzer & Job Recommender Project!")
    print("This project will help analyze resumes and suggest job roles based on skills.")

    file_path = r"C:\Users\manojpandey001\Downloads\Kamal Joshi Resume.pdf"  # 👈 Make sure this exists in folder
    resume_text = extract_text_from_pdf(file_path)

    print("\n📄 Extracted Text from Resume:\n")
    print(resume_text)

    skills = extract_skills(resume_text)
    print("\n🧠 Skills Found in Resume:\n")
    print(skills)

# Predefined job roles with required skills
job_roles = {
    "Accountant": {"Accounting and Bookkeeping", "Tally ERP 9 with GST", "Tax Return Filing", "MS Office"},
    "Tax Consultant": {"Tax Return Filing", "GST", "Tally ERP 9 with GST", "MS Office"},
    "Finance Assistant": {"Accounting and Bookkeeping", "MS Office", "Customer Relations"},
    "Administrative Executive": {"Customer Relations", "MS Office", "Communication"},
    "Data Entry Operator": {"MS Office", "Tally ERP 9 with GST", "Accuracy", "Typing"}
}

# Convert your resume skills into a set for comparison
resume_skills = {
    "MS Office",
    "Accounting and Bookkeeping",
    "Tally ERP 9 with GST",
    "Tax Return Filing",
    "Customer Relations"
}

# Match and score
print("\n💼 Recommended Job Roles Based on Resume:\n")
for role, required_skills in job_roles.items():
    match = resume_skills.intersection(required_skills)
    match_percent = (len(match) / len(required_skills)) * 100
    if match_percent >= 50:
        print(f"🔹 {role} - {match_percent:.0f}% match ({', '.join(match)})")

print("\n📋 Resume Analysis Complete!")
print("======================================")
print("👤 Candidate: Kamal Joshi")
print("📍 Location: Ghaziabad, Uttar Pradesh")
print("📞 Contact: +91 9910158337")
print("📧 Email: kamaljoshi046@gmail.com")

print("\n🧠 Skills Identified:")
for skill in resume_skills:
    print(f"✅ {skill}")

print("\n💼 Top Job Role Recommendations:")
for role, required_skills in job_roles.items():
    match = resume_skills.intersection(required_skills)
    match_percent = (len(match) / len(required_skills)) * 100
    if match_percent >= 50:
        print(f"\n🔹 {role}")
        print(f"   → Match: {match_percent:.0f}%")
        print(f"   → Matching Skills: {', '.join(match)}")

print("\n✅ End of Report")
print("======================================")
