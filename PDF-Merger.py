from PyPDF2 import PdfMerger

# Making a list of pdfs and a PdfMerger()
pdfs = ["1.pdf", "2.pdf"] # creates list of pdfs
merger = PdfMerger() # initialises pdf merger

# Adding pdfs in the PdfMerger()
for pdf in pdfs:
    merger.append(pdf)

# Creating a combined pdf
merger.write("Combinedpdf.pdf") # saves this with that name
merger.close()

