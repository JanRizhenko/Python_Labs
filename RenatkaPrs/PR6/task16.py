spreadsheet = {}

inputs = [
    "A1 300",
    "B1 2050",
    "B2 Python"
]

for entry in inputs:
    cell, value = entry.split(maxsplit=1)
    col, row = cell[0], cell[1:]
    spreadsheet[(col, row)] = value

for cell, value in spreadsheet.items():
    print(cell, value)
