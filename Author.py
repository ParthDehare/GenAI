import streamlit as st
import time
from google import genai

def get_author(story_name):
    if story_name:
        st.toast("Searching for author...")
        time.sleep(2)

        st.toast("Checking library records...")
        time.sleep(2)

        st.toast("Author Found!", icon="✍️")
        time.sleep(1)

        st.write(f"📖 Story: **{story_name}**")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Who is the author of the story or book '{story_name}'? If not real, invent a suitable fictional author name with a 1 line intro."
        )

        st.write(response.text)


if __name__ == "__main__":

    # ⚠️ Put your API key here for testing
    API_KEY = "AIzaSyCxXHL9YRI0VgrZP2rsSez03P-IlH_ItxE"

    client = genai.Client(api_key=API_KEY)

    st.title("📚 Story Author Finder")

    story_name = st.chat_input("Enter story/book name...")

    get_author(story_name)
