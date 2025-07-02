from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import openai

load_dotenv()  # .env 로드
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class SummaryRequest(BaseModel):
    content: str

@app.post("/summarize")
async def summarize(req: SummaryRequest):
    prompt = f"다음 내용을 요약해줘:\n\n{req.content}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            { "role": "user", "content": prompt }
        ]
    )
    return { "summary": response.choices[0].message.content.strip() }
