from pathlib import Path

def extract_text(file_path: str) -> str:
    p = Path(file_path)
    if p.suffix.lower() == ".pdf":
        import pypdf
        reader = pypdf.PdfReader(str(p))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif p.suffix.lower() in [".docx", ".doc"]:
        import docx
        d = docx.Document(str(p))
        return "\n".join(par.text for par in d.paragraphs)
    else:
        raise ValueError("Desteklenmeyen dosya formatı!")