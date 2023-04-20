import streamlit as st
import os
from PIL import Image

wd = os.getcwd()

css_file = f"{wd}/styles/main.css"
cv_file = f"{wd}/assets/CV.jpg"
pdp_file = f"{wd}/assets/pdp.png"

PAGE_TITLE = "Clélia Deleplanque"
PAGE_ICON = "🌷"
NAME = "Clélia Deleplanque"
AGE = "21 Ans"
DESCRIPTION = """
🎨 Graphiste 🎨 

🌟 Community Manager 🌟
 
📢 Chargée de Com 📢

Mon Projet :

Aider les entreprises à développer leur identité 🚀
"""
EMAIL = "cleliadeleplanque59780@gmail.com"
SOCIAL_MEDIA = {
    "🔗 Linkedin 🔗": "https://www.linkedin.com/in/cl%C3%A9lia-deleplanque-communication/",
    "📷 Book Behance 📷": "https://www.behance.net/gallery/117427745/BOOK"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

with open(css_file) as f:
    st.markdown(f"<style>{f.read}</style>", unsafe_allow_html=True)
with open(cv_file, "rb") as cv:
    CVbyte = cv.read()
profile_pic = Image.open(pdp_file)

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=300)

with col2:
    st.title(NAME)
    st.subheader(AGE)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Télécharger mon CV ",
        data=CVbyte,
        file_name="CV Clélia Deleplanque",
        mime="application/octet-stream"
    )
    st.write("📧", EMAIL)

st.write("#")
st.subheader("Je vous invite à visiter :")

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

st.write("#")
st.subheader("Formations")
st.write("""
- 🎓 2021-2022 : Bachelor événementiel
- 🎓 2020-2021 : Double cursus Déco/Graphisme, CEPRECO à Roubaix
- 🎓 2020 : Bac STL, Lycée Charlotte Perriand
""")

st.write("#")
st.subheader("Expériences")
st.write("""
- ✅ Janvier 2023 - Aujourd'hui : Baby-sitting avec l'entreprise Kinougarde
- ✅ Décembre 2020 : Recruteur de donateur en porte à porte pour l'association Valentin Haüy
- ✅ Juillet - Août 2022 : Stage community manager chez Etika Spirulina, Villeneuve d'ascq
- ✅ Novembre 2021 : Bénévolat au Word Forum Responsible Economy, Lille
- ✅ Octobre 2021 : Bénévolat, Fabrique du changement au Vélodrome de Roubaix
""")

st.write("#")
st.subheader("Compétences")
st.write("""
- 💡 Relation Client
- 💡 Organisation
- 💡 Créativité
- 💡 Rigueur
- 💡 Dynamisme
- 💡 Rédaction
""")

st.write("#")
st.subheader("Logiciels")
st.write("""
- 🛠️ Suite Adobe
- 🛠️ Suite Office
- 🛠️ Canvas
""")
