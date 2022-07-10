#Codigo que permite convertir un archivo en formato doxc a formato Txt de forma Individual
#instalar la libreria docx2txt
#Extrae la informacion del documento y la almacena 100% en texto plano
import docx2txt
text = docx2txt.process("C:/Users/Alexis/Desktop/Pruebas/V2/data/PIS.docx")
with open("C:/Users/Alexis/Desktop/Pruebas/V2/data/output.txt", "w", encoding='utf-8') as text_file:
    print(text, file=text_file)