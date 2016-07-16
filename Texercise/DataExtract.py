# Program to extract data from exel files
import xlrd
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Open the workbook
lst = os.listdir('/Users/vijayrajanna/Desktop/final_data')
path = '/Users/vijayrajanna/Desktop/final_data/'

x_values = []
y_values = []
z_values = []

# Now generate a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

import colorsys

N = 6
numberOfFiles = 0


HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
colors = ['red','blue','green','cyan','yellow','violet']

for file in range(0,len(lst)):
    filename = path + lst[file]

    # Open the workbook

    xl_workbook = xlrd.open_workbook(filename)

    # List sheet names, and pull a sheet by name
    sheet_names = xl_workbook.sheet_names()
    # print('Sheet Names', sheet_names)

    # Allfiles have just one sheet
    xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
    # print ('Sheet name: %s' % xl_sheet.name)

    # Pull the rows by index and print the values
    if xl_sheet.nrows < 10:
        continue
    numberOfFiles += 1
    print filename,
    print 'File count {}'.format(numberOfFiles),
    print 'Number of rows ',xl_sheet.nrows,
    print 'Time taken ',(xl_sheet.row(xl_sheet.nrows-1)[0].value - xl_sheet.row(0)[0].value)

    for index in range(0,xl_sheet.nrows):
        row = xl_sheet.row(index)
        x_values.append(row[1].value)
        y_values.append(row[2].value)
        z_values.append(row[3].value)
        ax.scatter(row[1].value, row[2].value, row[3].value, c=colors[N-1], edgecolor='none', depthshade='True',  s=20)
        # print '{} {} {}'.format(row[1].value, row[2].value, row[3].value)

    if N == 0:
        N = 6
    else:
        N = N -1

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()

