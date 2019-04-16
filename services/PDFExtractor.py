import io
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
import GeneralFuntions
import ConstDefine
import os

generalFunctions=GeneralFuntions.General()
filePath=''
LengthOfList=0
class PDFExtractor:
    def __init__(selt):
        pass
    
    def GetLength(self):
        return LengthOfList
    
    def SetLength(self, inputLength):
        global LengthOfList
        LengthOfList=inputLength
      
    def GetZipFolder(self): 
        return filePath
    
    def SetZipFolder(self, inpuzipfolder):
        global filePath
        filePath=inpuzipfolder    
    def ReadTextFromPdf(self,pdf_Input_Path, outputTextFile): 
        
        print('start get text from :', pdf_Input_Path)
        textList=list()
        
        folderZipFile=generalFunctions.extraZipfile(pdf_Input_Path)   
        if(folderZipFile==None or os.path.exists(folderZipFile)==False):
            print('file not exit, return None')
            return None        
        PDFExtractor.SetZipFolder(self,folderZipFile)               
        codec =ConstDefine.CODEC_READER_PDF
        laparams = LAParams()    
        with open(folderZipFile, 'rb') as fh:
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
        jsonTextList=generalFunctions.ConvertStringToJson(textList)
        PDFExtractor.SetLength(self,len(textList))
        generalFunctions.WriteTextFile(jsonTextList,outputTextFile)
        return outputTextFile
        
        
