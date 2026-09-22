"""
NCERT Automated Diagram & Vector Graphic Extractor
SAT-CORE Web Portal / NCERT CDN
Extracts high-resolution 300 DPI vector diagrams from NCERT PDFs
and generates responsive Diagram Card markup for Clean Markdown.
"""

import sys
import os
import re
import pymupdf

def extract_diagrams(pdf_path, output_dir, prefix=""):
    os.makedirs(output_dir, exist_ok=True)
    doc = pymupdf.open(pdf_path)
    print(f"[*] Processing {os.path.basename(pdf_path)} ({len(doc)} pages)...")
    
    fig_pattern = re.compile(r'(?:Fig\.|Figure|चित्र)\s*(\d+[\.\d]*)', re.IGNORECASE)
    extracted = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("blocks")
        drawings = page.get_drawings()
        
        for b in blocks:
            text = b[4].strip()
            # Match figure caption lines
            if text.startswith("Fig.") or text.startswith("Figure") or text.startswith("चित्र") or "\nFig." in text or "\nचित्र" in text:
                m = fig_pattern.search(text)
                if not m:
                    continue
                
                fig_num = m.group(1).replace(" ", "")
                caption = text.replace("\n", " ").strip()
                caption_rect = pymupdf.Rect(b[:4])
                
                # Find drawings above this caption
                above_drawings = [
                    d["rect"] for d in drawings
                    if d["rect"].y1 <= caption_rect.y1 + 10 and d["rect"].y0 >= max(0, caption_rect.y0 - 320)
                ]
                
                if not above_drawings:
                    continue
                
                # Compute bounding rectangle
                diag_rect = above_drawings[0]
                for r in above_drawings[1:]:
                    diag_rect |= r
                
                # Add slight padding
                crop_rect = pymupdf.Rect(
                    max(30, diag_rect.x0 - 10),
                    max(30, diag_rect.y0 - 10),
                    min(page.rect.width - 30, diag_rect.x1 + 10),
                    min(page.rect.height, caption_rect.y1 + 5)
                )
                
                filename = f"{prefix}fig_{fig_num.replace('.', '_')}.png"
                out_path = os.path.join(output_dir, filename)
                
                pix = page.get_pixmap(clip=crop_rect, dpi=300)
                pix.save(out_path)
                
                extracted.append({
                    "fig_num": fig_num,
                    "page": page_num + 1,
                    "caption": caption,
                    "filename": filename,
                    "width": pix.width,
                    "height": pix.height
                })
                print(f"  [+] Page {page_num + 1}: Extracted Fig. {fig_num} -> {filename} ({pix.width}x{pix.height})")
                
    print(f"[OK] Extracted {len(extracted)} diagrams into {output_dir}")
    return extracted

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_diagrams.py <pdf_path> <output_dir> [prefix]")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    out_dir = sys.argv[2]
    pfx = sys.argv[3] if len(sys.argv) > 3 else ""
    extract_diagrams(pdf_path, out_dir, pfx)
