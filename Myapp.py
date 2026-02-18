import streamlit as st
import pandas as pd 
import time
from google import genai

def cook_food(prompt):
    if prompt:
        msg = st.toast("Gathering ingredients...")
        time.sleep(2)
        msg = st.toast("Cooking...")
        time.sleep(2)
        msg = st.toast("Ready!", icon="🥞")
        time.sleep(2)
        st.write(f"So you want to prepare {prompt} today.")
        time.sleep(1)
        st.write("Let's see how you can make it.")
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=f"Write a summarized recipe on {prompt}")
        st.write(response.text)

# a function to pull up images goes here
# I will write this function later 

if __name__=="__main__":
    API_KEY = "AIzaSyBHNX9_ZyiQ4rdWKrD02sBFrN5kCT9imd4"   # YOUR API
    # initialize the client
    client = genai.Client(api_key=API_KEY)
    # title 
    st.title("Recipe Generator")
    prompt = st.chat_input("What's cooking?")
    cook_food(prompt)