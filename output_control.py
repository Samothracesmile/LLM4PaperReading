# output control code

import fitz
import subprocess
import os
from fpdf import FPDF
import textwrap
import re

def extract_text_from_pdf(pdf_path, max_pages=50):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(min(len(doc), max_pages)):
        page = doc[page_num]
        text += page.get_text()
    return text

def convert_markdown_to_plain_text(md_text):
    text = md_text
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"###\s*", "", text)
    text = re.sub(r"##\s*", "", text)
    text = re.sub(r"#\s*", "", text)
    text = text.replace("<think>", "").replace("</think>", "")
    text = re.sub(r"(?<!\n)(\d+\.\s+)", r"\n\1", text)
    return text

def extract_post_think_text(full_text):
    parts = full_text.split("</think>")
    return parts[1].strip() if len(parts) > 1 else full_text



    