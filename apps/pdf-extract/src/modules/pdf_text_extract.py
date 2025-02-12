# my program test

import PyPDF2
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure
import pdfplumber
import os
import re
from modules.tasks import *

def pdf_text_extract(pdf_path):
    # Find the PDF path
    #pdf_path = '../etl_sample.pdf'

    # create a PDF file object
    pdfFileObj = open(pdf_path, 'rb')
    # create a PDF reader object
    pdfReaded = PyPDF2.PdfReader(pdfFileObj)

    # Create the dictionary to extract text from each image
    text_per_page = {}
    # We extract the pages from the PDF
    for pagenum, page in enumerate(extract_pages(pdf_path)):
    
        # Initialize the variables needed for the text extraction from the page
        pageObj = pdfReaded.pages[pagenum]
        page_text = []
        table_extraction_flag= False
        # Open the pdf file
        pdf = pdfplumber.open(pdf_path)

        # Find all the elements
        page_elements = [(element.y1, element) for element in page._objs]
        # Sort the detected elements in the page
        page_elements.sort(key=lambda k: k[0], reverse=True)

        # Find the elements that composed a page
        for i,component in enumerate(page_elements):
            # Extract the element of the page layout
            element = component[1]
            
            # Check if the element is a text element
            if isinstance(element, LTTextContainer):
                # Check if the text appeared in a table
                if table_extraction_flag == False:
                    # Use the function to extract the text for each text element
                    line_text = text_extraction(element)
                    # Append the text of each line to the page text
                    # also excluding text extracted from figures captions, using regex re.search
                    if not re.search('^fig', line_text, re.IGNORECASE):
                        page_text.append(line_text)
                else:
                    # nothing to do if the extracted text comes from table element
                    pass



        # define array text_per_page, its values are the text extracted from each page
        # [text extracted from page 1, text extracted from page 2, etc etc]
        text_per_page[pagenum]= page_text

    # Closing the pdf file object
    pdfFileObj.close()

    # collect all text from pdf (excluding figur captions)
    all_text_from_pdf = ''
    for i in [0,1]:
        all_text_from_pdf = all_text_from_pdf + ''.join(text_per_page[i])

    with open("./../result_text_extraction/text_extracted_from_pdf_110225.txt", "w") as f:
        f.write(all_text_from_pdf)

    return all_text_from_pdf
