import streamlit as st
import random

st.set_page_config(page_title="YouTube Script Generator", layout="centered")

st.title("🎬 YouTube Script Generator (Free)")

st.write("Generate simple YouTube video scripts without any paid AI.")

# User inputs
topic = st.text_input("Enter your video topic")
video_type = st.selectbox(
    "Select video type",
    [
        "Educational",
        "Motivational",
        "Tech",
        "Story",
        "Gaming",
        "Vlog",
        "Review",
        "Podcast",
        "Shorts / Reels",
        "Comedy"
    ]
)
video_length = st.selectbox(
    "Select video duration",
    [
        "30–60 seconds (Shorts)",
        "3–5 minutes",
        "8–10 minutes",
        "12–15 minutes"
    ]
)

# Script templates
hooks = {
    "Educational": [
        "Have you ever wondered about",
        "Most people don’t understand",
        "Today, we are going to learn"
    ],
    "Motivational": [
        "Let me tell you something important",
        "If you feel like giving up, listen to this",
        "This message can change your life"
    ],
    "Tech": [
        "In today’s video, we’ll talk about",
        "This technology is changing everything",
        "If you love tech, you must know this"
    ],
    "Story": [
        "This is a story you’ve never heard before",
        "Once upon a time",
        "Let me tell you an interesting story"
    ]
}

if st.button("Generate Script"):
    if topic.strip() == "":
        st.error("Please enter a topic")
    else:
        hook = random.choice(hooks[video_type])

        script = f"""
HOOK:
{hook} {topic}.

INTRO:
In this video, we are going to talk about {topic}.
Make sure you watch till the end.

MAIN CONTENT:
Let’s break down {topic} step by step.
This is important because it affects our daily life.

ENDING:
If you found this video helpful, like the video,
subscribe to the channel, and share it with others.
"""

        st.subheader("📄 Generated Script")
        st.text(script)
       st.download_button(
    label="⬇️ Download Script (TXT)",
    data=script,
    file_name=f"{topic.replace(' ', '_')}_youtube_script.txt",
    mime="text/plain"
)
 
