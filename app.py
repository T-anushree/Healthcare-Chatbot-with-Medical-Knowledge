from fastapi import FastAPI, Request
import mysql.connector
import openai

app = FastAPI()

# Connect DB
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="healthcare_chatbot"
)
cursor = db.cursor(dictionary=True)

# LLM API Key
openai.api_key = "your_openai_api_key"

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    # Query LLM for medical response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"You are a medical chatbot. Answer: {user_message}",
        max_tokens=150
    )

    return {"reply": response.choices[0].text.strip()}

@app.post("/appointment")
async def book_appointment(request: Request):
    data = await request.json()
    user_id, doctor, date = data["user_id"], data["doctor_name"], data["date"]

    cursor.execute("INSERT INTO appointments (user_id, doctor_name, appointment_date) VALUES (%s,%s,%s)",
                   (user_id, doctor, date))
    db.commit()
    return {"status": "Appointment Scheduled"}
