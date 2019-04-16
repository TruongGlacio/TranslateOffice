import DocxExtractor
import ExcelExtractor
import PPTExtractor
import PDFExtractor
import TXTExtractor
import ConstDefine
import os

FILE_EXTENTION=''
LenghtListOutput=0
doc=DocxExtractor.DocxExtractor()
ppt=PPTExtractor.PPTExtractor()   
excel=ExcelExtractor.ExcelExtrator()
pdf=PDFExtractor.PDFExtractor()
txt=TXTExtractor.TXTExtractor()
class ExtractorOffice:
    def __init__(self):
        pass  
    #/........Read text from doc......../    
    def GetCount(self):
        print('LenghtListOutput=',LenghtListOutput)
        return LenghtListOutput
    
    def SetCount(seft,count):
        global LenghtListOutput
        LenghtListOutput=count
        
    def GetExtentionFile(self):
        return FILE_EXTENTION;
    
    def SetExtentionFile(self,extentionfile):
        global FILE_EXTENTION
        FILE_EXTENTION=extentionfile
           
    def GetZipFolder(self):
        print('zipFolder=',zipFolder)          
        return zipFolder
    
    def SetZipFolder(self,zipfolder):
        global zipFolder
        zipFolder=zipfolder    
        
        # value return is a list include : dataStruct=[outputTextFile,Count, ZipFolder, FILE_EXTENTION]
    def ReadText(self, inputOfficePath,outputTextFile):  
        dataStruct=list();       
        FileName=os.path.basename(inputOfficePath)   
        print('baseName:',FileName)
        ExtractorOffice.SetExtentionFile(self,os.path.splitext(FileName)[1])   
        # detect word file (.docx)        
        if(FILE_EXTENTION==ConstDefine.WORD_EXTENSION):
            print('file is .docx file')
            outputTextFile=doc.ReadWordText(inputOfficePath,outputTextFile)
            ExtractorOffice.SetCount(self, doc.GetCount())
            ExtractorOffice.SetZipFolder(self,doc.GetZipFolder())
            
        # detect Excel file (.xlsx)                
        elif(FILE_EXTENTION==ConstDefine.EXCEL_EXTENTION):
            print('file is .xlsx file')
            outputTextFile=excel.ExcelReadText(inputOfficePath,outputTextFile)
            ExtractorOffice.SetCount(self, excel.GetCount())
            ExtractorOffice.SetZipFolder(self,excel.GetZipFolder())
                              
        # detect PPT file (.pptx)                
        elif(FILE_EXTENTION==ConstDefine.PPT_EXTENTION):
            print('file is .pptx file')
            outputTextFile=ppt.ReadTextFromPPT(inputOfficePath,outputTextFile)
            ExtractorOffice.SetCount(self, ppt.GetLength())
            ExtractorOffice.SetZipFolder(self,ppt.GetZipFolder())  
            
         # detect PDF file (.pdf) 
        elif(FILE_EXTENTION==ConstDefine.PDF_EXTENTION):
            print('file is.pdf file')
            outputTextFile=pdf.ReadTextFromPdf(inputOfficePath,outputTextFile)
            ExtractorOffice.SetCount(self, pdf.GetLength())            
            ExtractorOffice.SetZipFolder(self,pdf.GetZipFolder())  

        # detect PDF file (.txt)         
        elif(FILE_EXTENTION==ConstDefine.TXT_EXTENTION):
            print('file is.txt file')
            outputTextFile=txt.ReadTextFromTXT(inputOfficePath,outputTextFile)
            ExtractorOffice.SetCount(self, txt.GetLength())            
            ExtractorOffice.SetZipFolder(self,txt.GetZipFolder())   
            
        # other format
        else:
            print('Not support file format')
            return None
        dataStruct.append(outputTextFile)
        dataStruct.append(ExtractorOffice.GetCount(self))            
        dataStruct.append(ExtractorOffice.GetZipFolder(self))
        dataStruct.append(FILE_EXTENTION)                   
        return dataStruct;        
        
    def WriteText(seft,jsonListInput): # input value is list include jsonListInput=[outputTextFile,Count, ZipFolder, FILE_EXTENTION]
        
        jsonTextFile=jsonListInput[0]
        count=jsonListInput[1]
        inputPath=jsonListInput[2]
        fileExtention=jsonListInput[3]
        
        with open(jsonTextFile, encoding='utf8') as f:
            textListJson = f.read().strip()            
        print('file extention:',fileExtention)
        # detect word file (.docx)
        if(fileExtention==ConstDefine.WORD_EXTENSION):
            print('file is .docx file')
            docFileTarget=doc.WriteTextFromJson(inputPath,textListJson,count)
            return docFileTarget
        # detect Excel file (.xlsx)        
        elif(fileExtention==ConstDefine.EXCEL_EXTENTION):
            print('file is .xlsx file')
            excelFileTarget=excel.ExcelWriteTextFromJson(inputPath, textListJson,count)
            return excelFileTarget
        # detect ppt file (.pptx)  
        elif(fileExtention==ConstDefine.PPT_EXTENTION):
            print('file is .docx file')
            pPTFileTarget=ppt.WriteTextFromJson(inputPath,textListJson,count)
            return pPTFileTarget 
        # detect pdf file (.pdf)  
        elif(fileExtention==ConstDefine.PDF_EXTENTION):
            #print('file is .docx file')
            #pDfFileTarget=ppt.WriteTextFromJson(inputPath,textListJson,count)
            #return pDfFileTarget
            return None            
        # detect pdf file (.txt)  
        elif(fileExtention==ConstDefine.TXT_EXTENTION):
            print('file is .TXT file')
            txtFileTarget=txt.WriteTextFromJson(inputPath,textListJson)
            return txtFileTarget
        
        # other format
        else:
            print('Not support file format')  
            return None
        