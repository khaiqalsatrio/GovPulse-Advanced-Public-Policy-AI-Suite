import re

def clean_text(text: str) -> str:
    """
    Membersihkan teks dari simbol, angka, dan mengubah ke lowercase.
    Cocok untuk normalisasi opini publik Bahasa Indonesia.
    """
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
