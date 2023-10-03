import requests
import streamlit as st 
from streamlit_lottie import st_lottie



# from steamlink_lottie import st_lottie
from PIL import Image


#configuration
st.set_page_config(page_title="SetCitasApp", page_icon="💈", layout="wide")

# url ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"
url = "https://d1jj76g3lut4fe.cloudfront.net/saved_colors/76951/qvjIxEl6UiFxHDOD.json"



def load_lottie(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie = load_lottie(url)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/main.css")
email_address ="3d60creations@gmail.com"
 


#intro

with st.container():
    st.header("Welcome to Set Citas App 💈✂")
    st.title("Pariatur ea fugiat velit irure.")
    st.write("In aliqua ex esse aliquip enim tempor duis velit esse laboris esse culpa aute. Cupidatat exercitation do eu eiusmod voluptate dolor ea dolore Lorem deserunt aute. Tempor exercitation eiusmod qui exercitation dolor eu ipsum Lorem dolor.")

    st.write("[For More info >](https://setcitasapp.com/)")

# about us


with st.container():
    st.write("----")
    text_col, animation_col = st.columns(2)
    with text_col:
         st.header("About Set Citas App  ")
         st.write(
             """
             
             In aute consectetur cillum anim aliquip culpa cillum exercitation nostrud nostrud. Culpa sunt cupidatat et incididunt commodo laboris dolor do dolor ex ad et non. Aute quis consectetur incididunt quis consectetur ut aliqua ullamco tempor labore.

             -Deserunt magna irure laboris adipisicing deserunt. \n
             -Sunt do dolor quis officia mollit irure nostrud qui. \n
             -Ea minim reprehenderit Lorem ullamco consectetur commodo Lorem.\n
             -Nostrud ea incididunt cillum minim officia.\n
             -Cillum occaecat ullamco elit tempor laboris irure elit nulla.\n


             ***Duis sint laboris nulla dolore proident ipsum sunt laboris amet ex ipsum mollit*** cupidatat incididunt.
             
             """
         )
         st.write("[For More info >](https://setcitasapp.com/about)")

         with animation_col:
             st_lottie(lottie, height = 400)
            
  #  Services
  
with st.container():
    st.write("---")
    st.header("Services : ✂ 🫧 💇 🪒")  
    st.write("##")
    image_col, text_col = st.columns((1,2))
    with image_col:
        image = Image.open("img/delfina-pan.jpg")
        st.image(image, use_column_width=True)
    with text_col:
        st.subheader("Hair Cut Service")
        st.write(
            """

            Ipsum eu aliquip pariatur occaecat in sit esse commodo officia dolore quis ut. Ad proident consectetur aliqua elit occaecat fugiat laboris veniam anim consequat sint. Ex culpa ullamco velit officia reprehenderit id ex. Irure culpa duis labore cillum quis culpa irure voluptate. In ipsum cupidatat id non nostrud. Commodo non duis cupidatat nostrud incididunt cillum veniam laborum aliquip ea incididunt.

            """   
        )
        st.write("[For More Service >](https://setcitasapp.com/services/)")
             
#contact

with st.container():
    st.write("---")
    st.header("Contact us 📩")
    st.write("##")
    
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder = "Type Your Name Here" required>
     <input type="email" name="email" placeholder = "Type Your Email Here" required>
     <textarea type="message" name="message" placeholder = "Write Your Message Here" required></textarea>
     <button type="submit">Send</button>
    </form>
   
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    
    
