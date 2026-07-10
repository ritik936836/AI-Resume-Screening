import fitz  # PyMuPDF

def extract_text(pdf_path):
    text = ""

    pdf = fitz.open(pdf_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text


# Test
if __name__ == "__main__":

    pdf_path = "resumes/resume1.pdf"

    text = extract_text(pdf_path)

    print(text)