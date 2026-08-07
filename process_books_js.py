import json

with open('books_metadata.json', 'r', encoding='utf-8') as f:
    metadata = json.load(f)

# Optional: if you wanted to include text in books_metadata.js, but user said "saprate" JSON for text,
# so we just export metadata.
with open('books_metadata.js', 'w', encoding='utf-8') as f:
    f.write('export const booksMetadata = ')
    json.dump(metadata, f, ensure_ascii=False, indent=2)
    f.write(';\n')
