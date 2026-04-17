#!/usr/bin/env python3
"""
analyze_document.py - Helper script for the legal-document-explainer skill.
Extracts text from various file formats for legal analysis.
"""

import sys
import os
from pathlib import Path

def extract_from_pdf(file_path):
    try:
        import PyPDF2
        text = ""
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except ImportError:
        return "[Error: PyPDF2 not installed. Please install it with 'pip install PyPDF2']"
    except Exception as e:
        return f"[Error extracting from PDF: {e}]"

def extract_from_docx(file_path):
    try:
        import docx
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except ImportError:
        return "[Error: python-docx not installed. Please install it with 'pip install python-docx']"
    except Exception as e:
        return f"[Error extracting from Word: {e}]"

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_document.py <file_path>")
        sys.exit(1)

    file_path = Path(sys.argv[1])
    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    suffix = file_path.suffix.lower()
    
    if suffix == '.pdf':
        print(extract_from_pdf(file_path))
    elif suffix in ['.docx', '.doc']:
        print(extract_from_docx(file_path))
    else:
        # Assume text/markdown
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                print(f.read())
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
