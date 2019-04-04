import os
import ConstDefine
import GeneralFuntions

generalFunctions=GeneralFuntions.General()
LenghtListOutput=0
zipFolder=''
class ExcelExtrator:

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

    def ExcelReadText(self,inputPath,outputTextFilePath):
        """
        Take the path of a Excel file as argument, return the text in unicode.
        """     
        folderZipFile=generalFunctions.extraZipfile(inputPath)
        if(folderZipFile==None):
            print ('Error When Extral file')
            return None 
        ExcelExtrator.SetZipFolder(self,folderZipFile)
        xmlListFilePath=generalFunctions.GetPathExcelXml(folderZipFile)
        print('xmlFilePath is:',xmlListFilePath)
        paragraphs = list()        
        for xmlPath in xmlListFilePath:
            paragraphs=generalFunctions.ReadTextXmlFile(xmlPath,paragraphs,ConstDefine.EXCEL_NAMESPACE,ConstDefine.EXCEL_PARA,ConstDefine.EXCEL_TEXT)
        print('count', len(paragraphs))   
        ExcelExtrator.SetCount(self,len(paragraphs))
        jsonTextList=generalFunctions.ConvertStringToJson(paragraphs)
        generalFunctions.WriteTextFile(jsonTextList, outputTextFilePath)        
        return outputTextFilePath                    
    def ExcelWriteTextFromJson(self,inputPath, inputListJson,count):
        textListInput=list()        
        if(inputListJson==None):
            print('input not incorrect, go exit ')
            return None
        textListInput=generalFunctions.ConvertJsonToString(inputListJson)
        if(len(textListInput)==count):
            i=0
            print("number item correct, do write")
            xmlListFilePath=generalFunctions.GetPathExcelXml(inputPath)
            print('xmlFilePath is:',xmlListFilePath)
            for xmlPath in xmlListFilePath:
                i=generalFunctions.WriteTextXmlFile(xmlPath,ConstDefine.EXCEL_NAMESPACE,ConstDefine.EXCEL_PARA,ConstDefine.EXCEL_TEXT,textListInput,i)      
            # get parent path of file path
            parentPath=os.path.abspath(os.path.join(inputPath, os.pardir))   
            baseFolderName=os.path.basename(inputPath)   
            excelFileTarget=parentPath+'/'+baseFolderName+'.xlsx'
            compressZipFilePath=generalFunctions.CompressOfficeFolder(inputPath)
            if(compressZipFilePath==None):
                print('erro compress file')
                return None
            os.rename(compressZipFilePath, excelFileTarget)
            print('input path :', inputPath)  
            return excelFileTarget
        else:
            print("number item incorrect, exit")
            return None
            