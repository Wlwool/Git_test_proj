import re

def normalize_text(text: str) -> str:
    """


    """

    if text is None:
        raise ValueError("требуется текст")
    text = text.strip().lower()
    text = re.sub(r'[!?.]+$', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text
