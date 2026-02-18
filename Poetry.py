import streamlit as st
import time
from google import genai
import os

def tell_story(prompt):
    if prompt:
        st.toast("Thinking of a story...")
        time.sleep(2)

        st.toast("Creating characters...")
        time.sleep(2)

        st.toast("Story Ready!", icon="📖")
        time.sleep(1)

        st.write(f"✨ Here is a story about **{prompt}**")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Write a short imaginative story about {prompt} and mention a fictional author name at the end."
        )

        st.write(response.text)


if __name__ == "__main__":

    # 🔐 Use environment variable for safety
    API_KEY = "AIzaSyBHNX9_ZyiQ4rdWKrD02sBFrN5kCT9imd4"

    client = genai.Client(api_key=API_KEY)

    st.title("📚 AI Story Teller")

    prompt = st.chat_input("Enter a topic for your story...")

    tell_story(prompt)
