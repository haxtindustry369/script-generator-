import streamlit as st
import random

# ===============================
# PAGE CONFIG + UI STYLE
# ===============================
st.set_page_config(page_title="Creator Script AI", layout="centered")

st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.stButton>button {
    width: 100%;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ===============================
# SESSION LIMIT (MONETIZATION)
# ===============================
if "count" not in st.session_state:
    st.session_state.count = 0

# ===============================
# VIRAL ELEMENTS
# ===============================
viral_hooks = [
    "Before you do anything, watch this till the end.",
    "Most people make this mistake.",
    "This might save you a lot of money.",
    "Don’t skip this if you care about results.",
    "Nobody tells you this truth."
]

retention_lines = [
    "But the most important part is coming next.",
    "Stay till the end to avoid mistakes.",
    "This one point changes everything.",
    "Wait — this is crucial."
]

# ===============================
# AI-LIKE EXPANSION LOGIC
# ===============================
def expand_point(topic, style):
    if style == "Educational":
        return f"{topic} helps people understand important concepts clearly and practically."
    elif style == "Motivational":
        return f"{topic} is something many people struggle with, but mastering it builds confidence."
    elif style == "Tech":
        return f"In the tech world, {topic} plays a major role in performance and efficiency."
    elif style == "Gaming":
        return f"In gaming, {topic} directly affects skills, reaction time, and decision-making."
    elif style == "Vlog":
        return f"{topic} connects strongly with everyday life and personal experience."
    elif style == "Review":
        return f"{topic} needs honest evaluation before making decisions."
    elif style == "Podcast":
        return f"{topic} is perfect for deep discussion and opinions."
    elif style == "Shorts / Reels":
        return f"{topic} must grab attention fast and deliver value quickly."
    elif style == "Comedy":
        return f"{topic} can be explained in a fun and entertaining way."
    else:
        return f"{topic} impacts daily life more than people realize."

# ===============================
# SMART SCRIPT GENERATOR
# ===============================
def generate_smart_script(topic, video_type, video_length, hook):
    viral = random.choice(viral_hooks)
    retain = random.choice(retention_lines)

    if video_length == "30–60 seconds (Shorts)":
        return f"""
HOOK:
{viral}

CONTENT:
{expand_point(topic, video_type)}
{retain}

ENDING:
Follow for more useful content!
"""

    elif video_length == "3–5 minutes":
        return f"""
HOOK:
{viral} {hook} {topic}.

INTRO:
Welcome back to the channel.
Today we’re talking about {topic} and why it matters.

MAIN CONTENT:
{expand_point(topic, video_type)}
Note this carefully.

{retain}

ENDING:
Like the video and subscribe.
"""

    elif video_length == "8–10 minutes":
        return f"""
HOOK:
{viral} {hook} {topic}.

INTRO:
Welcome back.
This video explains {topic} in detail.

SECTION 1 – WHAT IT IS:
{expand_point(topic, video_type)}

SECTION 2 – WHY IT MATTERS:
This affects real-world performance.

SECTION 3 – EXAMPLES:
People applying {topic} correctly see better results.

{retain}

ENDING:
Like, subscribe, and share.
"""

    else:
        return f"""
HOOK:
{viral} {hook} {topic}.

INTRO:
Welcome back.
This is a complete guide on {topic}.

SECTION 1 – BASICS:
{expand_point(topic, video_type)}

SECTION 2 – COMMON MISTAKES:
Most people misuse or ignore this.

SECTION 3 – HOW TO IMPROVE:
Consistency and learning matter.

SECTION 4 – REAL LIFE:
Those who apply {topic} perform better.

{retain}

ENDING:
Thanks for watching till the end.
Subscribe for more.
"""

# ===============================
# UI CONTENT
# ===============================
st.title("🎬 Creator Script AI")
st.caption("Generate viral YouTube scripts — 100% free")

topic = st.text_input("Enter your video topic")

video_type = st.selectbox(
    "Select video type",
    [
        "Educational", "Motivational", "Tech", "Story", "Gaming",
        "Vlog", "Review", "Podcast", "Shorts / Reels", "Comedy"
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

hooks = {
    "Educational": ["Have you ever wondered about", "Most people don’t understand", "Today we’ll learn"],
    "Motivational": ["Let me tell you something important about", "If you feel stuck, listen to this about"],
    "Tech": ["In today’s video we’ll talk about", "This technology is changing"],
    "Story": ["This is a story about", "Once upon a time"]
}

# ===============================
# GENERATE BUTTON
# ===============================
if st.button("🚀 Generate Script"):
    if topic.strip() == "":
        st.error("Please enter a topic")
    elif st.session_state.count >= 2:
        st.warning("Free limit reached. 💎 Contact on WhatsApp for Pro access.")
    else:
        hook = random.choice(hooks.get(video_type, ["Let’s talk about"]))
        script = generate_smart_script(topic, video_type, video_length, hook)
        st.session_state.count += 1

        st.subheader("📄 Generated Script")
        st.text_area("Your Script", script, height=420)

        st.download_button(
            "⬇️ Download Script (TXT)",
            script,
            file_name=f"{topic.replace(' ', '_')}_youtube_script.txt",
            mime="text/plain"
        )

st.info("💎 Want unlimited scripts? MAIL US : haxtindustry369@gmail.com")
