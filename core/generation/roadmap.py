import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_roadmap(missing_skills, target_role, cv_text):
    if not missing_skills:
        return "Tebrikler! Rol için tüm kritik yeteneklere sahipsin. Mevcut projelerini derinleştirmeye odaklanabilirsin."

    prompt = f"""
    Sen uzman bir teknoloji kariyer koçusun. 
    Adayın hedef rolü: {target_role}
    Eksik yetenekleri: {', '.join(missing_skills)}
    Adayın CV özeti: {cv_text[:1000]}

    Bu eksikleri kapatmak için adaya özel 4 haftalık bir gelişim planı hazırla.
    Formatın çok şık olsun, her hafta için spesifik bir GitHub proje fikri ver.
    Cevabı Markdown formatında ver.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Eğer bütçen varsa gpt-4o daha iyi sonuç verir
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Yapay Zeka şu an meşgul: {str(e)}"