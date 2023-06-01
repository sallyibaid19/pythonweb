import streamlit as st
from PIL import Image



img4 = Image.open("images/image2.png")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


st.title("Get In Touch With Me!")

# ---- CONTACT ----
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img4)
    # Documention: https://formsubmit.co/ 
    contact_form = """
    <form action="https://formsubmit.co/sky.sally1998@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


