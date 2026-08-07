import pdfplumber

def extract_text_pdfplumber(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error: {e}")
    return text

pdf_path = "./12th/physics/chapter_04/english.pdf"
text = extract_text_pdfplumber(pdf_path)
print(f"Extracted {len(text)} characters from {pdf_path}")
print(text[:100])
