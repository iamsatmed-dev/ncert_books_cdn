import json
import os
import pypdf

def extract_text_pypdf(pdf_path):
    text = ""
    try:
        reader = pypdf.PdfReader(pdf_path)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

metadata = []
with open('books_metadata.json', 'r') as f:
    metadata = json.load(f)

for item in metadata:
    rel_path = item['rel_path']
    if os.path.exists(rel_path):
        json_path = rel_path.replace('.pdf', '.json')
        print(f"Processing {rel_path} -> {json_path}")
        text = extract_text_pypdf(rel_path)

        # Save individual JSON
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                "id": item['id'],
                "filename": item['filename'],
                "rel_path": rel_path,
                "text": text
            }, f, ensure_ascii=False, indent=2)

print("Done")
