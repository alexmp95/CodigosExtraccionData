# Instalar la libreria nltk
# Se lee una cadena como entrada, no un archivo
import io
from nltk.corpus import stopwords
stop_words = set(stopwords.words('spanish'))
file1 = open("C:/Users/Alexis/Desktop/Pruebas/Data/Txt/2627062021 DIARIO CRONICA LOJA.pdf.txt", encoding='utf-8')

# Metodo que lee el contenido del archivo como una secuencia
line = file1.read()
words = line.split()
for r in words:
	if not r in stop_words:
		appendFile = open('C:/Users/Alexis/Desktop/Pruebas/Data/StopWords/2627062021 DIARIO CRONICA LOJA.pdf.txt','a', encoding='utf-8')
		appendFile.write(" "+r)
		appendFile.close()


