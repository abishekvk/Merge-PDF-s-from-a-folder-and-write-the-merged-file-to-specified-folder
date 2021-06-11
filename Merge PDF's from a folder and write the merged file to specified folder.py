# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 17:30:40 2021

@author: abishek.kandiyil
"""


from PyPDF2 import PdfFileMerger
import glob

archive_path='C:\\my files'
path =r'C:\PDF'  #path where the files kept
file_loc = glob.glob(path + "/*.PDF")      #generating list of file with location from the path

merger = PdfFileMerger()

for pdf in file_loc:
    merger.append(pdf)

merger.write("D:\\result.pdf")
