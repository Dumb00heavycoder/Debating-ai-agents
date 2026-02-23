#hi
import os 
import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

openai_client = OpenAI(api_keys = os.getenv("First_Key"))

GROK_API_KEY = os.getenv("Second_Key")
