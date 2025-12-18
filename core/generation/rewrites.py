import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def suggest_rewrites(cv_text):
    prompt = f"""
    Sen bir kıdemli İK uzmanısın. Aşağıdaki CV metnini incele:
    {cv_text[:2000]}
    
    Lütfen bu CV'deki 3 cümleyi seç ve onları daha etkileyici, 
    sayısal veri içeren ve aksiyon odaklı (STAR metodu) olacak şekilde yeniden yaz.
    Format:
    - Orijinal: ...
    - Öneri: ...
    - Neden: ...
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Öneriler hazırlanırken bir hata oluştu: {e}"