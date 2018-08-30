
import os 
import PyPDF2
#opening the file
read_file = open('dictionary.txt')
file_content = read_file.read() 

#making a list of strings by reading this file

wordlist = file_content.split('\n')

#use pypdf2 module to read our pdf files

pdfreader = PyPDF2.PdfFileReader(open('pdf_file','rb'))

#checking whether the file is encrypted or not
try:
	if pdfreader.isEncrypted == True:
		for word in wordlist:
			pdfreader.decrypt(word)
			if (decrypt()):
				return 1
		elif not( decrypt()):
			return 0
		#if the file is not encrypted open the file.
		else:
			pdfreader.numPages


