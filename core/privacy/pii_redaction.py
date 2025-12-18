import re

# E-posta ve Telefon numaralarını yakalayan dedektifler
PII_PATTERNS = [
    (re.compile(r"\b[\w\.-]+@[\w\.-]+\.\w+\b"), "[REDACTED_EMAIL]"),
    (re.compile(r"\b(\+?\d[\d\s\-\(\)]{7,}\d)\b"), "[REDACTED_PHONE]"),
]

def redact_pii(text: str) -> str:
    """Metindeki hassas bilgileri gizler."""
    out = text
    for pat, repl in PII_PATTERNS:
        out = pat.sub(repl, out)
    return out