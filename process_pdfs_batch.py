import json
import os
import pypdf
import sys

def process_batch(start_idx, end_idx):
    with open('books_metadata.json', 'r', encoding='utf-8') as f:
        metadata = json.load(f)

    unique_paths = []
    seen = set()
    for item in metadata:
        if item['rel_path'] not in seen:
            seen.add(item['rel_path'])
            unique_paths.append(item)

    batch = unique_paths[start_idx:end_idx]

    for item in batch:
        rel_path = item['rel_path']
        if os.path.exists(rel_path):
            json_path = rel_path.replace('.pdf', '.json')
            if os.path.exists(json_path):
                continue

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

            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump({
                    "id": item['id'],
                    "filename": item['filename'],
                    "rel_path": rel_path,
                    "text": text
                }, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        process_batch(int(sys.argv[1]), int(sys.argv[2]))
    else:
        # Run all sequentially, printing progress
        with open('books_metadata.json', 'r', encoding='utf-8') as f:
            metadata = json.load(f)

        unique_paths = []
        seen = set()
        for item in metadata:
            if item['rel_path'] not in seen:
                seen.add(item['rel_path'])
                unique_paths.append(item)

        total = len(unique_paths)
        print(f"Total unique PDFs: {total}")

        # Parallel execution script
        with open('run_all.sh', 'w') as f:
            f.write("#!/bin/bash\n")
            batch_size = 5
            for i in range(0, total, batch_size):
                f.write(f"python process_pdfs_batch.py {i} {min(i+batch_size, total)} &\n")
            f.write("wait\n")
            f.write("print 'All done'\n")
