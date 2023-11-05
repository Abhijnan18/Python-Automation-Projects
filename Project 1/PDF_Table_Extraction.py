'''
📜 PDF Table Extraction and CSV Storage 📊
'''
import camelot

# Read tables from the PDF file
tables = camelot.read_pdf('points_table.pdf', pages='1')

# Export the first table to a CSV file
if tables:
    tables[0].to_csv('points_table.csv')
else:
    print("No tables found in the PDF.")
