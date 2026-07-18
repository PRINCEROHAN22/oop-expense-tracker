import os 
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client= Groq(api_key=os.getenv("GROQ_API_KEY"))

def suggest_category(description:str)->str:
    prompt = f"""Given this expense description, suggest ONE category from this list only:
    Food, Travel, Shopping, Bills, Entertainment, Health, Other.
    
    Description:"{description}"

    Reply with ONLY the category word, nothing else."""
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}],
        temperature=0,
        max_tokens=10
    )
    return response.choices[0].message.content.strip()