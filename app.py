import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import time

# ---------------- UI ----------------
st.set_page_config(layout="wide")
st.markdown("""
<style>
.stApp { background-color: #0e1117; color: white; }
</style>
""", unsafe_allow_html=True)

st.title("🎭 Face Morphix - Live")

col1, col2 = st.columns(2)
frame_placeholder = col1.empty()
anime_placeholder = col2.empty()
emotion_text = st.empty()

# ---------------- MEDIAPIPE ----------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True
)

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    st.error("Camera not detected ❌")
    st.stop()

# ---------------- LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    emotion = "neutral"

    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark

    # Face width (reference scale)
        face_width = abs(landmarks[234].x - landmarks[454].x)

    # Mouth open ratio
        mouth_open = abs(landmarks[13].y - landmarks[14].y) / face_width

    # Eye open ratio
        eye_open = abs(landmarks[159].y - landmarks[145].y) / face_width

    # Mouth corners (sad detection)
        mouth_curve = (landmarks[61].y - landmarks[291].y) / face_width

    # ---------- Emotion Logic ----------

    # HAPPY (big smile / mouth open)
        if mouth_open > 0.25:
            emotion = "happy"

    # SAD (mouth closed + corners down)
        elif mouth_open < 0.12 and mouth_curve > 0.015:
            emotion = "sad"

    # ANGRY (eyes slightly squeezed + mouth closed)
        elif eye_open < 0.08 and mouth_open < 0.15:
            emotion = "angry"

    # NEUTRAL
        else:
            emotion = "neutral"
    # Load anime image
    anime_img = cv2.imread(f"assets/{emotion}.png")

    if anime_img is None:
        st.error(f"Image assets/{emotion}.png not found ❌")
        break

    anime_img = cv2.cvtColor(anime_img, cv2.COLOR_BGR2RGB)

    # Display
    frame_placeholder.image(rgb, channels="RGB")
    anime_placeholder.image(anime_img, channels="RGB")
    emotion_text.markdown(f"### Current Emotion: **{emotion.upper()}**")

    time.sleep(0.03)

cap.release()