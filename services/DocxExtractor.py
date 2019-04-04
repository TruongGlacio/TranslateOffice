try:
    from xml.etree.cElementTree import XML
    import xml.etree.cElementTree as ET 
except ImportError:
    from xml.etree.ElementTree import XML

import os
import GeneralFuntions
import ConstDefine
generalFunctions=GeneralFuntions.General() 
LenghtListOutput=0
zipFolder=''
class DocxExtractor:

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

    def ReadWordText(self,inputPath,outputTextFilepath):
        """
        Take the path of a docx file as argument, return the text in unicode.
        """     
        folderZipFile=generalFunctions.extraZipfile(inputPath)
        if(folderZipFile==None):
            print ('Error When Extral file')
            return None 
        DocxExtractor.SetZipFolder(self,folderZipFile)
        xmlListFilePath=generalFunctions.GetPathWordXml(folderZipFile)
        print('xmlFilePath is:',xmlListFilePath)
        paragraphs = list()        
        for xmlPath in xmlListFilePath:
            paragraphs=generalFunctions.ReadTextXmlFile(xmlPath,paragraphs,ConstDefine.WORD_NAMESPACE,ConstDefine.WORD_PARA,ConstDefine.WORD_TEXT)
        print('count', len(paragraphs))   
        DocxExtractor.SetCount(self,len(paragraphs))
        jsonTextList=generalFunctions.ConvertStringToJson(paragraphs)
        generalFunctions.WriteTextFile(jsonTextList, outputTextFilepath)        
        return outputTextFilepath

        #........Write Text ...................#
    def WriteTextFromJson(seft, inputPath,textListJson,cout):
        textListInput=list()
        if(textListJson==None):
            print('input not incorrect, go exit ')
            return None
        textListInput=generalFunctions.ConvertJsonToString(textListJson)
        if(len(textListInput)==cout):
            i=0
            print("number item correct, do write")
            xmlListFilePath=generalFunctions.GetPathWordXml(inputPath)
            print('xmlFilePath is:',xmlListFilePath)
            for xmlPath in xmlListFilePath:
                i=generalFunctions.WriteTextXmlFile(xmlPath,ConstDefine.WORD_NAMESPACE,ConstDefine.WORD_PARA,ConstDefine.WORD_TEXT,textListInput,i)      
            # get parent path of file path
            parentPath=os.path.abspath(os.path.join(inputPath, os.pardir))   
            baseFolderName=os.path.basename(inputPath)   
            docFileTarget=parentPath+'/'+baseFolderName+'.docx'
            compressZipFilePath=generalFunctions.CompressOfficeFolder(inputPath)
            if(compressZipFilePath==None):
                print('erro compress file')
                return None
            os.rename(compressZipFilePath, docFileTarget)
            print('input path :', inputPath)  
            return docFileTarget
        else:
            print("number item incorrect, exit")
            return None            