import streamlit as st
import sounddevice as sd
import numpy as np
import scipy.io.wavfile
import tempfile
import random

st.set_page_config(page_title="MoodMatch", page_icon="🎧", layout="centered")

st.title("🎧 MoodMatch – מזהה מצב הרוח שלך לפי הקול!")
st.write("הקלט משפט קצר (למשל: *היום שלי היה ממש...*) ונגיד לך מה מצב הרוח שלך וניתן המלצה 😄")

duration = 5  # משך הקלטה בשניות

if st.button("🎤 התחל הקלטה"):
    st.info("מקליט... דבר עכשיו!")
    fs = 44100
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        scipy.io.wavfile.write(f.name, fs, recording)
        st.success("ההקלטה הסתיימה!")

        # הדמיה של זיהוי מצב רוח (נבנה בהמשך קוד חכם אמיתי)
        mood = random.choice(["שמח", "עצבני", "עייף", "עצוב", "מתוח"])

        st.subheader(f"🎯 נראה שאתה: **{mood}**")

        if mood == "שמח":
            st.success("💃 שים מוזיקה שמרימה אותך!")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        elif mood == "עצבני":
            st.warning("😂 הנה בדיחה: למה הפיצה לא הלכה לבית הספר? כי היא פחדה מהתנור!")
        elif mood == "עייף":
            st.info("🧘‍♂️ תרגול נשימה: נשום עמוק 3 פעמים...")
        elif mood == "עצוב":
            st.video("https://www.youtube.com/watch?v=8ZcmTl_1ER8")  # סרטון מצחיק
        elif mood == "מתוח":
            st.info("📵 קח הפסקה קצרה, אולי תצא לטיול קצר 🏞️")

st.markdown("---")
st.markdown("🧪 פיתוח ראשוני • נבנה באהבה 💙")
