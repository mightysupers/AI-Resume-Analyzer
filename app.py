import streamlit as st
import fitz  # PyMuPDF
import re

# Define the job roles and required skills
job_roles = {
    "Accountant": {"Accounting and Bookkeeping", "Tally Erp. 9 with GST", "Tax Return Filing", "MS Office"},
    "Tax Consultant": {"Tax Return Filing", "MS Office", "Tally Erp. 9 with GST"},
    "Finance Assistant": {"Accounting and Bookkeeping", "MS Office", "Customer Relations"},
    "Administrative Executive": {"MS Office", "Customer Relations"},
    "Data Entry Operator": {"MS Office", "Tally Erp. 9 with GST"},
}

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_skills(text):
    skill_keywords = {
        "MS Office", "Accounting and Bookkeeping", "Tally Erp. 9 with GST",
        "Tax Return Filing", "Customer Relations"
    }
    found_skills = {skill for skill in skill_keywords if re.search(skill, text, re.IGNORECASE)}
    return found_skills

def recommend_jobs(skills_found):
    recommendations = []
    for role, skills_required in job_roles.items():
        matched = skills_found.intersection(skills_required)
        match_percent = (len(matched) / len(skills_required)) * 100
        if match_percent >= 50:
            recommendations.append((role, match_percent, matched))
    return recommendations

# ---------- Streamlit Interface ----------
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer & Job Recommender")
st.write("Upload your resume (PDF only) to get matching job recommendations based on your skills.")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:
    with st.spinner("Analyzing Resume..."):
        text = extract_text_from_pdf(uploaded_file)
        skills = extract_skills(text)
        matches = recommend_jobs(skills)

    st.success("✅ Resume Analyzed Successfully!")

    st.subheader("🧠 Skills Found:")
    for skill in skills:
        st.markdown(f"- {skill}")

    st.subheader("💼 Recommended Job Roles:")
    if matches:
        for role, percent, matched_skills in matches:
            st.markdown(f"**🔹 {role}** - {percent:.0f}% match")
            st.markdown(f"_Matched Skills:_ {', '.join(matched_skills)}")
            st.markdown("---")
    else:
        st.warning("No strong matches found. Try improving your resume or adding more skills.")
