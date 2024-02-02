#Exercise 8:merging PDF files
from PyPDF2 import PdfWriter
import os
merger = PdfWriter()
files = [file for file in os.listdir() if file.endswith(".pdf")]
#mention existing file folder in for loop

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()