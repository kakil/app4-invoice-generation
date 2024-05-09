import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")
print(filepaths)

# Create the dataframe
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)

    # Create the PDF
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Get the filename and date
    filename = Path(filepath).stem
    # invoice_nr = filename.split("-")[0]
    # invoice_date = filename.split("-")[1]
    invoice_nr, date = filename.split("-")
    print(f"Invoice #: {invoice_nr}")
    print(f"Invoice date: {date}")

    # Create the cell
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}")



    pdf.output(f"PDFs/{filename}.pdf")




