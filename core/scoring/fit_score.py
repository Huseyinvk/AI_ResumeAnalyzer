def compute_skill_coverage(cv_skills_set, target_set):
    """
    İki set arasındaki örtüşme oranını hesaplar.
    """
    if not target_set:
        return 1.0
    intersection = cv_skills_set & target_set
    return len(intersection) / len(target_set)

def calculate_fit_score(cv_profile: dict, role_spec: dict) -> dict:
    """
    Ürün tanımındaki hibrit skorlama mantığını uygular ve eksikleri bulur.
    """
    # Karşılaştırma kolaylığı için her şeyi küçük harfe çeviriyoruz
    cv_skills_lower = {s.lower() for s in cv_profile.get("skills", [])}
    must_have_orig = role_spec.get("must_have", [])
    nice_to_have_orig = role_spec.get("nice_to_have", [])
    
    must_have_set = {s.lower() for s in must_have_orig}
    nice_to_have_set = {s.lower() for s in nice_to_have_orig}
    
    # 1. Eksik Yetenekleri Belirleme
    missing_must = [s for s in must_have_orig if s.lower() not in cv_skills_lower]
    missing_nice = [s for s in nice_to_have_orig if s.lower() not in cv_skills_lower]
    
    # 2. Yetenek Skorunu Hesaplama (Ağırlıklı: Must %80, Nice %20)
    must_cov = compute_skill_coverage(cv_skills_lower, must_have_set)
    nice_cov = compute_skill_coverage(cv_skills_lower, nice_to_have_set)
    
    # Skills alt skoru (0-100 arası)
    skills_sub = round(100 * (0.8 * must_cov + 0.2 * nice_cov))
    
    # 3. Diğer Alt Skorlar (Şimdilik statik, LLM/NLP ile dinamikleşecek)
    subs = {
        "skills": skills_sub,
        "experience": 60,  # Planındaki 'Relevance' kısmı
        "impact": 40,      # Planındaki 'Impact & Metrics' kısmı
        "ats": 75,         # Planındaki 'ATS Hygiene' kısmı
        "portfolio": 50    # Planındaki 'Portfolio Proof' kısmı
    }
    
    # 4. Toplam Skor (Senin planındaki ağırlıklarla: %35 Skills, %25 Exp, %15 Impact, %15 Portfolio, %10 ATS)
    total = round(
        0.35 * subs["skills"] + 
        0.25 * subs["experience"] + 
        0.15 * subs["impact"] + 
        0.15 * subs["portfolio"] + 
        0.10 * subs["ats"]
    )
    
    return {
        "fit_score": total, 
        "subscores": subs,
        "missing_must": missing_must,
        "missing_nice": missing_nice
    }