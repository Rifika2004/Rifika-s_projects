import streamlit as st
import requests

st.title("🗓️ Appointment Assistant with LangGraph Mock Calendar")
st.write("Talk to me using plain English to book an appointment!")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("You:")

if user_input:
    st.session_state.messages.append(("You", user_input))

    try:
        res = requests.post("https://rifika-s-projects.onrender.com/chat", json={"text": user_input})
        st.write("🔍 Response status code:", res.status_code)
        st.write("📄 Raw text:", res.text)
        res.raise_for_status()  # This will raise HTTPError if status is 4xx or 5xx
        reply = res.json().get("reply", "❌ Couldn't parse backend reply.")
    except Exception as e:
        reply = f"❌ Error: {e}"

    st.session_state.messages.append(("Bot", reply))

for sender, msg in st.session_state.messages:
    st.write(f"**{sender}:** {msg}")
