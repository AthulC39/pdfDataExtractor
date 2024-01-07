import pandas as pd
import tabula 
import fitz

pdfName = "SF-3-001.pdf"

#open and get the dimensions of pdf
document = fitz.open(pdfName)
page = document[0]      

#define area parameters of table we want to extract
#left
x1=(page.rect.width * 0.55)
#left + width
x2=page.rect.width
#top + height
y2=(page.rect.height * 0.35)
#top
y1=0

#read the table
dfs = tabula.read_pdf(pdfName,pages="1", relative_area=False,area=(y1,x1,y2,x2))

print(dfs[0])

 

tabula.convert_into("SF-3-001.pdf","test2.tsv",output_format="tsv",pages="1",relative_area=False,area=(y1,x1,y2,x2))