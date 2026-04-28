from docx import Document
import PyPDF2
import io

def extract_text_from_docx(file_bytes):
    file=io.BytesIO(file_bytes)
    doc =Document(file)
    return " ".join([p.text for p in doc.paragraphs])


def extract_text_from_pdf(file_bytes):
    file=io.BytesIO(file_bytes)
    reader=PyPDF2.PdfReader(file)
    return " ".join([page.extract_text() or "" for page in reader.pages])

def extract_text(filename,content):
    filename=filename.lower()

    if filename.endswith(".docx"):
        return extract_text_from_docx(content)

    elif filename.endswith(".pdf"):
        return extract_text_from_pdf(content)
    
    elif filename.endswith(".txt"):
        return content.decode("utf-8")
    
    else:
        raise ValueError(f"Unsupported file format{filename}")