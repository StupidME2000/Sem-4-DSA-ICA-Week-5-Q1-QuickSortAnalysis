import csv
from openpyxl import Workbook

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Open the CSV file and read its data
with open('QuickSortRandom.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # Write each row of the CSV file to the spreadsheet
        ws.append(row)

# Save the spreadsheet as a new file
wb.save('output_Random.xlsx')

with open('QuickSortWorst.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # Write each row of the CSV file to the spreadsheet
        ws.append(row)

# Save the spreadsheet as a new file
wb.save('output_Worst.xlsx')
