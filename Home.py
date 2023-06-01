import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
from pathlib import Path

# ------------------------------------------------------------------------------------------------------------------------
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# LOAD ASSETS ------------------------------------------------------------
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_glp2wakj.json")
img3 = Image.open("images/image1.png")

# HEADER SECTION ------------------------------------------------------------
with st.container():
    st.subheader("Welcome, I am Sally Ibaid :wave:")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img3)
with text_column:
 ##       st.subheader("Mechatronics engineer")
        st.write(
            """
            I am a Mechatronics Engineer with experience in embedded 
            systems and programming. I have experience in designing, 
            developing, and testing mechatronic systems. 
            """
        )

# SOCIAL LINKS ------------------------------------------------------------
EMAIL = "sky.sally1998@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sally-ibaid-30052a19a",
    "GitHub": "https://github.com/sallyibaid19",
    "Twitter": "https://twitter.com/skysala98",
}
      

st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



#  WHAT I DO ------------------------------------------------------------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - 👩‍💻 Programming: Python | C/C++  
            - 👩‍💻 embedded systems programmings
            - 📊 Matlab,SolidWorks ,Proteus and Inventor
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")