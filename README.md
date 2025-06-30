# 🤖 Appointment Assistant with LangGraph-Style Mock Calendar

This is a conversational appointment booking app powered by FastAPI and Streamlit.  
It understands natural language like "Book a meeting tomorrow at 4 PM" and checks availability in a mock calendar.

---

### 🔗 Live Demo

👉 [Try the Assistant on Streamlit](https://appointment-assistant-2p8sadtwbzcedjozhxxmdh.streamlit.app/)  
👉 Backend API (FastAPI): [https://rifika-s-projects.onrender.com/chat](https://rifika-s-projects.onrender.com/chat)

---

### 💡 Features

- Understands natural English phrases like:
  - “Book a slot at 5 PM tomorrow”
  - “Can I meet on Monday at 3?”
- Checks a mock calendar for availability
- Prevents double booking
- Uses `dateparser` to extract date and time intelligently
- Frontend: **Streamlit**
- Backend: **FastAPI** (deployed on Render)

---

### 📦 Tech Stack

- Python
- FastAPI
- Streamlit
- LangGraph-style logic flow
- `dateparser`, `pydantic`, `uvicorn`
- Deployed via **Streamlit Cloud** and **Render**

---

### 🛠️ How It Works

1. User types a message like “Book an appointment at 2 PM today”
2. The Streamlit frontend sends it to the FastAPI backend
3. FastAPI parses the date & checks availability
4. If the slot is free, it's booked; else, the user is asked to try another time

---

### 📁 Project Structure

