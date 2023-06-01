import streamlit as st
from PIL import Image

img1 = Image.open("images/pro1.png")
img2 = Image.open("images/pro2.png")
img5 = Image.open("images/pro3.png")
img7 = Image.open("images/pp.png")


# Start Page ---------------------------------------------------------------------------
with st.container():
    st.title("My Projects")
    image_column, text_column = st.columns((2, 2))
    with image_column:
        st.image(img7)


# PROJECTS1 ---------------------------------------------------------------------------
with st.container():
    st.write("---")
    st.write("##")    
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img1)
with text_column:
        st.subheader("Door lock project (PIC microcontroller)")
        st.write(
            """
            This project aims to create a security system that requires a unique password input. 
            """
        )
        st.markdown("[PROJECTS LINK...](https://github.com/sallyibaid19/password_lock_door_project)")

# PROJECTS2 ---------------------------------------------------------------------------
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img2)
    with text_column:
        st.subheader("Air conditioning System Based  on ARM")
        st.write(
            """
            The project consists of control systems implemented in Air conditioning;
            the project is implemented on STM32F401 ARM microcontroller.

            """
        )
        st.markdown("[PROJECTS LINK...](https://github.com/sallyibaid19/00STM32_PRO)")

# PROJECTS3 ---------------------------------------------------------------------------
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img5)
    with text_column:
        st.subheader(" Bank System (C)")
        st.write(
            """
             C Language Project to establish a new account, change existing account information, 
             see and manage transactions, verify the details of an existing account, 
             delete an existing account, and browse a list of customers.
            """
        )
        st.markdown("[PROJECTS LINK...](https://github.com/sallyibaid19/00STM32_PRO)")

