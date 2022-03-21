

"""
import zipfile

# zip file handler
zip = zipfile.ZipFile('C:/Users/Ertugrul/Desktop/zipdeneme.zip')

# list available files in the container
print (zip.namelist())

# extract a specific file from the zip container
f = zip.open("zipname.txt")


# save the extraced file
content = f.read()

f = open('zipname.txt', 'wb')
f.write(content)
#f.close()
"""


# import xlsxwriter module
import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('C:/Users/Ertugrul/Desktop/pytdeneme.xlsx')

# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()

# Use the worksheet object to write
# data via the write() method.
worksheet.write('A1', 'Hello..')

worksheet.write('C1', 'For')
worksheet.write('D1', 'Geeks')
worksheet._write_color('ertu',3)

# Finally, close the Excel file
# via the close() method.
workbook.close()




