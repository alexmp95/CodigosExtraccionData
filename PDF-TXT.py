# Codigo que permite convertir  un lote de archivos en formato PDF a  formato txt
# Para un correcto funcionamiento se debe instalar las librerias IO,OS, pdfminer.

import io
import os
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


# convierte el pdf, devuelve su contenido de texto como una cadena
def convert (fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = io.StringIO()
    infile = open(fname, 'rb')
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

#Conversion multiple en base a los archivos que se encuentre en la carpeta
def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\"
    for pdf in os.listdir(pdfDir):
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            text = convert(pdfFilename)  # obtener una cadena de contenido de texto de pdf
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w", encoding='utf-8')  # hacer archivo de texto
            textFile.write(text)  # escribir el texto
        # textFile.close


pdfDir = "C:/Users/Alexis/Desktop/Pruebas/Data/Pdf/"#Carpeta con todos los archivos a convertir PDF#
txtDir = "C:/Users/Alexis/Desktop/Pruebas/Data/Txt/" # Carpeta que almacena los archivos convertidos TXT
convertMultiple(pdfDir, txtDir)