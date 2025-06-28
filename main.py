from fastapi import FastAPI
from pydantic import BaseModel
import datetime
from dateparser.search import search_dates
from mock_calendar import calendar

app = FastAPI()

class UserMessage(BaseModel):
    text: str

@app.post("/chat")
def chat(msg: UserMessage):
    text = msg.text

    # ⏱️ Smart date extraction from full text
    results = search_dates(
        text,
        settings={
            "PREFER_DATES_FROM": "future",
            "RETURN_AS_TIMEZONE_AWARE": True,
            "TIMEZONE": "Asia/Kolkata"
        }
    )

    if not results:
        return {"reply": "🤖 Hmm, I didn’t catch the time. Try something like 'tomorrow at 4 PM' or 'Monday at 10 AM'."}

    # 🎯 Grab the first detected datetime
    dt = results[0][1]
    print(f"🔍 Extracted datetime: {dt}")

    start = dt
    end = start + datetime.timedelta(minutes=30)

    if calendar.is_free(start, end):
        calendar.book(start, end, "Meeting")
        return {"reply": f"✅ Booked on {start.strftime('%Y-%m-%d %H:%M')}"}
    else:
        return {"reply": "❌ Sorry, that slot is taken. Try another time."}
        print("🔁 Deploying updated calendar...")

