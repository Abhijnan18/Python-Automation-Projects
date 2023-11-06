'''
📜 PDF Table Extraction and CSV Storage 📊
'''
import tabula

# PDF file to extract tables from
pdf_file = "points_table.pdf"

# Extract tables from the PDF
tables = tabula.read_pdf(pdf_file, pages='all')

# Check if any tables were found in the PDF
if len(tables) == 0:
    print("No tables found in the PDF.")
else:
    # Export the first table to a CSV file
    first_table = tables[0]
    first_table.to_csv("output_table.csv", index=False)

    print("First table extracted and exported to 'output_table.csv'.")


