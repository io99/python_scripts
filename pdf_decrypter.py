
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




import os
import PyPDF2 

read_file = open('dictionary.txt')
#the file which contains all the words
file_content = read_file.read()

wordlist = file_content.split('\n')

thispdfreader = PyPDF2.PdfFileReader(open('pdffilename', 'rb'))

#checking the file for encryption

try:
	if pdfreader.isEncrypted == True:
		for word in wordlist:
			pdfreader.decrypt(word)
			if(decrypt()):
				return 1
			elif not(decrypt()):
				return 0
			else:
				pdfreader.numPages







import os
import PyPDF2

#reading the dictionary file for decrypting

read_file = open('dictionary.txt')
file_content = read_file.read()

wordlist = file_content.split('\n')

#opening the pdf file

open_pdf = PdfFileReader.pdfreader(open('javi.pdf', 'rb'))

try:
	if pdfreader.isEncrypted() == True:
		for word in wordlist:
			pdfreader.decrypt(word)
			if (decrypt()):
				return 1
			elif not(decrypt()):
				return 0
			else:
				pdfreader.numPages




import os
import PyPDF2

read_file = open('dictionary.txt')
file_content = read_file.read()
#splitting the string
wordlist = word.split('\n')

#read the pdf file

pdfread = PyPDF2.ppdfreader(open('jacbob.pdf','rb'))

try:
	if pdfreader.isEncrypted == True:
		for word in wordlist:
		pdfreader.decrypt(word)
		if decrypt(word):
			return True
			elif not(decrypt())
			return 0
		else:
			return
			pdfreader.numPages


































import os

import PyPDF2

# Opening the dictionary file that contains all the possible combinations of words
read_file = open('dictionary.txt')
file_content = read_file.read()

# Making a list of word strings by reading this file
wordlist = file_content.split('\n')

# Using PyPDF2 module to read pdf files
pdfreader = PyPDF2.PdfFileReader(open('pdf_file','rb'))

# Checking whether the file is encrypted or not
try:
	if pdfreader.isEncrypted == True:
		for word in wordlist:
			pdfreader.decrypt(word)
			if (decrypt()): return 1
			elif not (decrypt()): return 0
	else:

		# If the file is not encrypted then simply open the file
		pdfreader.numPages