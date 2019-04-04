import DocxExtractor
import ExcelExtractor
import PPTExtractor
import ConstDefine
import os

FILE_EXTENTION=''

doc=DocxExtractor.DocxExtractor()
ppt=PPTExtractor.PPTExtractor()   
excel=ExcelExtractor.ExcelExtrator()
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
    def ReadText(self, inputOfficePath,outputTextFile):
        FileName=os.path.basename(inputOfficePath)   
        print('baseName:',FileName)
        ExtractorOffice.SetExtentionFile(self,os.path.splitext(FileName)[1]) 
        
        # detect word file (.docx)        
        if(FILE_EXTENTION==ConstDefine.WORD_EXTENSION):
            print('file is .docx file')
            jsonTextList=doc.ReadWordText(inputOfficePath,outputTextFile)
            ExtractorOffice.SetCount(self, doc.GetCount())
            ExtractorOffice.SetZipFolder(self,doc.GetZipFolder())
            return jsonTextList;            
        # detect Excel file (.xlsx)                
        elif(FILE_EXTENTION==ConstDefine.EXCEL_EXTENTION):
            print('file is .xlsx file')
            jsonTextList=excel.ExcelReadText(inputOfficePath,outputTextFile)
            ExtractorOffice.SetCount(self, excel.GetCount())
            ExtractorOffice.SetZipFolder(self,excel.GetZipFolder())
            return jsonTextList;                
            
        # detect PPT file (.pptx)                
        elif(FILE_EXTENTION==ConstDefine.PPT_EXTENTION):
            print('file is .pptx file')
            jsonTextList=ppt.ReadTextFromPPT(inputOfficePath,outputTextFile)
            ExtractorOffice.SetCount(self, ppt.GetCount())
            ExtractorOffice.SetZipFolder(self,ppt.GetZipFolder())            
            return jsonTextList;                
             
        # other format
        else:
            print('Not support file format')
            return None
        
    def WriteText(seft, inputPath,textListJson):
        fileExtention=ExtractorOffice.GetExtentionFile(seft);
        print('file extention:',fileExtention)
        # detect word file (.docx)
        if(FILE_EXTENTION==ConstDefine.WORD_EXTENSION):
            print('file is .docx file')
            doc.WriteTextFromJson(inputPath,textListJson)            
        # detect Excel file (.xlsx)        
        elif(FILE_EXTENTION==ConstDefine.EXCEL_EXTENTION):
            print('file is .xlsx file')
            excel.ExcelWriteTextFromJson(inputPath, textListJson)
            
        # detect ppt file (.pptx)  
        elif(FILE_EXTENTION==ConstDefine.PPT_EXTENTION):
            print('file is .docx file')
            ppt.WriteTextFromJson(inputPath,textListJson)
        
        # other format
        else:
            print('Not support file format')        
        