import os 
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

#gemini
genai.configure(api_key = os.getenv("Gemini_API_Key")) 
gemini_model = genai.GenerativeModel("gemini-1.5-flash")
def gemini_call(system_prompt, user_prompt):
    prompt = f"""
    {system_prompt}

    User:
    {user_prompt}"""
    response = gemini_model.generate_content(prompt)
    return response.text

#groq
Groq_API_Key = os.getenv("GROQ_API_KEY")

def groq_call(system_prompt, user_prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = { 
          "Authorization" : f"Bearer {Groq_API_Key}",
          "Content-Type" : "application/json"
        }

    data = {
            "models": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.6
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()["choices"][0]["message"]["content"]

