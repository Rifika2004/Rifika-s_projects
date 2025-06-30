import streamlit as st
import requests

st.title("🗓️ Appointment Assistant")
st.write("Talk to me using plain English to book an appointment!")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:")

if user_input:
    st.session_state.messages.append(("You", user_input))

    try:
    res = requests.post(
        "https://rifika-s-projects.onrender.com/chat",
        json={"text": user_input},
        timeout=30
    )
    st.write(f"🔍 Raw backend response: `{res.text}`")  # ✅ This line is key
    reply = res.json().get("reply", "❌ Couldn't parse backend reply.")

    except Exception as e:
        reply = f"❌ Error: {e}"

    st.session_state.messages.append(("Bot", reply))

for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")

