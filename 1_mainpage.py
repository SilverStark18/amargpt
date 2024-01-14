import streamlit as st
import os
import json
from streamlit_lottie import st_lottie
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image


load_dotenv()  ## loading all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

from streamlit_option_menu import option_menu
 ##initialize our streamlit app
st.set_page_config(page_title="AMAR GPT", page_icon='🦅')  # page title
#with st.sidebar:

#code for lottie file animation
def load_lottiefiles(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

# Use option_menu with the defined styles
selected = option_menu(
    menu_title=None,
    options=["NEW CHAT", "CHAT HISTORY", "CREDITS"],
    icons=['house', 'chat', 'person'],
    default_index=0,
    menu_icon='cast',
    orientation="horizontal",
)


if selected == "NEW CHAT":
    def get_gemini_response(question):
        response = chat.send_message(question, stream=True)
        return response
    st.header("𝐀𝐦𝐚𝐫𝐆𝐏𝐓 🦅 based on    Gemini LLM Application")  # title in the web page

    lottie_hi = load_lottiefiles(r'higpt.json')
    st_lottie(
        lottie_hi, loop=True, quality="high", speed=1.65, key=None, height=450)

    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    input_text = st.text_input("Input: ", key="input",help="Type your question here.")
    submit_button = st.button("Ask the question",help="Submit your question here.")
    if submit_button and input_text:
        response = get_gemini_response(input_text)
        # Add user query and response to session state chat history
        st.session_state['chat_history'].append(("You", input_text))
        st.success("The Response is")
       
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("BOT", chunk.text))

if selected == 'CHAT HISTORY':
    st.title("CHAT HISTORY")
    
    # Display chat history with animation
    lottie_chat = load_lottiefiles(r'askchat.json')
    st_lottie(lottie_chat, loop=True, quality="high", speed=1.65, key=None, height=450)
    
    # Display chat history if the button is clicked
    if st.button("Show Chat History"):
        if 'chat_history' in st.session_state and st.session_state['chat_history']:
            st.subheader("The Chat History is")
            for role, text in st.session_state['chat_history']:
                st.write(f"{role}: {text}")
        else:
            st.error("Chat History is empty. Start asking questions to build the history.")



if selected == 'CREDITS':
    lottie_credit = load_lottiefiles(r"thankyou bymonkeymoji.json")
    st_lottie(lottie_credit, loop=True,quality="high", speed=1.25, key=None, height=350)
    st.title("CRAFTED BY :")
    st.subheader("AMARNATH SILIVERI")

# Define your styles
    st.markdown("""
<style>
  .social-icons {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 20px;
  }

  .social-icon {
    text-align: center;
  }
</style>
""", unsafe_allow_html=True)

# Create a container for social icons
    st.markdown("""
<div class="social-icons">
  <div class="social-icon">
    <a href="https://www.github.com/SilverStark18" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/github.svg" width="32" height="32" alt="GitHub" />
    </a>
    <p>GitHub</p>
  </div>

  <div class="social-icon">
    <a href="http://www.instagram.com/itz.__.amar.__" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/instagram.svg" width="32" height="32" alt="Instagram" />
    </a>
    <p>Instagram</p>
  </div>

  <div class="social-icon">
    <a href="http://www.linkedin.com/in/amarnath-siliveri18" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/linkedin.svg" width="32" height="32" alt="LinkedIn" />
    </a>
    <p>LinkedIn</p>
  </div>

  <div class="social-icon">
    <a href="https://medium.com/@amartalks25603" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/medium.svg" width="32" height="32" alt="Medium" />
    </a>
    <p>Medium</p>
  </div>

  <div class="social-icon">
    <a href="https://www.x.com/Amarsiliveri" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/twitter.svg" width="32" height="32" alt="Twitter" />
    </a>
    <p>Twitter</p>
  </div>

  <div class="social-icon">
    <a href="https://www.threads.net/@itz.__.amar.__" target="_blank" rel="noreferrer">
      <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/socials/threads.svg" width="32" height="32" alt="Threads" />
    </a>
    <p>Threads</p>
  </div>
</div>
""", unsafe_allow_html=True)
    st.subheader("------------------------------------------------------------------------------------------------")
    st.success(" Stay in the loop and level up your knowledge with every follow! ")
    st.success("Do you see icons , click to follow  on SOCIAL")


