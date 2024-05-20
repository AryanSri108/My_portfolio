import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie


#TODO Function to load lottie animations
def LoadLottieUrl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    else:
        return r.json()

def LoadLottieUrl2(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    else:
        return r.json()

def LoadLottieUrl3(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    else:
        return r.json()

def LoadLottieUrl4(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    else:
        return r.json()

def LoadLottieUrl5(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    else:
        return r.json()


#TODO Load a lottie animation
lottieanimation = LoadLottieUrl("https://lottie.host/2fa8f3d4-553d-4ae7-baff-d42d8a76adea/GMzf2p4cLv.json")
lottieanimation2 = LoadLottieUrl2("https://lottie.host/43198d4f-81f5-4d78-932d-29ff47d2da9b/jxpdHR0GNE.json")
lottieanimation3 = LoadLottieUrl3("https://lottie.host/f3589817-cbc9-4a12-9c21-8b330171fd73/FI21yKCtrv.json")
lottieanimation4 = LoadLottieUrl4("https://lottie.host/c5bec734-1244-4167-843d-99c68e4e2e32/8IPdTcdlIt.json")
lottieanimation5 = LoadLottieUrl5("https://lottie.host/ce1e4918-1850-4ea1-9471-27f608212890/5d5xsXGVXu.json")


#TODO MYStreamlit application starts here
st.set_page_config("My Portfolio:wave:",page_icon=":infinity:",layout="wide")

#TODO Sidebar menu using streamlit_option_menu
with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home","Projects","Skills","Contact"],
        icons=["house-door-fill","filetype-py","code","person-rolodex"],
        menu_icon="list",
        styles={"icon": {"color":"red"}},
        default_index=0,
    )

#TODO Home Section
if selected == "Home":
    st.title("Welcome to my Portfolio! :wave:")
    st.write("Hi , I am Aryan Srivastava a passionate Python developer with a knack for crafting efficient, elegant solutions.",
     "From python to Machine Learning, I thrive on turning ideas into code.",
     "With a solid foundation in python engineering principles and a keen eye for detail, I'm dedicated to delivering high-quality projects that exceed expectations.")
    if lottieanimation:
        st_lottie(lottieanimation,height=300,key="coding")

#TODO Projects Section
elif selected == "Projects":
    st.title("My Projects :computer:")
    st.write("Here are some of my projects :")
    #TODO Adding project details
    st.write("1. Laptop price predictor (Machine Learning) - My Laptop Price Predictor project forecasts laptop prices accurately",
    "simplifying buying decisions. Demonstrates my data and tech skills effectively")
    if lottieanimation5:
        st_lottie(lottieanimation5,height=200,key="coding")

    st.write("2. Password Generator (Python) - This Streamlit app generates a strong password based on user input for length. It combines letters, digits",
     "and punctuation, then displays the generated password when the user clicks the Generate Password button.")
    if lottieanimation2:
        st_lottie(lottieanimation2,height=200)


# Skills Section
elif selected == "Skills":
    st.title("Technical Skills :books:")
    st.write("Here are some of my Technical Skills:")
    st.write("Language - Python & Good knowledge of oops")
    st.write("Database - MySQL")
    st.write("Developer tools - Visual studio code,Pycharm,Replit,Jupyternotebook")
    st.write("Version Control - Git & Github")
    if lottieanimation3:
        st_lottie(lottieanimation3,height=300,key="coding")


# Contact Section
# elif selected == "Contact":
#     if lottieanimation4:
#         st_lottie(lottieanimation4,height=200,key="coding")
#         st.title("Contact Me :telephone_receiver:")

#     st.write("Feel free to reach out to me:")
#     st.write("Mobile:calling:", 6397384758,6396079050)
#     st.write("whatsapp:iphone:", 6396079050)
#     st.write("Gmail:envelope_with_arrow: [aryanshrivastava573@gmail.com]")
#     st.write("LinkedIn:link: [https://www.linkedin.com/in/aryan-srivastava-139bb8228/]")
    
elif selected == "Contact":
    if lottieanimation4:
        st.title("Contact Me :telephone_receiver:")
        st.write("Feel free to reach out to me:")
        # Container for aligning content to the left
        col1, col2 = st.columns([1, 4])  # Adjust the width ratios as needed
        with col1:
            st_lottie(lottieanimation4, height=100, key="coding")
        with col2:
            st.write("Mobile :calling:", 6397384758, 6396079050)
            st.write("WhatsApp :iphone:", 6396079050)
            st.write("Gmail :envelope_with_arrow: [aryanshrivastava573@gmail.com]")
            st.write("LinkedIn:link: [https://www.linkedin.com/in/aryan-srivastava-139bb8228/]")
            st.write("Github:computer: [https://github.com/AryanSri108]")
    
