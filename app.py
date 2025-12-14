import streamlit as st
import random

# ===============================
# STEP 1: AI-like expansion logic
# ===============================
def expand_point(topic, style):
    if style == "Educational":
        return f"{topic} is important because it helps people understand real-world concepts clearly and practically."
    elif style == "Motivational":
        return f"{topic} is something many people struggle with, but once you master it, your confidence improves."
    elif style == "Tech":
        return f"In the tech world, {topic} plays a major role in improving efficiency and performance."
    elif style == "Gaming":
        return f"In gaming, {topic} can directly affect your skills, reaction time, and decision-making."
    elif style == "Vlog":
        return f"{topic} plays a big role in everyday life and personal experiences."
    elif style == "Review":
        return f"{topic} needs honest evaluation before people make decisions."
    elif style == "Podcast":
        return f"{topic} is worth discussing deeply with real opinions and experiences."
    elif style == "Shorts / Reels":
        return f"{topic} needs to grab attention quickly and deliver value fast."
    elif style == "Comedy":
        return f"{topic} can be presented in a fun and entertaining way."
    else:
        return f"{topic} has a strong impact on daily life."

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

# ===============================
# STEP 2: Smart script generator
# ===============================
def generate_smart_script(topic, video_type, video_length, hook):
    if video_length == "30–60 seconds (Shorts)":
        return f"""
HOOK:
{hook} {topic}!

CONTENT:
{expand_point(topic, video_type)}
Most people ignore this, but it matters.

ENDING:
Follow for more content.
"""

    elif video_length == "3–5 minutes":
        return f"""
HOOK:
{hook} {topic}.

INTRO:
Welcome back to the channel.
Today we’re talking about {topic} and why it matters.

MAIN CONTENT:
{expand_point(topic, video_type)}

KEY INSIGHT:
Understanding {topic} helps you improve faster.

ENDING:
Like the video and subscribe.
"""

    elif video_length == "8–10 minutes":
        return f"""
HOOK:
{hook} {topic}.

INTRO:
Welcome back to the channel.
This video explains {topic} in detail.

SECTION 1 – WHAT IT IS:
{expand_point(topic, video_type)}

SECTION 2 – WHY IT MATTERS:
This impacts performance and results.

SECTION 3 – REAL EXAMPLES:
Applying {topic} in real life gives better outcomes.

ENDING:
Like, subscribe, and share this video.
"""

    else:  # 12–15 minutes
        return f"""
HOOK:
{hook} {topic}.

INTRO:
Welcome back to the channel.
Today’s video is a complete guide on {topic}.

SECTION 1 – BASICS:
{expand_point(topic, video_type)}

SECTION 2 – COMMON MISTAKES:
People often misuse {topic}.

SECTION 3 – HOW TO IMPROVE:
Consistency and practice matter.

SECTION 4 – REAL LIFE:
Those who apply {topic} perform better.

ENDING:
Thanks for watching till the end.
Subscribe for more.
"""

script = generate_smart_script(topic, video_type, video_length, hook)

if st.button("Generate Script"):
    if topic.strip() == "":
        st.error("Please enter a topic")
    else:
        hook = random.choice(hooks[video_type])
        script = generate_smart_script(topic, video_type, video_length, hook)

        st.subheader("📄 Generated Script")
        st.text(script)
        st.download_button(
            label="⬇️ Download Script (TXT)",
            data=script,
            file_name=f"{topic.replace(' ', '_')}_youtube_script.txt",
            mime="text/plain"
        )

