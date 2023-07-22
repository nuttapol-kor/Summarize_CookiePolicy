from fastapi import FastAPI, HTTPException
from repo.text_summarize import summarize
from dotenv import load_dotenv
import os
import openai

load_dotenv()
app = FastAPI()

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.post("/generate_text/")
async def generate_text(prompt: str):
    summarize_text = summarize(prompt)
    
    try:
        prompt = summarize_text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            n=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            messages=[
                {"role": "system", "content": "You are an expert compliance and your native language is Thai. Summarize about policy and cookie in Thai that the user enters. Prompt from user was came from summarize model that maybe give you not full sentances, so you have try to complate the sentence for the user. User want short sentences to response back maybe not exceed 150 token"},
                {"role": "user", "content": prompt},
            ],
        )
    except Exception as e:
        print("Error in creating campaigns from openAI:", str(e))
        return 503
    return response["choices"][0]["message"]["content"]

