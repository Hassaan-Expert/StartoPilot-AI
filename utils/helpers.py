import os
import re
from fpdf import FPDF
from datetime import datetime

def generate_pdf(title: str, content: str) -> str:
    # Sanitize and truncate title for filename
    safe_title = re.sub(r'[\\/*?:"<>|\n]', "_", title)
    safe_title = safe_title.strip().replace(" ", "_").lower()

    # Truncate to max 50 characters to avoid long path errors
    safe_title = safe_title[:50]

    # Add timestamp to ensure uniqueness
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{safe_title}_{timestamp}.pdf"

    # Ensure export directory exists
    export_dir = "exports"
    os.makedirs(export_dir, exist_ok=True)

    path = os.path.join(export_dir, filename)

    # Create the PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=title.upper(), ln=True, align="C")
    pdf.ln(10)

    for line in content.split("\n"):
        pdf.multi_cell(0, 10, txt=line.strip())

    pdf.output(path)
    return path
