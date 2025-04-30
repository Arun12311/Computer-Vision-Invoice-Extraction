from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input,image):
    if input !="":
        response = model.generate_content([input,image])
        parts=response.candidates[0].content.parts
        text=' '.join(part.text for part in parts)
        return text

st.set_page_config(page_title="Gemini AI",page_icon="🚀")
st.header("Gemini AI")
input=st.text_input("Enter your text here:", key="input")
upload_file=st.file_uploader("Upload an image",type=["jpg","png"])

if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded Image")

submit=st.button("Tell me about image ")

if submit:
    response=get_gemini_response(input,image)
    st.subheader("The response is:")
    st.write(response)