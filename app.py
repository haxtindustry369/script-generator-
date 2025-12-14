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
        return f"In gaming, {topic} can directly affect skills, reaction time, and decision-making."
    elif style == "Vlog":
        return f"{topic} plays a big role in everyday life and personal experiences."
    elif style == "Review":
        return f"{topic} needs honest evaluation before people make decisions."
    elif style == "Podcast":
        return f"{topic} is worth discussing deeply with real opinions and experiences."
    elif style == "Shorts / Reels":
        return f"{topic} must grab attention quickly and deliver value fast."
    elif style == "Comedy":
        return f"{topic} can be presented in a fun and entertaining way."
    else:
        return f"{topic} has a strong impact on daily life."

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
Most people ignore this, but it actually matters.

ENDING:
Follow for more useful content!
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
When you understand {topic}, your results improve naturally.

ENDING:
Like the video and subscribe for more.
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
This directly affects performance and results.

SECTION 3 – REAL EXAMPLES:
People applying {topic} correctly see better outcomes.

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
Many people misunderstand or misuse {topic}.

SECTION 3 – HOW TO IMPROVE:
Consistency, learning, and practice matter.

SECTION 4 – REAL LIFE:
Those who apply {topic} perform better over time.

ENDING:
Thanks for watching till the end.
Subscribe for more content.
"""

# ===============================
# Streamlit UI
# ===============================
st.set_page_config(page_title="YouTube Script Generator", layout="centered")

st.title("🎬 YouTube Script Generator (Free)")
st.write("Generate full YouTube video scripts without any paid AI.")

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

# Hooks
hooks = {
    "Educational": [
        "Have you ever wondered about",
        "Most people don’t understand",
        "Today, we are going to learn"
    ],
    "Motivational": [
        "Let me tell you something important about",
        "If you feel like giving up, listen to this about",
        "This message can change your life regarding"
    ],
    "Tech": [
        "In today’s video, we’ll talk about",
        "This technology is changing everything about",
        "If you love tech, you must know this about"
    ],
    "Story": [
        "This is a story you’ve never heard before about",
        "Once upon a time, something happened related to",
        "Let me tell you an interesting story about"
    ]
}

# Generate button
if st.button("Generate Script"):
    if topic.strip() == "":
        st.error("Please enter a topic")
    else:
        hook = random.choice(hooks.get(video_type, ["Let’s talk about"]))
        script = generate_smart_script(topic, video_type, video_length, hook)

        st.subheader("📄 Generated Script")
        st.text(script)

        st.download_button(
            label="⬇️ Download Script (TXT)",
            data=script,
            file_name=f"{topic.replace(' ', '_')}_youtube_script.txt",
            mime="text/plain"
        )
