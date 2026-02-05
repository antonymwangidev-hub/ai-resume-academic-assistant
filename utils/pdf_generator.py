from fpdf import FPDF

def generate_pdf(text, filename="output.pdf"):
    """
    Generates a simple PDF from text and returns the PDF as bytes.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)
    
    # Split text into lines
    lines = text.split("\n")
    for line in lines:
        pdf.multi_cell(0, 8, line)
    
    # Output PDF to bytes
    import io
    pdf_bytes = io.BytesIO()
    pdf.output(pdf_bytes)
    pdf_bytes.seek(0)
    return pdf_bytes.getvalue()

