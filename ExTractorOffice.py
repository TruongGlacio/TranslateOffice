import DocxExtractor
import ExcelExtractor
import PPTExtractor
import ConstDefine

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
        
    def GetZipFolder(self):
        print('zipFolder=',zipFolder)  
        
        return zipFolder
    def SetZipFolder(self,zipfolder):
        global zipFolder
        zipFolder=zipfolder    
    def ReadText(self, inputOfficePath):
        FileName=os.path.basename(inputOfficePath)   
        print('baseName:',FileName)
        FILE_EXTENTION=os.path.splitext(FileName)[1]
        if(FILE_EXTENTION==ConstDefine.WORD_EXTENSION):
            print('file is .docx file')
            jsonTextList=doc.ReadWordText(inputOfficePath)
            ExtractorOffice.SetCount(self, doc.GetCount())
            ExtractorOffice.SetZipFolder(self,doc.GetZipFolder())
        elif(FILE_EXTENTION==ConstDefine.EXCEL_EXTENTION):
            print('file is .docx file')
        elif(FILE_EXTENTION==ConstDefine.PPT_EXTENTION):
            print('file is .docx file')
        else:
            print('Not support file format')
        
        