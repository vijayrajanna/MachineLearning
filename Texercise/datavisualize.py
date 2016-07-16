from os.path import join, dirname, abspath
import xlrd
import os


# Open the workbook

lst = os.listdir("/Users/vijayrajanna/Desktop/final_data")
print lst

path = '/Users/vijayrajanna/Desktop/final_data/'
for file in range(0,len(lst)):
    filename = path + lst[file]

    xl_workbook = xlrd.open_workbook(filename)

    # List sheet names, and pull a sheet by name
    #
    sheet_names = xl_workbook.sheet_names()
    # print('Sheet Names', sheet_names)

    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])

    # Or grab the first sheet by index
    #  (sheets are zero-indexed)
    #
    xl_sheet = xl_workbook.sheet_by_index(0)
    # print ('Sheet name: %s' % xl_sheet.name)

    # Pull the first row by index
    #  (rows/columns are also zero-indexed)
    #
    # row = xl_sheet.row(0)

    print 'Number of rows ',xl_sheet.nrows
    for index in range(0,xl_sheet.nrows):
        row = xl_sheet.row(index)
        print
        print '{} {} {}'.format(row[1].value, row[2].value, row[3].value)

# # Print 1st row values and types
# from xlrd.sheet import ctype_text
# print('(Column #) type:value')
# for idx, cell_obj in enumerate(row):
#     cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
#     print('(%s) %s %s' % (idx, cell_type_str, cell_obj.value))
#
# # Print all values, iterating through rows and columns
# #
# num_cols = xl_sheet.ncols   # Number of columns
# for row_idx in range(0, xl_sheet.nrows):    # Iterate through rows
#     print ('-'*40)
#     print ('Row: %s' % row_idx)   # Print row number
#     for col_idx in range(0, num_cols):  # Iterate through columns
#         cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
#         print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))



