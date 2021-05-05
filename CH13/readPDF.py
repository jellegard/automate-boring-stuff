#! python3
# readPDF.py - Launches a map in the browser using an address from the
# command line or clipboard.

import PyPDF2

pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()
print(pageObj.extractText())
