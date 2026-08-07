import json
import os
import sys

try:
    from PyPDF2 import PdfReader
except ImportError:
    print("PyPDF2 not installed")
    sys.exit(1)

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text

pdf_path = "./12th/physics/chapter_04/english.pdf"
try:
    text = extract_text(pdf_path)
    print(f"Extracted {len(text)} characters from {pdf_path}")
    print(text[:100])
except Exception as e:
    print(f"Error: {e}")
