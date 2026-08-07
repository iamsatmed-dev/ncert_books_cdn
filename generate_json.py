import json
import os
import pypdf

# Load metadata
with open('books_metadata.json', 'r', encoding='utf-8') as f:
    metadata = json.load(f)

# Keep track of unique JSON paths we've written (some metadata entries have same rel_path)
processed_paths = set()

for item in metadata:
    rel_path = item['rel_path']
    if rel_path in processed_paths:
        continue

    if os.path.exists(rel_path):
        json_path = rel_path.replace('.pdf', '.json')
        print(f"Processing {rel_path} -> {json_path}")

        text = ""
        try:
            reader = pypdf.PdfReader(rel_path)
            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        except Exception as e:
            print(f"Error reading {rel_path}: {e}")

        # Write individual json
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                "id": item['id'],
                "filename": item['filename'],
                "rel_path": rel_path,
                "text": text
            }, f, ensure_ascii=False, indent=2)

        processed_paths.add(rel_path)

print(f"Processed {len(processed_paths)} PDF files.")

# Generate books_metadata.js
with open('books_metadata.js', 'w', encoding='utf-8') as f:
    f.write("export const booksMetadata = ")
    json.dump(metadata, f, ensure_ascii=False, indent=2)
    f.write(";\n")
print("Generated books_metadata.js")
