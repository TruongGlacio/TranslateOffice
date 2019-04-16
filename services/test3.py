import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams

def extract_text_from_pdf(pdf_path):
    print('start get text')
    textList=list()
    codec = 'utf-8'
    laparams = LAParams()    
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True,check_extractable=True):
            resource_manager = PDFResourceManager()
            fake_file_handle = io.StringIO()
            converter = TextConverter(resource_manager, fake_file_handle,codec=codec, laparams=laparams)
            page_interpreter = PDFPageInterpreter(resource_manager, converter)
            page_interpreter.process_page(page)
            text = fake_file_handle.getvalue()
            textList.append(text)
            print('text=',text)
            
            # close open handles
            converter.close()
            fake_file_handle.close()    
    return textList
         
def main():
    inputpdfFile='/media/glacio/Data/Translate/Project/pdf/abc.pdf'
    DpcumentText=extract_text_from_pdf(inputpdfFile)
    for page in DpcumentText:
        print(page)   
    
if __name__ == '__main__':
    main()