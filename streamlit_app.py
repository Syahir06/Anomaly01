import streamlit as st

# ---- Page Setup ----
st.set_page_config(page_title="My Resume", page_icon="📄", layout="centered")

# ---- Header Section ----
st.title("Mohd Syahir's Resume")

# ---- Contact Information ----
st.header("📞 Contact Information")
st.write("""
**Email:** syahir@example.com  
**Phone:** +60 17-925 4055  
**LinkedIn:** [linkedin.com/in/syahirprofile](https://linkedin.com/in/syahirprofile)
""")

# ---- Education ----
st.header("🎓 Education")
st.write("""
**Bachelor of Computer Science (Data Science)**  
Universiti Malaysia Kelantan, 2022–2026
""")

# ---- Work Experience ----
st.header("💼 Work Experience")
st.write("""
**Intern – Data Analyst**, TechVision Sdn Bhd (June–August 2024)  
- Analyzed customer data using Python and Power BI  
- Automated reporting with Pandas and Excel  
""")

# ---- Skills ----
st.header("🛠 Skills")
col1, col2 = st.columns(2)
with col1:
    st.write("- Python")
    st.write("- Machine Learning")
    st.write("- Streamlit")
with col2:
    st.write("- SQL")
    st.write("- Power BI")
    st.write("- Data Visualization")

# ---- Projects ----
st.header("🚀 Projects")
st.write("""
**Smart Irrigation System Using IoT**  
Designed a smart irrigation system using ESP32 and sensors to optimize water usage.

**Traffic Volume Prediction Using LSTM**  
Developed an LSTM-based model to predict vehicle traffic volume based on real-world data.
""")

# ---- Achievements ----
st.header("🏆 Achievements")
st.write("""
- Dean’s List (1 semesters)  
- 1st Place, UMK Data Science Hackathon 2024
""")

# ---- Footer ----
st.markdown("---")
st.markdown("© 2025 Mohd Syahir | Built with ❤️ using Streamlit")
